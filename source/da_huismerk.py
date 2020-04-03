#!

import pandas as pd
from pathlib import Path

# todo add gui
# todo add functions module and paths module
# todo flexibel maken concat en mes en wikkel fucties

order_nummer = "202011034_3"  # wordt in GUI --> filenaam.stem
# source\file_in\202011034\Huismerk0.csv
file = r"file_in\202011034\output\file_0003.csv"
test_file = "file_out/Remark_out2-4-2020.csv"

wdir = Path.cwd()
print(wdir)
file_in = wdir / file
print(file_in)
print(wdir)
print(file_in.is_file())

file_tmp = wdir / "file_out/tmp"
file_tmp_2 = wdir / "file_out/tmp2"
hor = wdir / "file_out/hor"
vert = wdir / "file_out/vert"
VDP_Def = wdir / "VDP_Def/"

print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

aantal_per_rol = 2500
begin_rolnummer = 1200  # count zero, will fix default = 0 voor rol 1

df = pd.read_csv(file_in, ";", dtype="str")
aantal = len(df)

aantal_rollen = aantal // aantal_per_rol

baan = len(df) // 2500

mes = 15
combinaties = aantal_rollen // mes
wikkel = 19  # +2 = 21
etiketten_Y = 54
inloop = etiketten_Y * 10

print(f'de file bestaat uit {aantal} rows')
print(f'aantal rollen = {aantal_rollen}')
print(f'baan = {baan} || wikkel ={wikkel + 2}')


def breek_naar_csv(csv_file_in, aantalperrol, aantalrollen):
    """# dit is een functie waard maak een dataframe
    van lijst en maak dan x aantal csv files"""

    begin = 0
    eind = aantalperrol

    for i in range(1, aantalrollen + 1):
        rol = f'{file_tmp}/rol_{i:>{0}{4}}.csv'
        df.iloc[begin:eind].to_csv(rol, index=0)
        begin += aantalperrol
        eind += aantalperrol


breek_naar_csv(file_in, aantal_per_rol, aantal_rollen)




def wikkel_aan_file_zetten(posixlijst, aantal_per_rol, wikkel, rolnummer):
    """nee de csv file en zet er een sluitetiket en een wikkel aan"""
    rol = pd.read_csv(posixlijst, dtype="str")
    # print(rol.head(1))

    df_rol = pd.DataFrame(rol, columns=["kolom1", "pdf", "omschrijving"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [(".", "stans.pdf", "") for x in range(2)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    wikkel_df = pd.DataFrame(
        [(".", "stans.pdf", "") for x in range(wikkel)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    sluitstuk = pd.DataFrame(
        [[".", "stans.pdf", f"{rolnummer} {begin} t/m {eind} {aantal_per_rol} etiketten"]],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=["kolom1", "pdf", "omschrijving"],
    )

    naam = f"df_{posixlijst.name:>{0}{4}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def files_maken_met_wikkel_en_sluit(posix_rollen_lijst, aantal_per_rol, wikkel, aantalrollen, begin_nummer_rol=0):
    """de totale wikkel functie met de wikkel functie erin"""
    for i in range(aantalrollen):
        csv_naam = f'wikkel_sluit_{i:>{0}{5}}.csv'
        pad = Path(file_tmp_2 / csv_naam)
        # print(csv_naam)
        rol = f'rol_{begin_nummer_rol + i + 1:>{0}{3}}'
        wikkel_aan_file_zetten(posix_rollen_lijst[i], aantal_per_rol, wikkel, rol).to_csv(pad, index=0)
    return csv_naam


def lijstmaker_uit_posixpad_csv(padnaam):
    rollen_posix_lijst = [rol for rol in padnaam.glob("*.csv") if rol.is_file()]
    return rollen_posix_lijst

# todo maak def voor deze list comp
tmp_rollen_lijst = [rol.name for rol in file_tmp.glob("*.csv") if rol.is_file()]
tmp_rollen_posix_lijst = [rol for rol in file_tmp.glob("*.csv") if rol.is_file()]

# wikkel_aan_file_zetten(tmp_rollen_posix_lijst[0], 50, 3).to_csv(file_tmp / test_file)

files_maken_met_wikkel_en_sluit(tmp_rollen_posix_lijst, aantal_per_rol, wikkel, aantal_rollen, begin_rolnummer)

print(tmp_rollen_lijst[0:5])


def lijst_opbreker(lijst_in, mes_waarde):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes_waarde
        end += mes_waarde
    return combinatie_binnen_mes


# todo maak def voor deze list comp
tmp_rollen_posix_lijst_met_wikkel = [rol for rol in file_tmp_2.glob("*.csv") if rol.is_file()]
print(tmp_rollen_posix_lijst_met_wikkel)

lijst_tmp2 = lijst_opbreker(tmp_rollen_posix_lijst_met_wikkel, mes)


# print(lijst_opbreker(tmp_rollen_lijst,5))
# print(lijst_opbreker(tmp_rollen_posix_lijst,5))

# for lijst in lijst_opbreker(tmp_rollen_posix_lijst,5):
# print(f'dit is een lijst van 5 : {lijst}')

def kol_naam_lijst_builder(mes_waarde=1):
    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        num = f"kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


# hier komt een stukje num verz om de hoek kijken

# todo def maken
def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit/ vdp_hor_stap
        # print(vdp_hor_stap)
        df = lees_per_lijst(lijst_met_posix, mes)
        print(df.tail(5))
        lees_per_lijst(lijst_met_posix, mes).to_csv(vdp_hor_stap, index=0)

        count += 1


count = 1
for lijst_met_posix in lijst_tmp2:
    vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
    vdp_hor_stap = hor / vdp_hor_stap
    # print(vdp_hor_stap)
    df = lees_per_lijst(lijst_met_posix, mes)
    print(df.tail(5))
    lees_per_lijst(lijst_met_posix, mes).to_csv(vdp_hor_stap, index=0)

    count += 1


def stapel_df_baan(naam,lijstin, ordernummer, map_uit):
    stapel_df = []
    for lijst_naam in lijstin:
        print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ";", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ";")


hor_lijst = [rol for rol in hor.glob("*.csv") if rol.is_file()]
print(hor_lijst)

stapel_df_baan("VDP",hor_lijst, order_nummer, vert)

print("klaar?  alleen nog in en uitloop")


# testing 123

def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """suplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ","
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)

    namen = list_to_string(kollomnaamlijst)

    return namen





def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".,stans.pdf,," * mes) + "\n"

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = VDP_Def / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])


VDP_final = [vdp for vdp in vert.glob("*.csv") if vdp.is_file()]
print(VDP_final)

wikkel_n_baans_tc(VDP_final, etiketten_Y, inloop, mes)

# todo cleaner maken
# todo 15 banen maken
# todo x aantal vdps
# todo paden module toevoegen

#todo where does the extracolumn come from?
