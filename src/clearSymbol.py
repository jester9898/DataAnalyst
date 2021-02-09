import pandas as pd
import csv
def clearSymbol(dir, file_name, delimiter='', excess_delim='', head=None):
    """
    :param excess_delim: str
    :param delimiter: str
    :param dir: str
    :param file_name: str
    :param head: bool
    :return: Creates new CSV file
    """
    with open(file_name, 'w', newline='') as file_name:
        data = csv.writer(file_name)
        dataset = pd.read_csv(dir, header=head)
        for index, row in dataset.iterrows():
            data.writerow(row[0].replace(excess_delim, '').split(delimiter))

clearSymbol("../data/other/test_bank.csv", "new_dataset.csv", ";", '"', None)
