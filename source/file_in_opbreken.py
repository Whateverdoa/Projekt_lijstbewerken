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

print(shutil.disk_usage(file_tmp))

# csv_files_in_tmp = [x for x in os.listdir(path) if x.endswith(".csv")]
# sorted_files = sorted(csv_files_in_tmp)
# combinatie_binnen_mes = []
# print(combinatie_binnen_mes)
# print(combinaties)
#
# begin = 0
# eind = mes
#
# for combinatie in range(combinaties):
#     combinatie_binnen_mes.append(sorted_files[begin:eind])
#     begin += mes
#     eind += mes


tmp_rollen_lijst = [rol.name for rol in file_tmp.glob("*.csv") if rol.is_file()]


# print(combinatie_binnen_mes)
# print(combinaties)
print(tmp_rollen_lijst[0:5])

def lijst_opbreker(lijst_in,mes):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(tmp_rollen_lijst[start:end])
        start += mes
        end += mes
    return combinatie_binnen_mes

print(lijst_opbreker(tmp_rollen_lijst,5))





# hier komt een stukje num verz om de hoek kijken

