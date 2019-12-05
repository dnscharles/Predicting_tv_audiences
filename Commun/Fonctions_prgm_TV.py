import requests as rq
import re
import bs4

'Arbre'
def tree(chemin):
    page = rq.get(chemin)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "html.parser")
    return arbre

'Jour du programme TV'
def jour(arbre):
    jour = arbre.findAll("h1")
    jour = re.findall("TV (.*) \(",str(jour))
    date = []
    for i in range(25):
        result = jour
        result = str(jour)[2:-2]
        result = result.split(" ")[0]
        date.append(result)
    return date

'Date du programme'
def date(arbre):
    jour = arbre.findAll("h1")
    jour = re.findall("TV (.*) \(",str(jour))
    date = []
    for i in range(25):
        result = jour
        result = str(jour)[2:-2]
        if result[0] == "d":
            result = result.split("che ")[1]
        else:
            result = result.split("di ")[1]
        for k in range(1,10):
            if result[0:2] == str(k) + " ":
                result = str(0) + str(result)
        date.append(result)
    return date

'Chaîne'
def chaines(arbre):
    noeud = arbre.findAll("div", {"class":"logo_chaine_g"})
    chn = re.findall("Programme(.{0,23})",str(noeud)) 
    chaine = [] 
    for i in range(25):
        result = chn[i].split('"')[0]
        chaine.append(result)
    return chaine

'Heure du premier programme'
def heures1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    heure = []
    for i in range(0,50,2):
        result = re.findall("b t16\">(.*)</span> ",str(noeud[i]))
        result = str(result)[2:7]
        if result == "":
            result = "NA"
        heure.append(result)
    return heure

'Heure du deuxième programme'
def heures2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    heure = []
    for i in range(1,50,2):
        result = re.findall("b t16\">(.*)</span> ",str(noeud[i]))
        result = str(result)[2:7]
        if result == "":
            result = "NA"
        heure.append(result)
    return heure

'Titre du premier programme'
def titres1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    titre = []
    for i in range(0,50,2):
        arbre2 = bs4.BeautifulSoup(str(noeud[i]),"lxml")
        noeud2 = arbre2.find_all("span",{"class":"titre b"})
        if noeud2 == []:
            noeud2 = arbre2.find_all("a",{"class":"titre b"})
        result = re.findall(">(.*)<", str(noeud2))
        result = str(result).replace("&amp;", "&")
        result = str(result).replace(";", "")
        result = result[2:-2]
        if result == "":
            result = "NA"
        titre.append(result)
    return titre

'Titre du deuxième programme'
def titres2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    titre = []
    for i in range(1,50,2):
        arbre2 = bs4.BeautifulSoup(str(noeud[i]),"lxml")
        noeud2 = arbre2.find_all("span",{"class":"titre b"})
        if noeud2 == []:
            noeud2 = arbre2.find_all("a",{"class":"titre b"})
        result = re.findall(">(.*)<", str(noeud2))
        result = str(result).replace("&amp;", "&")
        result = str(result).replace(";", "")
        result = result[2:-2]
        if result == "":
            result = "NA"
        titre.append(result)
    return titre

'Type du premier programme'
def type_prgm1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    typ = []
    for i in range(0,50,2):
        result = re.findall("cat-(.{0,30})",str(noeud[i]))
        result = str(result).split('"')[0]
        if result == "[]":
            result = "NA"
        typ.append(result)
    return typ

'Type du deuxième programme'
def type_prgm2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    typ = []
    for i in range(1,51,2):
        result = re.findall("cat-(.{0,30})",str(noeud[i]))
        result = str(result).split('"')[0]
        if result == "[]":
            result = "NA"
        typ.append(result)
    return typ

'Durée du premier programme en minutes'
def temps_prgm1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    temps = []
    for i in range(0,50,2):
        result = re.findall("<br/>\((.{0,6})",str(noeud[i]))
        result = str(result)[2:5]
        if result == "":
            result = "NA"
        temps.append(result)
    return temps

'Durée du deuxième programme en minutes'
def temps_prgm2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    temps = []
    for i in range(1,50,2):
        result = re.findall("<br/>\((.{0,6})",str(noeud[i]))
        result = str(result)[2:5]
        if result == "":
            result = "NA"
        temps.append(result)
    return temps

'Nombres épisodes du premier programme'
def nbre_ep1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    nbre = []
    for i in range(0,50,2):
        result = re.findall("(.{0,2})épisodes",str(noeud[i]))
        if len(result) > 1:
            result = result[0]
        else:
            result = result
        if len(str(result)) > 4:
            result = str(result)[2:-2]
        if result == []:
            result = "0"
        nbre.append(result)
    return nbre 

'Nombre épisodes du deuxième programme'
def nbre_ep2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    nbre = []
    for i in range(1,50,2):
        result = re.findall("(.{0,2})épisodes",str(noeud[i]))
        if len(result) > 1:
            result = result[0]
        else:
            result = result
        if len(str(result)) > 4:
            result = str(result)[2:-2]
        if result == []:
            result = "0"
        nbre.append(result)
    return nbre 

'Age conseillé du premier programme'
def ages1(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    age = []
    for i in range(0,50,2):
        result = re.findall("tv right t22 line4\">(.{0,1})", str(noeud[i]))
        if result == ['2']:
            result = '-10 ans'
        elif result == ['3']:
            result = '-12 ans'
        elif result == ['4']:
            result = '-16 ans'
        elif result == ['5']:
            result = '-18 ans'
        elif result == []:
            result = "NA"
        age.append(result)
    return age

'Age conseillé du deuxième programme'
def ages2(arbre):
    noeud = arbre.find_all("div",{"class":"b_d prog1"})
    age = []
    for i in range(1,50,2):
        result = re.findall("tv right t22 line4\">(.{0,1})", str(noeud[i]))
        if result == ['2']:
            result = '-10 ans'
        elif result == ['3']:
            result = '-12 ans'
        elif result == ['4']:
            result = '-16 ans'
        elif result == ['5']:
            result = '-18 ans'
        elif result == []:
            result = "NA"
        age.append(result)
    return age