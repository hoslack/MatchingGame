#! usr/bin/env/ python
import random
from graphics import *
import pygame

mydict = {"State1": ["city1", "city2", "city3"], "State2": ["city4", "city5", "city6"]}


def round3():
    ranstate = random.choice(mydict.keys())

    cities = mydict[ranstate]

    rancity1 = cities[0]
    rancity2 = cities[1]
    rancity3 = cities[2]

    state = input(" {} {} {} : ".format(rancity1, rancity2, rancity3))

    if rancity1 in mydict[state]:
        print "Found"
        print state
        print "Congratulations, you beat the game"
    else:
        print "You failed, going back to level 1"
        round1()


def round2():

    ranstate = random.choice(mydict.keys())

    cities = random.sample(mydict[ranstate], 2)

    rancity1, rancity2 = cities

    state = input(" {} {} : ".format(rancity1, rancity2))

    if rancity1 in mydict[state]:
        print "Found"
        print state
        print "Proceeding to level 3"
        round3()
    else:
        print "You failed, take another shot"
        ranstate = random.choice(mydict.keys())

        cities = random.sample(mydict[ranstate], 2)

        rancity1, rancity2 = cities

        state = input(" {} {} : ".format(rancity1, rancity2))

        if rancity1 in mydict[state]:
            print "Found"
            print state
            print "Proceeding to level 3"
            round3()

        else:
            print "You failed, starting over at level 2"
            round2()


def round1():
    mylist = []

    for n in mydict:
        mylist.extend(mydict[n])

    rancity = random.choice(mylist)

    state = input(" {} : ".format(rancity))

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

round1()
