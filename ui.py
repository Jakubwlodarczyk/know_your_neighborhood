import os


class Ui:

    @staticmethod
    def print_table(table, title, title_list):
        """
        prints format table of data
        :param table: list of data
        :param title: string, info about table
        :param title_list: list of strings, first line of table
        """
        os.system("clear")
        print(title)
        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            for row in table:
                if len(str(row[title_iterator])) > len_col:
                    len_col = len(str(row[title_iterator]))
            len_for_col.append(len_col)

        how_wide = 0
        for item in title_list:
            x = (len_for_col[title_list.index(item)])
            how_wide += (len(("|{: <" + str(x + 2) + "}").format(item)))
        print('-' * how_wide)

        for name in title_list:
            print("|", end="")
            x = (len_for_col[title_list.index(name)])
            print(("{: <" + str(x + 2) + "}").format(name), end="")
        print("|")
        print('-' * how_wide)

        for row in table:
            print("|", end="")
            for element in row:
                x = (len_for_col[row.index(element)])
                print(("{: <" + str(x + 2) + "}|").format(element), end="")
            print()
        print('-' * how_wide)

    @staticmethod
    def get_input(title):
        """
        get input from user
        :param title: text to display in input
        :return: user input
        """
        user_input = input('{}'.format(title))
        return user_input

    @staticmethod
    def print_message(text):
        """
        Print text
        :param text: string to print
        """
        print(text)

    @staticmethod
    def print_menu():
        """
        print menu options
        """
        os.system('clear')
        print("""What would you like to do:\n
        (1) List statistics
        (2) Display 3 cities with longest names
        (3) Display county's name with the largest number of communities
        (4) Display locations, that belong to more than one category
        (5) Advanced search
        (0) Exit program\n""")
