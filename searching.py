import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    r'"V:\BPC-PRG\lecture09\lecture_searching\sequential.json"'
    with open(file_name) as file:
        data = json.load(file)
    if field not in data.keys():
        return None
    return data[field]

def linear_search(sequential_data, wanted_number):
    indexes = []
    for pozice, number in enumerate(sequential_data):
        if number == wanted_number:
            indexes.append(pozice)
    searched = {}
    searched["positions"] = indexes
    searched["count"] = len(indexes)
    return searched

def pattern_search(sequential_data, wanted_pattern):
    n = len(sequential_data)
    m = len(wanted_pattern)
    positions = set()
    for i in range(n - (m - 1)):
        subseq = sequential_data[i:i+m]
        if subseq == wanted_pattern:
            positions.add(i)
    return positions


def main():
    sequential_data = read_data("sequential.json", "dna_sequence")
    # number_in_sequence = linear_search(sequential_data, 0)
    print(pattern_search(sequential_data, "ATA"))
    return sequential_data



if __name__ == '__main__':
    print(main())
