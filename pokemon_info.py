import tkinter as tk
import requests
from tkinter import ttk, messagebox
import math

window = tk.Tk()
window.title('Pokemon Information')
pokemon_name = None
frame1 = tk.Frame(window)
entry = tk.Entry(master=frame1)
label_frame = tk.LabelFrame(window, text='Info')
frame2 = tk.Frame(label_frame, highlightbackground="gray")
info_label1 = tk.Label(master=frame2, text="Height: ")
info_label11 = tk.Label(master=frame2, text="")
info_label2 = tk.Label(master=frame2, text="Weight: ")
info_label22 = tk.Label(master=frame2, text="")
info_label22 = tk.Label(master=frame2, text="")
info_label3 = tk.Label(master=frame2, text="Type: ")
info_label33 = tk.Label(master=frame2, text="")
label_frame2 = tk.LabelFrame(window, text='Stats')
frame3 = tk.Frame(label_frame2, highlightbackground="gray")
stats_label1 = ttk.Label(master=frame3, text="HP: ")
hp_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
stats_label2 = tk.Label(master=frame3, text="Attack: ")
attack_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
stats_label3 = tk.Label(master=frame3, text="Defense: ")
defense_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
stats_label4 = tk.Label(master=frame3, text="Special Attack: ")
spl_att_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
stats_label5 = tk.Label(master=frame3, text="Special Defence: ")
spl_def_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
stats_label6 = tk.Label(master=frame3, text="Speed: ")
speed_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)

def main():
    #frame1 = tk.Frame(window)
    frame1.pack(padx=10, pady=10)
    lbl_value = tk.Label(master=frame1, text="Pokemon Name:")
    lbl_value.grid(row=0, column=0, padx=10)
    #entry = tk.Entry(master=frame1)
    entry.grid(row=0, column=1, padx=10)
    btn_increase = tk.Button(master=frame1, text="Get Info", command=get_info)
    btn_increase.grid(row=0, column=2, padx=10)

    
    #label_frame = tk.LabelFrame(window, text='Info')
    label_frame.pack(side=tk.LEFT, padx=10, pady=10, anchor="n")
    #frame2 = tk.Frame(label_frame, highlightbackground="gray")
    frame2.pack(padx=10, pady=10)
    #info_label1 = tk.Label(master=frame2, text="Height: ")
    info_label1.grid(row=0, column=0, sticky="e")
    #info_label11 = tk.Label(master=frame2, text="")
    info_label11.grid(row=0, column=1, sticky="w")
    #info_label2 = tk.Label(master=frame2, text="Weight: ")
    info_label2.grid(row=1, column=0, sticky="e")
    #info_label22 = tk.Label(master=frame2, text="")
    info_label22.grid(row=1, column=1, sticky="w")
    #info_label3 = tk.Label(master=frame2, text="Type: ")
    info_label3.grid(row=2, column=0, sticky="e")
    #info_label33 = tk.Label(master=frame2, text="")
    info_label33.grid(row=2, column=1, sticky="w")

    
    #label_frame2 = tk.LabelFrame(window, text='Stats')
    label_frame2.pack(side=tk.RIGHT, pady=10, anchor="n")
    #frame3 = tk.Frame(label_frame2, highlightbackground="gray")
    frame3.pack(padx=10, pady=10)
    #stats_label1 = ttk.Label(master=frame3, text="HP: ")
    stats_label1.grid(row=2, column=1, sticky="e")
    #hp_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
    hp_pb.grid(row=2, column=2, columnspan=2, padx=1, pady=1)
    #stats_label2 = tk.Label(master=frame3, text="Attack: ")
    stats_label2.grid(row=3, column=1, sticky="e")
    #attack_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
    attack_pb.grid(row=3, column=2, columnspan=2, padx=1, pady=1)
    #stats_label3 = tk.Label(master=frame3, text="Defense: ")
    stats_label3.grid(row=4, column=1, sticky="e")
    #defense_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
    defense_pb.grid(row=4, column=2, columnspan=2, padx=1, pady=1)
    #stats_label4 = tk.Label(master=frame3, text="Special Attack: ")
    stats_label4.grid(row=5, column=1, sticky="e")
    #spl_att_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
    spl_att_pb.grid(row=5, column=2, columnspan=2, padx=1, pady=1)
    #stats_label5 = tk.Label(master=frame3, text="Special Defence: ")
    stats_label5.grid(row=6, column=1, sticky="e")
    #spl_def_pb = ttk.Progressbar(frame3, orient='horizontal', mode='determinate', length=100)
    spl_def_pb.grid(row=6, column=2, columnspan=2, padx=1, pady=1)
    #stats_label6 = tk.Label(master=frame3, text="Speed: ")
    stats_label6.grid(row=7, column=1, sticky="e")
    #speed_pb = ttk.Progressbar(frame3, orient='horizontal', value="40", mode='determinate', length=100)
    speed_pb.grid(row=7, column=2, columnspan=2, padx=1, pady=1)

    """
    info_label11.config(text = pokemon_data["height"])
    info_label22.config(text = pokemon_data["weight"])
    info_label33.config(text = ", ".join(type_list_from_types(pokemon_data["types"])))
    #print(type_list_from_types(pokemon_data["types"]))
    """
    window.mainloop()


def get_info():
    pokemon_name = entry.get()
    pokemon_info = fetch_pokemon_details(pokemon_name)
    
    if pokemon_info:
        info_label11.config(text=pokemon_info.get("height", ""))
        info_label22.config(text=pokemon_info.get("weight", ""))
        info_label33.config(text=", ".join(type_list_from_types(pokemon_info.get("types", []))))
        
        stats = pokemon_info.get("stats", [])
        for i, stat in enumerate(stats):
            pb = [hp_pb, attack_pb, defense_pb, spl_att_pb, spl_def_pb, speed_pb][i]
            pb["value"] = math.floor(stat.get("base_stat", 0) * 100 / 260)
        
        return True
    else:
        messagebox.showinfo(message=f'Unable to fetch information for {pokemon_name} from PokeAPI.', icon="error", title="Error")
        return False


def fetch_pokemon_details(name):
    try:
        url = "https://pokeapi.co/api/v2/pokemon/"+name
        pokemon_data = requests.get(url).json()
        return pokemon_data
    except Exception as e:
        return False
    return False


def type_list_from_types(types):
    return [type["type"]["name"].capitalize() for type in types]

if __name__ == '__main__':
   main()