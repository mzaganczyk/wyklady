import requests
import os
import zipfile


def pobierz_mormula(url):
    local_filename = url.split('/')[-1]
    if local_filename in os.listdir(os.getcwd()):
        return True
    else:
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            f.write(r.content)


def spakuj_mormula(nazwa):
    newzip = zipfile.ZipFile('{}.zip'.format(nazwa), 'w')
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.pdf'):
            newzip.write(filename)
    newzip.close()
    print("Mormul spakowany.")


i = 1

while True:
    url = 'https://www.mimuw.edu.pl/~mormul/w{}.pdf'.format(i)
    if requests.get(url).status_code != 200:
        print("Mormul nie ma wiecej :(")
        spakuj_mormula("mormul")
        break
    else:
        if pobierz_mormula(url):
            print("Mormul {} juz jest.".format(i))
        else:
            pobierz_mormula(url)
            print("Mormul {} pobrany.".format(i))
    i += 1
