import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st

'Gestion date'
def annee(string):
    parts = string.split(' ')
    return parts[2]
def mois(string):
    parts = string.split(' ')
    return parts[1]

'Gestion Jour'
def weekend(string):
    if string == 'samedi' or string == 'dimanche':
        D = 1
    else:
        D = 0
    return D

'Gestion type de programme'
def Prog(string):
    if string == 'Telerealitee' or string == 'Jeu' or string == 'Spectacle' or string == 'Concert' or string == 'Theatre' or string == 'Dessin-anime' or string == 'Ceremonie' or string == 'Gala' or string == 'Opera' or string == 'Clips' or string == 'Talk-Show' or string == 'Danse' or string == 'Musique' or string == 'Ballet':
        P = 'Divertissement'
    elif string == 'Reportage' or string == 'Making-of':
        P = 'Magazine'
    elif string == 'Journal' or string == 'Debat':
        P = 'Information'
    else:
        P = string
    return P

'Gestion duree programme'
def Duree_prog(string):
    parts = string.split(' ')
    if string == "nan":
        return np.nan
    else:
        return parts[0]
    
'Gestion pdm'
def Pdm(string):
    if string == "nan":
        return np.nan
    else:
        P = string.replace(",",".")
        return P

def nettoyage(data):
    'Gestion unnamed'
    data = data.drop(data.columns[0],axis='columns')
    
    'Date'
    data['Annee'] = data['Date']
    data['Annee'] = data['Annee'].apply(annee)
    data['Mois'] = data['Date']
    data['Mois'] = data['Mois'].apply(mois)
    
    'Jour'
    data['Week end'] = data['Jour']
    data['Week end'] = data['Week end'].apply(weekend)
    
    'Chaines'
    data = data.drop(data[data.Chaine == 'RTL 9'].index)
    data = data.drop(data[data.Chaine == '35_" hr'].index)
    
    'Type de programme'
    data['Type_prgm1'] = data['Type_prgm1'].apply(Prog)
    data['Type_prgm2'] = data['Type_prgm2'].apply(Prog)
    data = data.drop(data[data.Type_prgm1 == 'Court-metrage'].index)
    data = data.drop(data[data.Type_prgm1 == 'Programme Court'].index)
    data = data.drop(data[data.Type_prgm2 == 'Court-metrage'].index)
    data = data.drop(data[data.Type_prgm2 == 'Programme Court'].index)
    data = data.drop(data[data.Type_prgm2 == 'Emission religieuse'].index)
    data = data.drop(data[data.Type_prgm2 == 'Fin des emissions'].index)
    
    'Duree programme'
    data['Duree_prgm1'] = data['Duree_prgm1'].astype(str)
    data['Duree_prgm2'] = data['Duree_prgm2'].astype(str)
    data['Duree_prgm1'] = data['Duree_prgm1'].apply(Duree_prog)
    data['Duree_prgm2'] = data['Duree_prgm2'].apply(Duree_prog)
    
    data['Part_de_marche'] = data['Part_de_marche'].astype(str)
    data['Part_de_marche'] = data['Part_de_marche'].apply(Pdm)
    
    return data
    
    
    