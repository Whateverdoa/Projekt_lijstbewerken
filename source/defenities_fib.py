
import pandas as pd
from pathlib import Path



def lijst_opbreker(lijst_in, mes, combinaties):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes
        end += mes
    return combinatie_binnen_mes

def kol_naam_lijst_builder(mes=1):
    kollomnaamlijst=[]

    for count in range(1,mes+1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        # kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)


    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst

def lees_per_lijst(lijst_met_posix_paden):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count=1
    concatlist=[]
    for posix_pad_naar_file in lijst_met_posix_paden:
        print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count+=1
    kolomnamen=kol_naam_lijst_builder(5)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]


    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1

def df_rol_builder(posixlijst_naam,aantal_per_rol, wikkel):

    rol = pd.DataFrame(posixlijst_naam)


    df_rol = pd.DataFrame(rol, columns=["omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [("", "stans.pdf") for x in range(2)],
        columns=["omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [("", "stans.pdf") for x in range(wikkel)],
        columns=["omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{begin} t/m {eind}", "stans.pdf"]],
        columns=["omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam