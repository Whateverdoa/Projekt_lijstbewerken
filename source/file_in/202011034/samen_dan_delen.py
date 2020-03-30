import pandas as pd
from pathlib import Path
import source.paden_naar_files as pad


map=sorted(Path(r'C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_in\202011034').glob('*.csv'))
maplijst=[]
for file in map:

    maplijst.append(pd.read_csv(file))

samen = pd.concat(maplijst, axis=0)
samencsv = pd.concat(maplijst, axis=0).to_csv("output\huismerk_samen.csv", index=0)

lengte_dataframe= len(samen)


def samenvoegen_map_csvs(padnaarcsv):
    pass


# 3 files van maken

def breek_naar_csv(csv_file_in, aantalperrol, aantalrollen, dataframe):
    """# dit is een functie waard maak een dataframe
    van lijst en maak dan x aantal csv files"""

    begin = 0
    eind = aantalperrol

    for i in range(1, aantalrollen + 1):
        rol = f'{pad.file_out_test}/file_{i:>{0}{4}}.csv'
        dataframe.iloc[begin:eind].to_csv(rol, index=0)
        begin += aantalperrol
        eind += aantalperrol

breek_naar_csv(r"source\file_in\202011034\output\huismerk_samen.csv",1500000,3,samen)