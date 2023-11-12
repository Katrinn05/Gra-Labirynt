# Noname
## Autorzy
Jest to wspólny projekt grupy w składzie:  <br>
Maciej Jamroży  <br>
Anna Moroń  <br>
Katsiaryna Naumovich  <br>
Zuzanna Pawłowska  <br>
Joanna Wojnowska  <br>
## licencja 
MIT Licence - szczegóły w LICENSE
## Labirynt
### Główne założenia
Celem projektu jest stworzenie platformowej gry 2D, polegającej na przechodzeniu labiryntu, który nie jest widoczny w całości. Gracz może poruszać się swoją postacią po planszy, jednak widzi tylko jej część wokół siebie, w postaci aureoli. Do dyspozycji ma mini-mapę pokazującą jego ogólne położenie względem krańców mapy.
Poniższe rysunki poglądowo przedstawiają nasz pomysł:

![ilustracja labirynt i pole widzenia](/zdjecia/pole%20widzenia.jpg)

### Grafika
Grafika będzie inspirowana tą z gry sieciowej margonem


### Elementy dodatkowe, potencjalne obszary rozwijania projektu:
- Dodanie kolejnych poziomów gry do tych głównych, a także stworzenie poziomów innego typu np. *“gra na czas”* - w ograniczonym czasie trzeba znaleźć wyjście z labiryntu. Mogłyby to być poziomy bonusowe, takie odblokowywane w trakcie gry, lub w ogóle osobny tryb gry, wybierany podczas logowania. Gracz wchodząc do gry ma do wyboru:
*{Tryb fabularny}*
*{Sprint przez labirynt}*
*{Tryb swobodny}*
*{...}*
- Dodanie możliwości zapisywania postępu gry w trzech miejscach:
*{Miejsce zapisu 1}*
*{Miejsce zapisy 2}*
*{Miejsce zapisy 3}*
	Pozwoli to np. grać trzem osobom na jednym urządzeniu - często spotykane rozwiązanie w dzisiejszych grach.
- Dodanie różnych poziomów trudności, wybieranych na początku gry (możliwych do zmiany później). Np. na poziomie trudnym nie byłoby mini-mapy, lub zakres widzenia byłby mniejszy.
- Dodanie elementów boostów, np. po zebraniu takowego aureola widoku zwiększa się dwukrotnie na czas 4 sekund, i/lub zwiększa się szybkość postaci.
- Dodanie systemu punktów (np. monet) za które można by kupować ułatwienia/boosty, i używać podczas przechodzenia labiryntu. Ikony kupionych boostów wyświetlałyby się np. w rogu ekranu, po kliknięciu byłyby aktywowane.

### Proponowane rozwiązania:
1. Grę będziemy programować przy użyciu języka **Python** - zapewnia idealne warunki do tworzenia niezbyt skomplikowanych gier.
1. Labirynt może być zapisany jako lista dwuwymiarowa: poszczególne pola byłyby korytarzem/ ścianami/ monetami/ etc.
1. Po planszy-tablicy poruszamy się strzałkami, program odpowiednio reaguje w zależności na jakie pole chcemy przejść.
1. **Pygame** - stworzymy w nim prosty interfejs gry (jest dostępnych wiele tutoriali).
1. Grafiki będą tworzone za pomocą programów FireAlpaca (możliwość tworzenia animacji) i Krita.

### Cele poboczne projektu:
1. Zdobycie umiejętności programowania w **pythonie**. Podstawowych oraz tych zorientowanych na kodowaniu mechaniki gier.
1. Poznanie różnorodnych narzędzi informatycznych, które ułatwiają współpracę między uczestnikami projektu.
1. Doskonalenie umiejętności pracy w zespole.
