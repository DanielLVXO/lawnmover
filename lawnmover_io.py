import os
import lawnmover_map as map

def get_file_name() -> str:
    print("Ladda karta:")
    #ladda filer från mappen maps/
    map_files = [file for file in os.listdir("maps") if file.endswith(".csv")]
    print("Välj fil:")
    i = 1
    for map in map_files: #skriv ut filer
        print(f"{i}. {map[:-4]}")
        i += 1
    
    while True: #ta in data från användare
        try:
            choice = int(input("Ditt val:"))
            if choice >= 1 and choice <= len(map_files):
                if not os.path.isfile('saved_maps/saved_'+ map_files[choice-1]): #sparad fil saknas
                    create_save_file(map_files[choice-1]) #skapa sparad fil
                return map_files[choice-1]
            else:
                raise ValueError
        except ValueError:
            print("Ogiltligt val")
    

def create_save_file(file):
    #skapa fil med långt gräs
    save_map = map.expand_map(map.load_map("maps/"+file, True))
    save_file(save_map, file)


def save_file(saved_map: list, file):
    #skapa fil som skriver över gammal
    folder_name = "saved_maps"
    os.makedirs(folder_name, exist_ok=True) #skapa mapp om den inte finns
    with open(folder_name+"/saved_"+file,"w",encoding="UTF-8") as f:
        for row in saved_map:
            f.write(",".join([str(cell) for cell in row])+"\n") 
