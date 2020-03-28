import pandas as pd
from pathlib import Path
from source.paden_naar_files import file_in, test_file

order_nummer = "202006799"  # wordt in GUI --> filenaam.stem

print(file_in)

df = pd.read_csv(file_in, sep=";")


with open(file_in, "r") as file:
    readline = file.readlines()

with open(test_file, "w") as write_file:
    begin = 1
    eind = 50
    for i in range(len(df) // 50):

        print(begin, eind)
        write_file.writelines(readline[begin:begin + 1])
        write_file.writelines(readline[eind:eind+1])
        begin += 50
        eind += 50
