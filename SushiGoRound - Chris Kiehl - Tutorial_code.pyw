import ImageGrab, Image, ImageOps
import os
import time
import win32api, win32con
from numpy import *

"""
Assumptions:
-----------------

down key 4 times to center play area on screen.

Play Area = (157,346,796,825)
x_pad = 156
y_pad = 345

"""


#Globals
#----------------------------

x_pad = 156
y_pad = 345




sushiTypes = {2670:'onigiri', 
              3143:'caliroll',
              2677:'gunkan',}



class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598 
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041
    


             











#End Globals
#-------------------------------------



def screenGrab():
    b1 = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    box = (x_pad+1,y_pad+1, x_pad+640, y_pad + 479)
    b2 = (0,0,600,480)
    im = ImageGrab.grab()
##    im.thumbnail((600,600), Image.ANTIALIAS)
    im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    return im



def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a
    ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
##    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##    print "Click."
##    time.sleep(.01)


def middleClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,120)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,120)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0)
    print "Click."
    time.sleep(.01)

def mClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE,0,0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE,800,400)
    print "Click."
    time.sleep(.01)

def mousePos(cord=(0,0)):
    win32api.SetCursorPos(cord)


def get_cords():
    x,y = win32api.GetCursorPos()
##    x = x - x_pad
##    y = y - y_pad
    print x, y

def startGame():
    mousePos((182, 225))
    leftClick()
    time.sleep(.1)
    mousePos((193, 410))
    leftClick()
    time.sleep(.1)
    mousePos((435, 470))
    leftClick()
    time.sleep(.1)
    mousePos((167, 403))
    leftClick()
    time.sleep(.1)
    


    


"""
Food cords:

shrimp = 54,700
rice = 119, 701
nori = 63, 745
roe = 111, 749
salmon = 54, 815
unagi = 111, 812



Plate cords:

    108, 573
    212, 574
    311, 573
    412, 574
    516, 575
    618, 573

Phone system:









"""


def clear_tables():
    mousePos((108, 573))
    leftClick()

    mousePos((212, 574))
    leftClick()

    mousePos((311, 573))
    leftClick()

    mousePos((412, 574))
    leftClick()

    mousePos((516, 575))
    leftClick()

    mousePos((618, 573))
    leftClick()
    time.sleep(1)


class Cord:

    f_shrimp = (54,700)
    f_rice = (119, 701)
    f_nori = (63, 745)
    f_roe = (111, 749)
    f_salmon = (54, 815)
    f_unagi = (111, 812)
    

    
    phone = (601, 730)

    menu_toppings = (567, 638)
    
    t_shrimp = (509, 581)
    t_nori = (507, 645)
    t_roe = (592, 644)
    t_salmon = (510, 699)
    t_unagi = (597, 585)
    t_exit = (614, 702)

    menu_rice = (551, 662)
    buy_rice = (564, 647)
    
    delivery_norm = (510, 664)
    
    
def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 1  
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
	
    elif food == 'onigiri':
        print 'Making a onigiri'
        foodOnHand['rice'] -= 2  
        foodOnHand['nori'] -= 1  
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
        
        time.sleep(1.5)


    elif food == 'gunkan':
        foodOnHand['rice'] -= 1  
        foodOnHand['nori'] -= 1  
        foodOnHand['roe'] -= 2   
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)




def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)


                

def buyFood(food):
    
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print 'rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            

            
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print 'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
	



    mousePos(Cord.phone)
    
    mousePos(Cord.menu_toppings)
    
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
    
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)
    
    mousePos(Cord.delivery_norm)

        





def foldMat():
    mousePos((Cord.f_rice[0]+35,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)



foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5} 




def get_seat_one():
    box = (45,427,45+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_two():
    box = (146,427,146+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_three():
    box = (247,427,247+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_four():
    box = (348,427,348+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_five():
    box = (449,427,449+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_six():
    box = (550,427,550+63,427+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
##    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
    


def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()
    
def check_bubs():

    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is ocupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1

    else:
        print 'Table 1 unoccupied'


    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is ocupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2

    else:
        print 'Table 2 unoccupied'




    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is ocupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3

    else:
        print 'Table 3 unoccupied'









    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is ocupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4

    else:
        print 'Table 4 unoccupied'




    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is ocupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5

    else:
        print 'Table 5 unoccupied'









    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 1 is ocupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6

    else:
        print 'Table 6 unoccupied'


    clear_tables()
        

    
def main():
    pass
    
    


if __name__ == '__main__':
    main()






