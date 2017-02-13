from ui import Ui
from cities import Cities
import sys
import os


class Menu:
    """
    handle full menu options
    """

    @staticmethod
    def menu_handle():
        while True:
            Ui.print_menu()
            option = Ui.get_input("Choose an option: ")
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
            elif option == '0':
                os.system('clear')
                sys.exit()
                pass


def main():
    Cities.create_table_csv()
    Menu.menu_handle()

if __name__ == '__main__':
    main()
