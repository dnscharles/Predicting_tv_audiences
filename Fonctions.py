from requests import get
import re
import bs4


'Fonction qui récupère lurl et renvoit larbre'
def arbre(chemin):
    page = get(chemin)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "lxml")
    return arbre


'Fonction qui récupère les logos'
def Logo(arbre):
    logo = []
    logos = arbre.findAll("span", {"class" : "logo"})
    logos = logos[0:19]
    for i in range(len(logos)):
        a = str(logos[i])
        logo.append(a[49:56])
    return logo
    

'Fonction qui récupère les parts de marchés'
def Pdm(arbre):
    pdm = []
    pdms = arbre.findAll("em", {"style" : "display: none;"})
    for i in range(len(pdms)):
        b = str(pdms[i])
        pdm.append(b[27:31])
    return pdm[0:19]

'Fonction qui récupère le jour'
def Jour(arbre):
    jour = arbre.find("h1")
    jour = str(jour)
    jours = []
    for i in range(19):
        jours.append(jour[20:-17])
    return jours