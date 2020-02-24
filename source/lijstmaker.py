import pandas as pd
import os

path = os.getcwd
myfile = r"\bestanden\201922020.csv"
output_file =r"\bestanden\output.csv"

pad = os.path.join('C:\\Users\\mike\\PycharmProjects\\Projekt_lijstbewerken\\' + myfile)
pad_out = os.path.join('C:\\Users\\mike\\PycharmProjects\\Projekt_lijstbewerken\\' + output_file)
print(pad)


lijst_in = pd.read_csv(pad, ";", encoding="utf-8")
lijst_in[0:1]

oap = overaantalpercentage = 1.02  # 1.02 = 2% overlevering


def lijst_maker(art, pdf, aantal):
    """
    Take line from list and build csv for that line
    """

    with open(pad_out, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{art}; {aantal}= x {int(oap*100)}% = {int(aantal*oap)};leeg.pdf\n", end="", file=fn)

        print(f";;{pdf}\n" * int(aantal * oap), end="", file=fn)
        # print(f"{art}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{art}; {aantal}= x 102% = {int(aantal*oap)};leeg.pdf\n", end="", file=fn)
        print(f";;stans.pdf\n", end="", file=fn)


df1 = lijst_in[["art", "pdf", "aantal"]]
df1.to_csv("lijst_in.csv", index=0)

new_input_list = []

with open("lijst_in.csv") as input:
    num = 0
    for line in input:
        line_split = line.split(",")

        new_input_list.append(line_split)
        num += 1

list_length = len(new_input_list)

beg = 1
eind = 2


with open(pad_out, "w", encoding="utf-8") as fn:

    print("art;aantal:pdf", file=fn)

with open(pad_out, "a", encoding="utf-8") as fn:
    for _ in range(list_length - 1):
        a = str(new_input_list[beg:eind][0][0])
        b = str(new_input_list[beg:eind][0][1])
        c = int(new_input_list[beg:eind][0][2])
        lijst_maker(a, b, c)

        beg += 1
        eind += 1
