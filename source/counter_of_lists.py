
import pandas as pd
import pathlib
import os

path = os.getcwd
myfile = r"\bestanden\201922020_lijst.csv"
print(path)

pad = os.path.join('C:\\Users\\mike\\PycharmProjects\\Projekt_lijstbewerken\\' + myfile)
print(pad)




df1= pd.read_csv(pad, ";")

totaal = df1.aantal.sum()

rollen = totaal//6

# C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\bestanden\201922020_lijst.csv