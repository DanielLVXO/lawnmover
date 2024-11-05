import lawnmover_map as map

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_load_map(map: list, filename, lawn_area, area):
    load_map = map.copy() #skapa kopia för att inte påverka senare kod
    rows = len(load_map)
    cols = len(load_map[0]) 

    load_map.reverse()
    plt.figure()
    col_map = ListedColormap(["black", "yellow", "green"])
    plt.pcolormesh(load_map, edgecolors="k", linewidth=2, cmap=col_map)
    plt.title(f"Map loaded: {filename}")
    plt.xticks(range(0, cols + 1, 1))
    plt.yticks(range(0, rows + 1, 1))
    plt.figtext(0.5, 0.01, f"Total area: {area} m2, Lawn-area: {lawn_area} m2, lawn-percentage {(lawn_area / area)*100:.0f}%", ha="center")
    plt.show()

def plot_coverage_map(trace_x: list, trace_y: list, lawn: list):
    expanded_map = map.expand_map(lawn)
    trace_x_expanded = [map.EXPAND_RATIO * x for x in trace_x]
    trace_y_expanded = [map.EXPAND_RATIO * y for y in trace_y]
    coverage_map = map.load_covarage_map(trace_x_expanded , trace_y_expanded, expanded_map)
    coverage_map.reverse()
    
    plt.figure()
    col_map = ListedColormap(['black', '#FFFDD0', 'red']) #svart, creme, rött
    plt.pcolormesh(coverage_map,cmap=col_map)
    visited, unvisited = map.calc_coverege(coverage_map)
    plt.title(f"{visited} out of {(visited + unvisited)} ==> {(visited / (visited + unvisited))*100:.1f} %")
    plt.axis("off")
    plt.show()

def plot_saved_map(saved_map: list, fig_message=""):
    plt.figure()
    saved_map.reverse()

    col_map = ListedColormap([
    "#000000", # Svart
    "#b2fab4",  # Ljusgrön
    "#9ae29c",
    "#82cb84",
    "#6ab36c",
    "#529c54",
    "#3a843c",
    "#326e34",
    "#29582b",
    "#214123",
    "#183b1a", #mörkgrön    
    ])
    col_map.set_over("#183b1a")
    plt.pcolormesh(saved_map,cmap=col_map)
    visited, unvisited = map.calc_coverege(saved_map, saved_map=True)
    plt.title(f"{visited} out of {(visited + unvisited)} ==> {(visited / (visited + unvisited))*100:.1f} %")
    plt.axis("off")
    if fig_message != "":
         plt.figtext(0.5, 0.01, fig_message, ha="center")
    plt.show()

def plot_tracemaps(trace_x: list, trace_y: list, lawn: list):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5)) #större

    end_index = int(len(trace_x)/8) #15 min om 2h simulering
    ax1.plot(trace_x[0:end_index], trace_y[0:end_index])
    ax1.set_title("15 min simulering")
    ax1.set_ylim(0,len(lawn))
    ax1.set_xlim(0,len(lawn[0]))

    end_index = int(len(trace_x)/2) #1h om 2h simulering
    ax2.plot(trace_x[0:end_index], trace_y[0:end_index])
    ax2.set_title("En timmes simulering")
    ax2.set_ylim(0,len(lawn))
    ax2.set_xlim(0,len(lawn[0]))

    ax3.plot(trace_x,trace_y) #hel simulering
    ax3.set_title("Två timmars simulering")
    ax3.set_ylim(0,len(lawn))
    ax3.set_xlim(0,len(lawn[0]))

    plt.show()  