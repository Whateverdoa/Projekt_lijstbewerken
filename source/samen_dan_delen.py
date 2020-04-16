import pandas as pd
from pathlib import Path
import source.paden_naar_files as pad

#todo schrijf een paden module

map = sorted(
    Path(r'C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_in').glob('*.csv'))
map2 = Path(pad.file_out).glob("*.csv")

file_out_name = "202013134_tot.csv"

for file in map:
    print(file)



maplijst = []
for file in map:
    maplijst.append(pd.read_csv(file))

samen = pd.concat(maplijst, axis=0)
pad_file_uit = pad.file_out / file_out_name
# padd = Path(
#     r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_in\202011035\output\Remark_samen.csv")
samencsv = pd.concat(maplijst, axis=0).to_csv(pad_file_uit, index=0)

lengte_dataframe = len(samen)
print(lengte_dataframe)


a = lengte_dataframe % 5
print(a)








def samenvoegen_map_csvs(padnaarcsv):
    pass


# 3 files van maken

def breek_naar_csv(csv_file_in, aantalperrol, aantalrollen, dataframe, naar_posix_pad):
    """# dit is een functie waard maak een dataframe
    van lijst en maak dan x aantal csv files"""

    begin = 0
    eind = aantalperrol

    for i in range(1, aantalrollen + 1):
        rol = f'{naar_posix_pad}/file_{i:>{0}{4}}.csv'
        dataframe.iloc[begin:eind].to_csv(rol, index=0)
        begin += aantalperrol
        eind += aantalperrol


breek_naar_csv(pad_file_uit/file_out_name, 300000, 5, samen, pad.file_out)

map = sorted(
    Path(pad.file_out).glob('*.csv'))
maplijst = []
for file in map:
    print(len(pd.read_csv(file)))
