#!/usr/bin/env python
# -*- coding:utf-8 -*-
from listener import Listener
from comprehender import Comprehender
#from database import Database
#from drowner import Drowner

#---- enumeration ----
MODE_UNLOCK = -2
MODE_LOCKED = -1
MODE_QUIT = 0
MODE_HOME = 1
MODE_SEARCH = 2
MODE_PLAY = 3
MODE_REVIEW = 4

MAX_RETRY = 3

#---- global variable ----
listener = Listener(600)
comprehender = Comprehender()

#( get_input : unit -> (string | None) )
def get_input():
  print "* waiting input... : 入力を待っています…"
#  return listener.listen()
  result = raw_input()
  if result == "":
    return None
  else:
    return result

#( deal_with_no_recognition : int ref -> unit )
def deal_with_no_recognition(refnorecogn):

  refnorecogn += 1
  if refnorecogn < MAX_RETRY:
    print ("!---No word recognized.")
    return
  else:
    print ("!---No word recognized for three consecutive times.")
    return

#( mode_locked : unit -> mode )
def mode_locked():
  print "  [locked mode]"
  #(should be written)
  # * if 人感センサからの情報が陽性
  # *   return MODE_UNLOCK
  # * else
  return MODE_LOCKED

#( mode_unlock : unit -> mode )
def mode_unlock():

  norecogn = 0
  while norecogn < MAX_RETRY:

    print "  [unlock mode]"
    result = get_input()

    if result == None:
      deal_with_no_recognition(MODE_UNLOCK, refnorecogn)
    else:
      # * 認識された文字列をデータベースに送信
      # * if ロックが外れた:
      #     mode = MODE_HOME
      # * else:
      #     mode = MODE_LOCKED
      # * #end if
      return MODE_HOME

  #end while

#( mode_search : recogn ref -> mode )
def mode_search():

  norecogn = 0
  while norecogn < MAX_RETRY:

    print "  [search mode]"
    result = get_input()

    if result == None:
      deal_with_no_recognition(norecogn)
    else:
      #(should be written)
      #( 検索：Drawnerを呼ぶ )
      return MODE_HOME

  #end while


#( mode_play : unit -> mode )
def mode_play():

  print "  [play mode]"
  #(should be written)
  #( 再生：Drawnerを呼ぶ )
  return MODE_SEARCH


def mode_review():

  norecogn = 0
  while norecogn < MAX_RETRY:
    print "  [review mode]"
    result = get_input()

    if result == None:
      deal_with_no_recognition(norecogn)
    else:
      #(should be written)
      #( 評価処理：ReviewSenderを呼ぶ )
      return MODE_HOME


#( mode_home : unit -> mode )
def mode_home():

  norecogn = 0
  while True:
    print "  [command mode]"
    result = get_input()

  if result == None:
    print ("!---No word recognized.")
  else:
    words_dict = comprehender.comprehend(result)
    print (" ".join(words_dict['all']).encode("utf-8"))

    #( 超絶単純な判定によるコマンド認識 )
    if u"終了" in words_dict['all']:
      return MODE_QUIT
    elif u"検索" in words_dict['all']:
      return MODE_SEARCH
    elif u"再生" in words_dict['all']:
      return MODE_PLAY
    elif u"評価" in words_dict['all']:
      return MODE_REVIEW
    else:
      print "!---No command recognized."
      return MODE_HOME


def main():
  #---- 初期化 ----
  # mode = MODE_LOCKED
  mode = MODE_HOME

  while mode != MODE_QUIT:

    if mode == MODE_LOCKED:
      mode = mode_locked()
    elif mode == MODE_UNLOCK:
      mode = mode_unlock()
    elif mode == MODE_HOME:
      mode = mode_home()
    elif mode == MODE_SEARCH:
      mode = mode_search()
    elif mode == MODE_PLAY:
      mode = mode_play()
    elif mode == MODE_REVIEW:
      mode = mode_review()
    else:
      print "!---[BUG] This cannot happen."
      mode = MODE_HOME

  #end while

  print "  [quit]"
  return

#---- execute ----
if __name__ == "__main__":
  main()
