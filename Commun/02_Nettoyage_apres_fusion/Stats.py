def stats(A):
    for cat in data[A].unique():
        subset = data[data.Type_prgm1 == cat] # Création du sous-échantillon
        print("-"*20)
        print(cat)
        print("moy:\n",subset[B].mean())
        print("med:\n",subset[B].median())
        print("mod:\n",subset[B].mode())
        subset["Duree_prgm1"].hist() # Crée l'histogramme
        plt.show() # Affiche l'histogramme