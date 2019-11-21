import pandas as pd

def Donnee(Date, Chaine, Heure1, Titre1, Type1,Durée1, Nbre1, Age1, Heure2, Titre2, Type2, Durée2, Nbre2, Age2,Donnees):
    Data = pd.DataFrame({"Date": [], "Chaîne": [], "Heure_prgm1": [], "Titre_prgm1": [], "Type_prgm1": [], "Durée_prgm1": [], "Nbre_épisodes_prgm1": [], "Age_conseillé_prgm1": [],"Heure_prgm2": [], "Titre_prgm2": [], "Type_prgm2": [], "Durée_prgm2": [],"Nbre_épisodes_prgm2": [], "Age_conseillé_prgm2": []})
    [Data["Date"],Data["Chaîne"],Data["Heure_prgm1"], Data["Titre_prgm1"], Data["Type_prgm1"],Data["Durée_prgm1"],Data["Nbre_épisodes_prgm1"],Data["Age_conseillé_prgm1"],Data["Heure_prgm2"], Data["Titre_prgm2"], Data["Type_prgm2"], Data["Durée_prgm2"], Data["Nbre_épisodes_prgm2"],Data["Age_conseillé_prgm2"]] = [Date, Chaine, Heure1, Titre1, Type1,Durée1,Nbre1, Age1, Heure2, Titre2,Type2, Durée2, Nbre2, Age2]
    Donnees = pd.concat([Donnees, Data],ignore_index = True)
    return Donnees