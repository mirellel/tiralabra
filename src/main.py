'''Moduuli, joka käynnistää pelin'''
from files.menu import Menu

def main():
    '''Funktio aloittaa sovelluksen pyörityksen'''
    game = Menu()
    game.run_menu()

if __name__ == "__main__":
    main()
