EXPAND_RATIO = 5

def load_map(file, long_grass = False):
    # long_grass innebär att vi sätter gräslängd till 9, 
    # som används när vi gör analys över tid i sparade filer
    map = []
    grass_area = 0
    obsticle_area = 0
    with open(file, "r", encoding="utf-8") as f:
        for row in f:
            values = row.strip().split(",")
            row_lst = []
            for value in values:
                match value:
                    case "O":#hinder
                        row_lst.append(0)
                        obsticle_area += 1
                    case "S": #start
                        if long_grass:
                            row_lst.append(9)
                        else:
                            row_lst.append(1)
                        grass_area += 1
                    case "L": #gräs
                        if long_grass:
                            row_lst.append(9)
                        else:
                            row_lst.append(2)
                        grass_area += 1
            map.append(row_lst)
    if long_grass:
        return map
    else:
        return map, grass_area, obsticle_area

def load_saved_map(file):
    #ladda intern sparad fil
    saved_map = []
    with open(file, "r", encoding="utf-8") as f:
        for row in f:
            values = row.strip().split(",")
            row_lst = []
            for value in values:
                row_lst.append(int(value))
            saved_map.append(row_lst)
    return saved_map

def get_start_position(lawn: list):
    map = lawn.copy()
    map.reverse() #origo nedre vänstra hörnet
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                return x, y
    return 0, 0 #saknar startpunkt, vi startar från 0,0 

def expand_map(map: list):
    #skapa utökad karta varje ruta blir en 5x5 (beroende på EXPAND_RATIO) rutor
    expanded_map = [] #ny karta
    for row in map:
        row_expanded = [x for x in row for _ in range(EXPAND_RATIO)] # [0,1] -> [0,0,0,0,0,1,1,1,1,1]
        for _ in range(EXPAND_RATIO):
            expanded_map.append(row_expanded) # multiplicera rader
    return expanded_map

def load_covarage_map(trace_x: list, trace_y: list, map: list):
    #0 = hinder, 1 = oklippt, 2 = klippt
    coverage_map = []
    for row in map:
        row_list = []
        for cell in row:
            if cell == 0:
                row_list.append(0) #hinder
            else:
                row_list.append(1) #gräsmatta
        coverage_map.append(row_list)
    
    #lägg till klippning
    for i in range(len(trace_x)):
        x = int(trace_x[i])
        y = len(map) - 1 - int(trace_y[i])
        coverage_map[y][x] = 2
    return coverage_map

def calc_coverege(map, saved_map = False):
    uncut_cells = 0
    cut_cells = 0
    for row in map:
        for cell in row:
            if saved_map: #för sparad karta
                if cell >= 1 and cell <= 6:
                    cut_cells += 1
                elif cell >= 7:
                    uncut_cells += 1
            else: #för senaste klippning
                if cell == 1:
                    uncut_cells += 1
                elif cell == 2:
                    cut_cells += 1
    return cut_cells, uncut_cells

def simulate_grass_grow(saved_map: list):
    for y in range(len(saved_map)):
        for x in range(len(saved_map[y])):
            if saved_map[y][x] != 0:
                if saved_map[y][x] < 10: #10 är max-längd
                    saved_map[y][x] += 1 #gräs växer
    return saved_map

def cut_saved_map(trace_x: list, trace_y: list, saved_map: list):
    trace_x_expanded = [EXPAND_RATIO * x for x in trace_x]
    trace_y_expanded = [EXPAND_RATIO * y for y in trace_y]
    for i in range(len(trace_x_expanded)):
        x = int(trace_x_expanded[i])
        y = len(saved_map) - 1 - int(trace_y_expanded[i])
        saved_map[y][x] = 1 #område klippt
    return saved_map

#stor karta
def convert_coordinate(x, y, cols, rows):
    #cols används inte i denna version
    y = (rows*EXPAND_RATIO) - 1 - y*EXPAND_RATIO
    x = x * EXPAND_RATIO
    return x, y


