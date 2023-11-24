import msvcrt

# Funkcja do rysowania planszy
def draw_board():
    pass

# Pozycja startowa
x, y = 1, 1

while True:

    # Odczytywanie ruchu gracza
    key = msvcrt.getch().decode('utf-8').lower()

    # Aktualizacja pozycji gracza
    if key == 'w' and board[x-1][y] == 0:  # Góra
        x -= 1
    elif key == 's' and board[x+1][y] == 0:  # Dół
        x += 1
    elif key == 'a' and board[x][y-1] == 0:  # Lewo
        y -= 1
    elif key == 'd' and board[x][y+1] == 0:  # Prawo
        y += 1
    elif key == 'q':  # Wyjście z gry
        break
