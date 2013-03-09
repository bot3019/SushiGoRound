# -*- coding: utf-8 -*-
#import ImageGrab
import pyscreenshot as ImageGrab
import os
import time
import xaut
import ImageOps
from numpy import *

# Screen coordinates
""" 
All coordinates assume a
    screen resolution of 0x0
    Chrome windows half screen sized
    Bookmarks Toolbar disabled.

    Screen 1
    + -
    - -

me:
first day - 1120
            2480
            4370

7SINS: press key_down 7 times
    x_pad   = 30
    y_pad   = 102
PANDEMIC:
    x_pad   = 34
    y_pad   = 397
PANDEMIC:
    x_pad   = 31
    y_pad   = 377
    openbox - decorate - opera half screen
PANDEMIC:
    x_pad   = 31
    y_pad   = 401
    openbox - decorate - opera half screen
# ---------------"""
x_pad   = 34
y_pad   = 397
box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
maked   = 0

# Sushi mechanics
# ------------------
sushi = dict(
    colorcode = {
        2103:           'onigiri', 
        2747:           'caliroll',
        2110:           'gunkan',
        2078:           'salmonroll',
        2525:           'shrimpsushi',
        2326:           'unagiroll',
        2880:           'dragonroll',
        4016:           'combosushi'},
    name = {
        'onigiri':      'Onigiri',
        'caliroll':     'California Roll',
        'gunkan':       'Gunkan Maki',
        'salmonroll':   'Salmon Roll',
        'shrimpsushi':  'Shrimp Sushi',
        'unagiroll':    'Unagi Roll',
        'dragonroll':   'Dragon Roll',
        'combosushi':   'Combo Sushi'},
    recipe = {
        'onigiri':      dict(shrimp=0,  rice=2, nori=1, roe=0,  salmon=0,   unagi=0),
        'caliroll':     dict(shrimp=0,  rice=1, nori=1, roe=1,  salmon=0,   unagi=0), 
        'gunkan':       dict(shrimp=0,  rice=1, nori=1, roe=2,  salmon=0,   unagi=0), 
        'salmonroll':   dict(shrimp=0,  rice=1, nori=1, roe=0,  salmon=2,   unagi=0), 
        'shrimpsushi':  dict(shrimp=2,  rice=1, nori=1, roe=0,  salmon=0,   unagi=0),
        'unagiroll':    dict(shrimp=0,  rice=1, nori=1, roe=0,  salmon=0,   unagi=2),  
        'dragonroll':   dict(shrimp=0,  rice=2, nori=1, roe=1,  salmon=0,   unagi=2),  
        'combosushi':   dict(shrimp=1,  rice=2, nori=1, roe=1,  salmon=1,   unagi=1)}
    )

# Ingredient mechanics
# ------------------
foodOnHand =            dict(shrimp=5,  rice=10,nori=10,roe=10, salmon=5,   unagi=5)

class cord:
    tel         = (564, 345)
    deliveryn   = (484, 293)
    t_topping   = (541, 273)
    t_rice      = (549, 292)
    t_exit      = (582, 336)

cordbuy = dict(
    shrimp      =(497, 222),
    rice        =(534, 279),
    nori        =(500, 277),
    roe         =(568, 271),
    salmon      =(488, 335),
    unagi       =(572, 221))

cordput = dict(
    shrimp      =(30, 330),
    rice        =(80, 330),
    nori        =(30, 380),
    roe         =(80, 380),
    salmon      =(30, 440),
    unagi       =(80, 440))

clrnota = dict(
    shrimp      =(127, 102, 90),
    rice        =(127, 127, 127),
    nori        =(33,  30,  11),
    roe         =(127, 61,  0),
    salmon      =(127, 71,  47),
    unagi       =(103, 64,  12))

seat    = (0, 7846, 6551, 11567, 11190, 8456, 8187)
seatb   = (0, 28, 129, 230, 331, 432, 533)

def screenGrab():
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.bmp', 'BMP')
    return im

# Get Seat
# ------------------
def gs(seat):
    box = (x_pad+1 + seatb[seat], y_pad+1 + 57, x_pad+1+seatb[seat] + 57, y_pad+1+57 + 20)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

# Mouse Helpers
# ------------------
m = xaut.mouse()

def mv(xy):
    m.move(x_pad+xy[0],y_pad+xy[1])

def gc():
    print m.x()-x_pad,m.y()-y_pad

def lc():
    m.click(1)
    #print "Click@",m.x()-x_pad,m.y()-y_pad

def mlt(xy,s=0.05):
    mv(xy)
    lc()
    if s > 0.9:
        clr()
    else:
        time.sleep(s)

# 
# ------------------
def make(f):
    global maked

    print 'Making a {}'.format(sushi['name'][f])
    if not [k for k in foodOnHand if foodOnHand[k] < sushi['recipe'][f][k]]:
        for k in foodOnHand:
            foodOnHand[k] -= sushi['recipe'][f][k]
        for i, j in sushi['recipe'][f].items():
            while j != 0:
                mlt(cordput[i])
                j -= 1
        mlt((150,330),1)    # fold
    else:
        print "!!!UNABLE"

# 
# ------------------  
def clr():
    mlt((84, 210),0)
    mlt((184, 210),0)
    mlt((287, 210),0)
    mlt((384, 210),0)
    mlt((483, 210),0)
    mlt((591, 210),.1)
    print 'Clear tables'

# Check food
# ------------------  
def check():
    print foodOnHand.items()
    print 'check for cheap food'
    for i, j in foodOnHand.items():
        if i == 'rice' or i == 'nori' or i == 'roe':
            if j <= 3:
                print '{} is low and needs to be replenished'.format(i)
                buy(i)

    if maked > 5:
        print 'check for rich food'
        for i, j in foodOnHand.items():
            if i == 'shrimp' or i == 'salmon' or i == 'unagi':
                if j <= 2:
                    print '{} is low and needs to be replenished'.format(i)
                    buy(i)

# buy food
# ------------------  
def buy(f):
    mlt(cord.tel)
    if f != 'rice':
        mlt(cord.t_topping,.9)
    else:
        mlt(cord.t_rice,.9)
    s = ImageGrab.grab(box)
    if s.getpixel(cordbuy[f]) != clrnota[f]:
            print '{} is available (buy)'.format(f)
            mlt(cordbuy[f],.1)
            mlt(cord.deliveryn,2)
            if f == 'rice' or f == 'nori' or f == 'roe':
                foodOnHand[f] += 10
            else:
                foodOnHand[f] += 5
    else:
        print '{} is NOT available (discard)'.format(f)
        mlt(cord.t_exit,1)

# Check Orders
# ------------------  
def order(i):
    check()
    s = gs(i)
    if s != seat[i]:
        if sushi['colorcode'].has_key(s):
            print 'table {} is occupied and needs {}'.format(i, sushi['colorcode'][s])
            make(sushi['colorcode'][s])
        else:
            print 'sushi not found!\n sushi colorcode = {}'.format(s)
    else:
        print 'Table {} unoccupied'.format(i)

# Check Orders
# ------------------  
def orders():
    clr()
    order(1)
    order(2)
    order(3)

    clr()    
    order(4)
    order(5)
    order(6)

# Game init
# ------------------
def init():
    foodOnHand = dict(shrimp=5,rice=10,nori=10,roe=10,salmon=5,unagi=5)

    global maked
    maked = 0
    print 'Variables initiated'

# 
# ------------------
def nextround():
    for i in range(1, 18):
        print "We're on iteration {}".format(i)
        orders()

# Start game again
# ------------------
def sga():
    init()
    mlt((300,370),.1)
    mlt((320,430),.1)
    mlt((190,380),.1)
    mlt((310,370),.1)
    nextround()

# Start game
# ------------------
def sg():
    mlt((300,200),.1)
    mlt((300,400),.1)
    mlt((300,400),.1)
    mlt((570,440),.1)
    mlt((330,380),.1)
    print 'Game started first time'

    for day in range(1, 9):
        print "We're on day {}".format(day)
        sga()

# 
# ------------------
if __name__ == '__main__':
    m.move_delay(100)
    m.down_delay(100)
