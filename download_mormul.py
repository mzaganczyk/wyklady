import requests
import os
import zipfile
from tqdm import tqdm
import math

'''
Skrypt pozwala na pobieranie skrypcików z analizy, v. 0.0.0.0.0.0.1.2
Marcinek
'''


def pobierz_wyklady(url):
    r = requests.get(url, stream=True)
    rozmiar = int(r.headers.get('content-length', 0))
    rozmiarpobrany = 1024
    kwadrat = int(rozmiar/rozmiarpobrany)
    pobrany = 0
    with open(nazwa_wykladu, 'wb') as f:
        for plik in tqdm(r.iter_content(chunk_size=rozmiarpobrany),
                           total=kwadrat, unit='KB', unit_scale=True,
                           desc=nazwa_wykladu, leave=True, dynamic_ncols=True):
            f.write(plik)
            pobrany += rozmiarpobrany

def spakuj_wyklady(nazwa):
    newzip = zipfile.ZipFile(f'{nazwa}.zip', 'w')
    for wyklad in os.listdir(os.getcwd()):
        if wyklad.endswith('.pdf'):
            newzip.write(wyklad)
    newzip.close()
    print("Wyklady spakowane.")


i = 1

while True:
    url = f'https://www.mimuw.edu.pl/~mormul/w{i}.pdf'
    nazwa_wykladu = url.split('/')[-1]
    if nazwa_wykladu not in os.listdir(os.getcwd()):
        if requests.get(url).status_code != 200:
            print('Nie ma wiecej wykladow.')
            spakuj_wyklady('wyklady')
            usuwanie = input('Czy chcesz usunac pdfy? "Tak", "Nie".').lower()
            if usuwanie == "tak":
                for wyklad in range(1,i):
                    os.remove(f'w{wyklad}.pdf')
                print("Wyklady usuniete.")
                break
            else:
                break
        pobierz_wyklady(url)
        print(f'Wyklad {i} pobrany.')
    else:
        print(f'Wyklad {i} jest juz pobrany.')
    i += 1
