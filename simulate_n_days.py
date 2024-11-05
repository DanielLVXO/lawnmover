import lawnmover_io as io
import lawnmover_map as map
from lawnmover_plot import *
import lawnmover

import os

def main():
    file = io.get_file_name() #Fil som vi vill köra
    lawn, lawn_area, obsticle_area  = map.load_map("maps/"+file) #ladda fil
    area = lawn_area + obsticle_area
    
    try:
        days = int(input("hur många dagar vill du simuelera?: "))
    except ValueError:
        print("Felaktigt val, simulering blir 10 dagar")
        days = 10

    plot_load_map(lawn, file, lawn_area, area )   #visa plot för laddad fil.

    if os.path.isfile('saved_maps/saved_'+file): #läs in sparad_fil
        saved_map = map.load_saved_map('saved_maps/saved_'+file)
    else: #generera om fil försvunnit
        saved_map = map.expand_map(map.load_map("maps/"+file, True))

    for _ in range(days): #simulera n dagar
        saved_map = map.simulate_grass_grow(saved_map) #simulering att gräs växt
        trace_x, trace_y = lawnmover.simulate(lawn) #kör gräsklippare
        saved_map = map.cut_saved_map(trace_x, trace_y, saved_map) #simulera klippning
    
    file = str(days)+"_"+file
    io.save_file(saved_map, file) #spara fil
    plot_saved_map(saved_map, f"Simulering {days} dagar")
    
main()