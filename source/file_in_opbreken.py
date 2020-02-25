import pandas as pd
from pathlib import Path


#todo add gui
#todo add functions and paths module


file = "file_in/QR_600X50.csv"

wdir = Path.cwd()
file_in = wdir/file
print(wdir)
print(file_in.is_file())
file_tmp = wdir/"file_out/tmp"
print(file_tmp.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

aantal_per_rol = 50

df = pd.read_csv(file_in, ";")
aantal = len(df)
print(f'de file bestaat uit {aantal} rows')
aantal_rollen = aantal//aantal_per_rol
print(f'aantal rollen = {aantal_rollen}')
baan = len(df)//1000
# print(f'baan = {baan} || wikkel ={rolwikkel}')
mes=5
combinaties = aantal_rollen // mes


begin = 0
eind = 50


# dit is een functie waard maak een dataframe van lijst en maak dan x aantal csv files

for i in range(1, aantal_rollen+1):
    rol = f'{file_tmp}/rol_{i:>{0}{4}}.csv'
    df.iloc[begin:eind].to_csv(rol, index=0)
    begin += aantal_per_rol
    eind += aantal_per_rol




tmp_rollen_lijst = [rol.name for rol in file_tmp.glob("*.csv") if rol.is_file()]
tmp_rollen_posix_lijst= [rol for rol in file_tmp.glob("*.csv") if rol.is_file()]


# print(combinatie_binnen_mes)
# print(combinaties)
print(tmp_rollen_lijst[0:5])

def lijst_opbreker(lijst_in,mes):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes
        end += mes
    return combinatie_binnen_mes

# print(lijst_opbreker(tmp_rollen_lijst,5))
# print(lijst_opbreker(tmp_rollen_posix_lijst,5))

# for lijst in lijst_opbreker(tmp_rollen_posix_lijst,5):
#     print(f'dit is een lijst van 5 : {lijst}')

def kol_naam_lijst_builder(mes=1):
    kollomnaamlijst=[]

    for count in range(1,mes+1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        # kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)


    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst

def lees_per_lijst(lijst_met_posix_paden):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count=1
    concatlist=[]
    for posix_pad_naar_file in lijst_met_posix_paden:
        print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count+=1
    kolomnamen=kol_naam_lijst_builder(5)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]


    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1

lees_per_lijst(lijst_opbreker(tmp_rollen_posix_lijst,5)[0])

rollen_voor_het_stapelen = [lees_per_lijst(lijst_opbreker(tmp_rollen_posix_lijst,5)[i]
                             for i in range(aantal_rollen)]



# hier komt een stukje num verz om de hoek kijken

