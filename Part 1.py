# Bruk Thomas Tewelde PSID:1834504 FINAL PROJECT PT.1


import csv
from datetime import date

dict_ManufacturerList = {
}

dict_PriceList = {
}

dict_ServiceDatesList = {
}

with open('ManufacturerList.csv', mode='r') as ML_file:
    s = 0
    for i in ML_file:
        a, b, c, d = i.rstrip('\n').split(',')
        ML_file[s] = {"item ID": a, "manufacturer name": b, "item type": c, "damaged indicator": d}
        s += 1
with open('PriceList.csv', mode='r') as PL_file:
    s = 0
    for i in PL_file:
        a, b = i.rstrip('\n').split(',')
        PL_file[s] = {"item ID": a, "item price": b}
        s += 1
with open('ServiceDatesList.csv', mode='r') as SDL_file:
    s = 0
    for i in SDL_file:
        a, b = i.rstrip('\n').split(',')
        SDL_file[s] = {"item ID": a, "Service Date": b}
        s += 1

# ----------(A)  Creating Full Inventory ------ #
g = ""
d = ""
o = 0
Full_Inventory = {}
for x in ML_file:
    for y in PL_file:
        if ML_file[x]["item ID"] == PL_file[y]["item ID"]:
            g = PL_file[y]["item Price"]
    for z in SDL_file:
        if ML_file[x]["ID"] == SDL_file[z]["ID"]:
            d = PL_file[y]["Service Date"]
    Full_Inventory[o] = {"item ID": ML_file[x]["item ID"], "manufacturer name": ML_file[x]["manufacturer name"],
                         "item type": ML_file[x]["item type"],
                         "damaged indicator": ML_file[x]["damaged indicator"], "item Price": g, "Service Date": d,
                         }
    o += 1

print(Full_Inventory)

# --------(B) Creating Item Type Inventory List---------- #

pho_counter = 0
lap_counter = 0
tower_counter = 0

Phone_inv = {}
Laptop_inv = {}
Tower_inv = {}
for x in Full_Inventory:
    if x['item type'] == 'phone':
        Phone_inv[pho_counter] = {"item ID": x["item ID"], "manufacturer name": x["manufacturer name"],
                                  "damaged indicator": x["damaged indicator"], "item Price": x['item Price'],
                                  "Service Date": x['Service Date']
                                  }

        pho_counter += 1

    elif x["item type"] == 'laptop':
        Laptop_inv[lap_counter] = {"item ID": x["item ID"], "manufacturer name": x["manufacturer name"],
                                   "damaged indicator": x["damaged indicator"], "item Price": x['item Price'],
                                   "Service Date": x['Service Date']
                                   }

        lap_counter += 1

    elif x["item type"] == 'tower':
        Tower_inv[tower_counter] = {"item ID": x["item ID"], "manufacturer name": x["manufacturer name"],
                                    "damaged indicator": x["damaged indicator"], "item Price": x['item Price'],
                                    "Service Date": x['Service Date']
                                    }

        tower_counter += 1

# --------(C) Creating Past Service Date Inventory------------- #

today = date.today().strftime('%m/%d/%Y')

psd_counter = 0
Past_S_Date = {}

for x in Full_Inventory:
    if x['Service Date'] < today:
        Past_S_Date[psd_counter] = {"item ID": x["item ID"], "manufacturer name": x["manufacturer name"],
                                    "item type": x["item type"],
                                    "damaged indicator": x["damaged indicator"], "item Price": x['item Price'],
                                    "Service Date": x['Service Date']
                                    }

        psd_counter += 1

# ----(D) Damage Indicator ---- #

dam_counter = 0
Damaged_Item = {}

for x in Full_Inventory:
    if x['damaged indicator'] == 'damaged':
        Damaged_Item[dam_counter] = {"item ID": x["item ID"], "manufacturer name": x["manufacturer name"],
                                     "item type": x["item type"],
                                     "item Price": x['item Price'], "Service Date": x['Service Date']
                                     }

    dam_counter += 1

# ---- Exporting 'A' to csv ---- #

with open("FullInventory.csv", "w") as f:
    for x in Full_Inventory:
        f.write(x)

# --- Exporting 'B' to csv---- #

with open("LaptopInventory.csv", "w") as f:
    for x in Laptop_inv:
        f.write(x)

with open("PhoneInventory.csv", "w") as f:
    for x in Phone_inv:
        f.write(x)

with open("TowerInventory.csv", "w") as f:
    for x in Tower_inv:
        f.write(x)

# --- Exporting 'C' to csv---- #

with open("PastServiceDateInventory.csv", "w") as f:
    for x in Past_S_Date:
        f.write(x)

# --- Exporting 'D' to csv---- #

with open("DamagedInventory.csv", "w") as f:
    for x in Damaged_Item:
        f.write(x)
