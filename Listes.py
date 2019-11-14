'Vecteur des dates'
def date(j,m,a):
    Dates = []
    for k in range(j):
        for j in range(m):
            for i in range(a):
                'Jour'
                if i < 10:
                    JJ = "0" + str(i+1)
                else:
                    JJ = str(i+1)
                'Mois'
                if j < 10:
                    MM = "0" + str(j+1)
                else:
                    MM = str(j+1)
                'Année'
                AAAA = k + 2014
                AAAA = str(AAAA)
                'Date'
                Date = JJ + "-" + MM + "-" + AAAA
                Dates.append(Date)
    return Dates
            
'Vecteur des chemins'
def chemin(Dates):
    url = "https://www.programme-television.org/audiences/"
    Chemins = []
    for i in range(len(Dates)):
        Chemin = url + Dates[i]
        Chemins.append(Chemin)
    return Chemins