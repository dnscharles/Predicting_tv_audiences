import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

from sklearn.model_selection import (train_test_split,
                                     RandomizedSearchCV,
                                    GridSearchCV)

from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNN

def recodage(data):
    ohe = OneHotEncoder()
    le = LabelEncoder()
    data['Jour'] = le.fit_transform(data["Jour"].astype(str))
    data['Mois'] = le.fit_transform(data["Mois"].astype(str))

    data['Heure_prgm1'] = le.fit_transform(data["Heure_prgm1"].astype(str))
    data['Heure_prgm2'] = le.fit_transform(data["Heure_prgm2"].astype(str))

    data['Age_conseille_prgm1'] = le.fit_transform(data["Age_conseille_prgm1"].astype(str))
    data['Age_conseille_prgm2'] = le.fit_transform(data["Age_conseille_prgm2"].astype(str))

    data['Type_prgm1'] = le.fit_transform(data["Type_prgm1"].astype(str))
    data['Type_prgm2'] = le.fit_transform(data["Type_prgm2"].astype(str))

    reste = data[["Jour","Week end","Mois","Annee","Heure_prgm1","Duree_prgm1","Duree_prgm2", "Nbre_episodes_prgm1","Age_conseille_prgm1",
              "Heure_prgm2", "Nbre_episodes_prgm2","Age_conseille_prgm2","Part_de_marche",
             "Type_prgm2"]].values
    chaine_ohe = ohe.fit_transform(data["Chaine"]
                                  .astype(str)
                                  .values
                                  .reshape(-1, 1)
                                 )
    X = np.concatenate((chaine_ohe.toarray(),reste), axis=1)
    y = data[['Type_prgm1']].values
    return X,y

def split(X,y,n=0.9):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   test_size=0.9)
    return X_train, X_test, y_train, y_test

def normalisation(X_train,X_test):
    ss = StandardScaler()
    mm = MinMaxScaler()
    X_train_ess = ss.fit_transform(X_train)
    X_train_emm = mm.fit_transform(X_train)
    X_test_ess = ss.fit_transform(X_test)
    X_test_emm = mm.fit_transform(X_test)
    return X_train_ess, X_train_emm, X_test_ess, X_test_emm
