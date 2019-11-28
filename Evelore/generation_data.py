import pandas as pd

def Donnee(Date, Chaine, Heure1, Titre1, Type1,Durée1, Nbre1, Age1, Heure2, Titre2, Type2, Durée2, Nbre2, Age2,Donnees):
    Data = pd.DataFrame({"Date": [], "Chaine": [], "Heure_prgm1": [], "Titre_prgm1": [], "Type_prgm1": [], "Duree_prgm1": [], "Nbre_episodes_prgm1": [], "Age_conseille_prgm1": [],"Heure_prgm2": [], "Titre_prgm2": [], "Type_prgm2": [], "Duree_prgm2": [],"Nbre_episodes_prgm2": [], "Age_conseille_prgm2": []})
    [Data["Date"],Data["Chaine"],Data["Heure_prgm1"], Data["Titre_prgm1"], Data["Type_prgm1"],Data["Duree_prgm1"],Data["Nbre_episodes_prgm1"],Data["Age_conseille_prgm1"],Data["Heure_prgm2"], Data["Titre_prgm2"], Data["Type_prgm2"], Data["Duree_prgm2"], Data["Nbre_episodes_prgm2"],Data["Age_conseille_prgm2"]] = [Date, Chaine, Heure1, Titre1, Type1,Durée1,Nbre1, Age1, Heure2, Titre2,Type2, Durée2, Nbre2, Age2]
    Donnees = pd.concat([Donnees, Data],ignore_index = True)
    return Donnees