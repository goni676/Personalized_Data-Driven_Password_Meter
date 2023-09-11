import decimal
import os
import pandas as pd
import BS  # Import the BS module or replace with the appropriate import for BS
import numpy as np

def load_data(file_path):
    """
    Load and parse data from a file into a list of tuples.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().rsplit(' ', 1)
            if len(parts) == 2:
                word = parts[0].strip('"')
                value = float(parts[1])
            if len(parts) == 1:
                word = ""
                value = float(parts[0])
            data.append((word, value))
    return data


def n_most_popular(data, n):
    """
    Get the top n most popular items from the data.
    """
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)[:int(n)]
    sorted_ascii = sorted(sorted_data, key=lambda x: x[0])
    return sorted_ascii


def calc_tweak(file_path_general, file_path_country, top_country_path, n):
    most_popular = n_most_popular(load_data(file_path_country), n)
    product = 1
    with open(top_country_path, 'w') as file:
        for item in most_popular:
            word = item[0]
            pp = item[1]
            print(word, pp)
            pp0 = BS.main(file_path_general, word)
            if pp0 is not None:
                pp0 = float(pp0)
                product *= (1-(pp-pp0))
            else:
                product *= (1 - pp)
            file.write(f'{item[0]} {item[1]}\n')
    return product


def main_tweaking():
    countries = ["china"]
    main_path = os.getcwd()
    tests = ["100", "500", "1000", "5000"]
    tweak_dict = {}  # Dictionary to store DataFrames
    for country in countries:
        country_dict = {}
        for n in tests:
            country_dict[n] = {'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}
            for i in range(1, 6):
                curr_sub = f"a{i}"
                origin_path = os.path.join(main_path, f"{curr_sub}.txt")
                country_path = os.path.join(main_path, f"{country}_{i}.txt")
                top_country_path = os.path.join(os.getcwd(), f"{country}{i}_{n}.txt")
                curr_tweak = calc_tweak(origin_path, country_path, top_country_path, n)
                country_dict[n][curr_sub] = float(curr_tweak)
        tweak_dict[country] = country_dict
    return tweak_dict


if __name__ == "__main__":
    result = main_tweaking()
    print(result)


