import requests
import os
import zipfile

i = 1


def pobierz_mormula(url):
    nazwa_wykladu = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(nazwa_wykladu, 'wb') as f:
        f.write(r.content)


def spakuj_mormula(nazwa):
    newzip = zipfile.ZipFile('{}.zip'.format(nazwa), 'w')
    for wyklad in os.listdir(os.getcwd()):
        if wyklad.endswith('.pdf') and not wyklad.isalpha():
            newzip.write(wyklad)
    newzip.close()
    print("Mormul spakowany")


while True:
    url = 'https://www.mimuw.edu.pl/~mormul/w{}.pdf'.format(i)
    if requests.get(url).status_code != 200:
        print("Mormul nie ma wiecej :(")
        spakuj_mormula("mormul")
        break
    else:
        pobierz_mormula(url)
        print("Mormul {} pobrany".format(i))
        i += 1