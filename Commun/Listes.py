'Vecteur des dates'
def date(j,m,a):
    Dates = []
    for k in range(a):
        for l in range(m):
            for i in range(j):
                'Jour'
                if i < 9:
                    JJ = "0" + str(i+1)
                else:
                    JJ = str(i+1)
                'Mois'
                if l < 9:
                    MM = "0" + str(l+1)
                else:
                    MM = str(l+1)
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