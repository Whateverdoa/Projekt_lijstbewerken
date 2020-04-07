import pandas as pd
from pathlib import Path



file = "file_in/202011035/Remark1.csv"
test_file = "test2722020.csv"

wdir = Path.cwd()
file_in = wdir / file
print(wdir)
print(file_in.is_file())
file_out_test= r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_in\202011035\output"
file_tmp = wdir / "file_out/tmp"
file_tmp_2 = wdir / "file_out/tmp2"
hor = wdir / "file_out/hor"
vert = wdir / "file_out/vert"
VDP_Def = wdir / "VDP_Def/"
file_sum = wdir / "summary"
file_sum_hor = wdir / "summary/hor"
file_sum_vert = wdir / "summary/vert"

print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

file_tmp_2.mkdir(parents=True, exist_ok=True)
file_tmp.mkdir(parents=True, exist_ok=True)
vert.mkdir(parents=True, exist_ok=True)
hor.mkdir(parents=True, exist_ok=True)
VDP_Def.mkdir(parents=True, exist_ok=True)
file_sum.mkdir(parents=True, exist_ok=True)
file_sum_hor.mkdir(parents=True, exist_ok=True)
file_sum_vert.mkdir(parents=True, exist_ok=True)

list_of_files_to_clean = [file_tmp_2,file_tmp,hor, vert,file_sum_hor,file_sum_vert]
def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()



