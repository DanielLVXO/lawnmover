import lawnmover_io as io
import lawnmover_map as map
from lawnmover_plot import *
import lawnmover

import os

def main():
    file = io.get_file_name()     #Fil som vi vill köra
    lawn, lawn_area, obsticle_area  = map.load_map("maps/"+file) #ladda fil
    total_area = lawn_area + obsticle_area
   
    plot_load_map(lawn, file, lawn_area, total_area )   #visa plot för laddad fil.
   
    trace_x, trace_y = lawnmover.simulate(lawn) #simulera gräsklippare
   
    if os.path.isfile('saved_maps/saved_' + file): #läs in sparad_fil 
        saved_map = map.load_saved_map('saved_maps/saved_'+file)
    else: #generera om fil försvunnit
        saved_map = map.expand_map(map.load_map("maps/"+file, True))

    saved_map = map.simulate_grass_grow(saved_map) #simulering att gräs växt
    saved_map = map.cut_saved_map(trace_x, trace_y, saved_map) #simulera klippning
    io.save_file(saved_map, file) #spara fil
 
    plot_tracemaps(trace_x, trace_y, lawn) #skriv ut trace-map
    plot_coverage_map(trace_x, trace_y, lawn) #skriv ut covarage map
    plot_saved_map(saved_map) #skriv ut sparad karta

main()