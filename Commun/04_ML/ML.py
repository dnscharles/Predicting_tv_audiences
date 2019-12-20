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
from sklearn.gaussian_process import GaussianProcessClassifier as GPC
from sklearn.gaussian_process.kernels import RBF

import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('figure',figsize=(11,5))

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
              "Heure_prgm2", "Nbre_episodes_prgm2","Age_conseille_prgm2","Part_de_marche"]].values
    chaine_ohe = ohe.fit_transform(data["Chaine"]
                                  .astype(str)
                                  .values
                                  .reshape(-1, 1)
                                 )
    type_prgm2_ohe = ohe.fit_transform(data["Type_prgm2"]
                                  .astype(str)
                                  .values
                                  .reshape(-1, 1)
                                 )
    X = np.concatenate((chaine_ohe.toarray(),type_prgm2_ohe.toarray(),reste), axis=1)
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

def rpz_resultat(predicteur,X_test,y_test):
    table_predite = predicteur.predict(X_test)
    table_predite = table_predite.T
    table_predite = pd.DataFrame(table_predite)
    table_predite = table_predite.astype(np.str)
    table_predite['Types'] = y_test
    table_predite['Types prédits'] = table_predite[0]
    table_predite = table_predite.drop(table_predite.columns[0],axis='columns')
    heat = sns.heatmap(pd.crosstab(table_predite['Types'], table_predite['Types prédits']),
            cmap="YlGnBu", annot=True,fmt='',square=True, cbar=False)
    return heat
    