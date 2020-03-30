import pandas as pd
from pathlib import Path

file = "file_in/QR_600X50.csv"
test_file = "test2722020.csv"

wdir = Path.cwd()
file_in = wdir / file
print(wdir)
print(file_in.is_file())
file_out_test= r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_in\202011034\output"
file_tmp = wdir / "file_out/tmp"
file_tmp_2 = wdir / "file_out/tmp2"
hor = wdir / "file_out/hor"
vert = wdir / "file_out/vert"
VDP_Def = wdir / "VDP_Def/"

print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

file_tmp_2.mkdir(parents=True, exist_ok=True)
file_tmp.mkdir(parents=True, exist_ok=True)
vert.mkdir(parents=True, exist_ok=True)
hor.mkdir(parents=True, exist_ok=True)
VDP_Def.mkdir(parents=True, exist_ok=True)


