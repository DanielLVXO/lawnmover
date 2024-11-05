import lawnmover_map as map
import math
import random

ROBOT_SPEED = 0.3
DELTA_T = 0.1
SIMULATED_TIME = 7200 #2h i sekunder

def random_bouncing():
    angle = random.uniform(0, math.pi*2) #vinkel
    vx = ROBOT_SPEED*math.cos(angle) #sätt hastighet i x-led
    vy = ROBOT_SPEED*math.sin(angle) #sätt hastighet i y-led
    return vx, vy

def one_step(x, y, vx, vy):
    #eftersom vi använder em utökad karta, anpassar vi farten till denna.
    return (x + (vx * DELTA_T)), (y + (vy * DELTA_T)) #öka ett steg

def is_outside(x, y, lawn: list):
    map = lawn.copy()
    map.reverse() #fixa origo
    height = len(map) 
    width = len(map[0])
  
    #utanför tomten
    if (x > width or x < 0) or (y > height or y < 0):
        return True

    #på hinder
    if map[int(y)][int(x)] == 0:
        return True
    return False

def simulate(lawn: list):
    #expanded_map = map.expand_map(lawn)

    x, y = map.get_start_position(lawn) #startpositon
    vx, vy = random_bouncing() #sätt hastighet
    trace_x = [x] #lista med start-värde
    trace_y = [y] #lista med start-värde
  
    while len(trace_y) < SIMULATED_TIME * (1/DELTA_T):
        #kolla om gräsklippare hamnar utanför kartan eller på hinder om man tar ett steg
        if is_outside(x + vx * DELTA_T, y + vy * DELTA_T, lawn):
            vx, vy = random_bouncing()

        else:
            x, y = one_step(x, y, vx, vy) # ta steg
            trace_x.append(x)
            trace_y.append(y)

    return trace_x, trace_y







