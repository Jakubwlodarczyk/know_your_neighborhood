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
                os.system('clear')
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
                os.system('clear')
                Ui.print_message("County's name with the largest number of communities:"
                                 "\n\n{}, has {} communities"
                                 .format(Cities.get_largest_county()[1], Cities.get_largest_county()[0]))
                Ui.get_input('\nEnter to continue:')
            elif option == '4':
                os.system('clear')
                idx = 1
                Ui.print_message("Locations, that belong to more than one category:\n")
                for i in sorted(Cities.get_multi_types_objects()):
                    Ui.print_message("{}. {}".format(idx, i))
                    idx += 1
                Ui.get_input('\nEnter to continue:')
            elif option == '5':
                os.system('clear')
                user_input = Ui.get_input('Searching for: ')
                search_result = Cities.get_search_items(user_input)
                if search_result:
                    Ui.print_message('Found {}'.format(len(search_result)))
                    Ui.print_table(sorted(search_result), "", ['Location', 'Type'])
                    Ui.get_input('\nEnter to continue:')
                else:
                    Ui.print_message('No match')
                    Ui.get_input('\nEnter to continue:')
            elif option == '0':
                os.system('clear')
                sys.exit()
            else:
                Ui.print_message("\nWrong input, try again.")


def main():
    Cities.create_table_csv()
    Menu.menu_handle()

if __name__ == '__main__':
    main()
