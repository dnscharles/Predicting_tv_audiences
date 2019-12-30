import datetime

'Boucle créant la date pour url'
'a est l année jusqu à laquelle on veut récupérer les dates'
def dates(a):
    Date = []
    for i in range(2014,a+1):
        for j in range(1,13):
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
                l = 32
            elif j == 4 or j == 6 or j == 9 or j == 11:
                l = 31
            elif j == 2:
                if i == 2016:
                    l = 30
                else:
                    l=29
            for k in range(1,l):
                date = str(datetime.date(i, j, k))
                Date.append(date)       
    return Date[280:-21]

'Génération du chemin'
def chemin(Dates):
    'http://programme-tv.nouvelobs.com/programme-tv/2014-10-08/'
    url = "http://programme-tv.nouvelobs.com/programme-tv/"
    Chemins = []
    for i in range(len(Dates)):
        Chemin = url + str(Dates[i]) + "/"
        Chemins.append(Chemin)
    return Chemins