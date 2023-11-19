import pygame
import json

pygame.init()

# Obiekt do przechowywania postępu gry
postep = {
    'zdobyte_punkty': 0,
    'poziom': 1
}

# Funkcja do zapisywania postępu
def zapisz_postep(postep, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        json.dump(postep, plik)

# Funkcja do wczytywania postępu
def wczytaj_postep(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            postep = json.load(plik)
            return postep
    except FileNotFoundError:
        return None

# Zapisz postęp gry
zapisz_postep(postep, 'zapis1.json')

# Wczytaj postęp gry
postep = wczytaj_postep('zapis1.json')

pygame.quit()
