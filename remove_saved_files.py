import os

def main():
    choice = input("Ta bort sparade filer? (j/n):")
    

    if choice.upper() == "J":  
        folder = "saved_maps/"
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)

            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                except Exception as exception:
                    print(f"Problem att ta bort {file_path}, felmeddelande: {exception}", )
    
    print("Klart")
                


main()

