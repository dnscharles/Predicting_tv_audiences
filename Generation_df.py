import pandas as pd

'Fonction qui alimente le data frame'
def Donnee(Date,Logo,Pdm,Donnees):
    Data = pd.DataFrame({"Date": [], "Logo_chaîne": [], "Part_de_marché": []})
    Data["Date"],Data["Logo_chaîne"],Data["Part_de_marché"] = Date,Logo,Pdm
    Donnees = pd.concat([Donnees, Data],ignore_index = True)
    return Donnees