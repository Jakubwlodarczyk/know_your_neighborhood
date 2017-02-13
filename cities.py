import csv


class Cities:

    city_list = []

    def __init__(self, province, county, community, rgmi, name, type):
        self.province = province
        self.county = county
        self.community = community
        self.rgmi = rgmi
        self.name = name
        self.type = type

    def __str__(self):
        return self.name

    @staticmethod
    def create_table_csv():
        """
        Create object and append to list
        """
        city_table = Cities.read_file('malopolska.csv')
        for row in city_table:
            new_object = Cities(row[0], row[1], row[2], row[3], row[4], row[5])
            Cities.city_list.append(new_object)

    @staticmethod
    def read_file(file_name):
        """
        Read csv file
        :param file_name: name of file to read
        :return: list
        """
        new_table = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                new_table.append(row)
        return new_table[1:]

    @classmethod
    def count_statistic(cls):
        """
        Count statistic
        :return: list with statistic of all city
        """
        statistic = [['województwo', 0], ['powiat', 0], ['gmina miejska', 0], ['gmina wiejska', 0],
                     ['gmina miejsko-wiejska', 0], ['obszar wiejski', 0], ['miasto', 0],
                     ['miasto na prawach powiatu', 0], ['delegatura', 0]]
        for item in cls.city_list:
            statistic = Cities.change_statistic_value(item, statistic)
        return statistic

    @staticmethod
    def change_statistic_value(object_to_check, statistic_list):
        """
        change value in statistic list
        :param object_to_check: object to check which type it is
        :param statistic_list: list with statistic to change
        :return: statistic list
        """
        for item in statistic_list:
            if object_to_check.type == item[0]:
                item[1] += 1
        return statistic_list

    @classmethod
    def get_name_list(cls):
        """
        :return: Name of all cities without duplicate
        """
        name_list = []
        for item in cls.city_list:
            if item.name not in name_list:
                name_list.append(item.name)
        return name_list

    @staticmethod
    def get_longest_words(words_list, amount=3):
        """
        Check longest word in list
        :param words_list: list of words to check
        :param amount: how many words should be returned
        :return: list of words
        """
        words_list.sort(key=len, reverse=True)
        return words_list[:amount]

    @classmethod
    def get_largest_county(cls):
        """
        Check which count is the largest
        :return: The largest county
        """
        county_number = ''
        community_number = 0
        for item in Cities.city_list:
            if item.community:
                if int(item.community) > community_number:
                    community_number = int(item.community)
                    county_number = item.county
        for item in Cities.city_list:
            if county_number == item.county and item.type == 'powiat':
                item_details = [community_number, item]
                return item_details

    @classmethod
    def get_multi_types_objects(cls):
        """
        Check which object has more than 1 type
        :return: list ( contain object with more than 1 type)
        """
        cities = []
        multi_types = []
        for item in Cities.city_list:
            if item.name in cities:
                if item.name not in multi_types:
                    multi_types.append(item.name)
            else:
                cities.append(item.name)
        return multi_types

    @classmethod
    def get_search_items(cls, user_input):
        """
        Search matching words
        :param user_input: fragment or whole word to search
        :return: list with matched words
        """
        search_result = []
        for item in Cities.city_list:
            if user_input in item.name:
                row = [item.name, item.type]
                search_result.append(row)
        if search_result:
            return search_result
        else:
            return False

