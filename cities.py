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
