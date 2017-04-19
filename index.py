#! usr/bin/env/ python

import random

from graphics import *

mydict = {"State1": ["city1", "city2", "city3"], "State2": ["city4", "city5", "city6"]}


def round2():
    pass


def round3():
    pass


def round1():
    mylist = []

    for n in mydict:
        mylist.extend(mydict[n])

    rancity = random.choice(mylist)

    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(255, 255, 255))

    text = Text(Point(280, 250), rancity)
    input_box = Entry(Point(250, 250), 20)

    input_box.draw(win)
    state = input_box.getText()

    if rancity in mydict[state]:
        print "Found"
        print state
        print "Proceeding to level 2"
        round2()
    else:
        print "You failed, take another chance"
        rancity = random.choice(mylist)

        state = input(" {} : ".format(rancity))

        if rancity in mydict[state]:
            print "Found"
            print state
            print "Proceeding to level 2"
            round2()

        else:
            print "You failed, starting over at level 1"
            round1()
