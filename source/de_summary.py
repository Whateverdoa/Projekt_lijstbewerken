''''work around is put al relevant input in da_huismerk file mes rol etc... then run de summary'''


import pandas as pd
from pathlib import Path
from source.paden_naar_files import file_sum, file_sum_hor,file_sum_vert, VDP_Def
from source.da_huismerk import tmp_rollen_posix_lijst, begin_rolnummer, aantal_per_rol,aantal_rollen,\
    lijstmaker_uit_posixpad_csv, lijst_opbreker, mes,kol_naam_lijst_builder,lees_per_lijst,stapel_df_baan,horizontaal_samenvoegen, order_nummer
from source.paden_naar_files import cleaner, list_of_files_to_clean



def summary_maken(posixlijst, aantal_per_rol, wikkel, rolnummer):
    """haal uit de csv file het begin, ein en rolnummer"""
    rol = pd.read_csv(posixlijst, dtype="str")
    # print(rol.head(1))

    df_rol = pd.DataFrame(rol, columns=["kolom1", "pdf", "omschrijving"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    rol_nummer = pd.DataFrame(
        [(".", "rol nummer", f"{rolnummer}") for x in range(1)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    begin_nummer = pd.DataFrame(
        [(".", "begin nummer", f"{begin}") for x in range(1)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    eind_nummer = pd.DataFrame(
        [(".", "eind nummer",f"{eind}") for x in range(1)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    sluitstuk = pd.DataFrame(
        [[".", "stans.pdf", f"{aantal_per_rol} etiketten"]],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=["kolom1", "pdf", "omschrijving"],
    )

    naam = f"df_{posixlijst.name:>{0}{4}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([rol_nummer, begin_nummer, eind_nummer])

    return naam

#
# testpad =  Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Projekt_lijstbewerken\source\file_out\tmp\rol_0001.csv")
# print(testpad.is_file())
# print(summary_maken(testpad,2500,1,1))

def Summary_files_maken_met_wikkel_en_sluit(posix_rollen_lijst, aantal_per_rol, wikkel, aantalrollen, begin_nummer_rol=0):
    """de totale wikkel functie met de wikkel functie erin"""
    for i in range(aantalrollen):
        csv_naam = f'summary_{i:>{0}{5}}.csv'
        pad = Path(file_sum / csv_naam)
        # print(csv_naam)
        rol = f'rol_{begin_nummer_rol + i + 1:>{0}{3}}'
        summary_maken(posix_rollen_lijst[i], aantal_per_rol, wikkel, rol).to_csv(pad, index=0)
    return


Summary_files_maken_met_wikkel_en_sluit(tmp_rollen_posix_lijst,aantal_per_rol,1,aantal_rollen,begin_rolnummer)

opgebroken_lijst = lijst_opbreker(lijstmaker_uit_posixpad_csv(file_sum),mes)

horizontaal_samenvoegen(opgebroken_lijst,file_sum_hor,mes)

stapel_df_baan("Summary",lijstmaker_uit_posixpad_csv(file_sum_hor), order_nummer, VDP_Def)

print("clean up & done")

for pad in list_of_files_to_clean:
    cleaner(pad)




