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
                Ui.print_table(Cities.count_statistic(), 'LIST STATISTICS', ['Małopolska', 'count'])
                Ui.get_input('\nENTER to go back')
            elif option == '2':
                os.system('clear')
                name_list = Cities.get_name_list()
                idx = 1
                Ui.print_message("Cities with longest names\n")
                for i in Cities.get_longest_words(name_list):
                    Ui.print_message("{}. {}".format(idx, i))
                    idx += 1
                Ui.get_input('\nEnter to continue:')
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
            elif option == '0':
                os.system('clear')
                sys.exit()
            else:
                Ui.print_message("Wrong input, try again.")


def main():
    Cities.create_table_csv()
    Menu.menu_handle()

if __name__ == '__main__':
    main()
