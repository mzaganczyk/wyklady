import requests
import os
import zipfile

'''
Skrypt pozwala na pobieranie skrypcików z analizy, v. 0.0.0.0.0.0.1
Marcinek
'''


def pobierz_mormula(url):
    nazwa_wykladu = url.split('/')[-1]
    if nazwa_wykladu in os.listdir(os.getcwd()):
        return True
    else:
        r = requests.get(url, stream=True)
        with open(nazwa_wykladu, 'wb') as f:
            f.write(r.content)


def spakuj_mormula(nazwa):
    newzip = zipfile.ZipFile('{}.zip'.format(nazwa), 'w')
    for wyklad in os.listdir(os.getcwd()):
        if wyklad.endswith('.pdf'):
            newzip.write(wyklad)
    newzip.close()
    print("Mormul spakowany.")


i = 1

while True:
    url = 'https://www.mimuw.edu.pl/~mormul/w{}.pdf'.format(i)
    if requests.get(url).status_code != 200:
        print("Mormul nie ma wiecej :(")
        spakuj_mormula("mormul")
        usun = bool(input("Chcesz usunac pdfy? 'True', 'False' "))
        if usun:
            for wyklad in range(1, i):
                os.remove("w{}.pdf".format(wyklad))
            print("Wyklady usuniete.")
            break
        else:
            break
    else:
        if pobierz_mormula(url):
            print("Mormul {} juz jest.".format(i))
        else:
            pobierz_mormula(url)
            print("Mormul {} pobrany.".format(i))
    i += 1
