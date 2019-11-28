import pandas as pd

'Fonction qui alimente le data frame'
def Donnee(Date,Logo,Pdm,Donnees):
    Data = pd.DataFrame({"Date": [], "Chaine": [], "Part_de_marche": []})
    Data["Date"],Data["Chaine"],Data["Part_de_marche"] = Date,Logo,Pdm
    Donnees = pd.concat([Donnees, Data],ignore_index = True)
    return Donnees