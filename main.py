import json

from src.rangeofnumbers import RangeOfNumbers
from src.save_information import csv_file

r = RangeOfNumbers.get_increment()


def start_calculate_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    calculate_n_ranges(data['start'], data['ranges_to_calculate'])


def calculate_n_ranges(start: int, ranges_to_calculate: int):
    ran = 0

    while ran < ranges_to_calculate:
        c = RangeOfNumbers(start + ran * r)
        print(c)
        c.calculate()
        ran += 1


def calculate_all_ranges():
    i = 0
    while True:
        c = RangeOfNumbers(i * r)
        print(c)
        c.calculate()
        i += 1


def update_data_json():
    start = 0
    ranges = 100
    try:
        with open("data.json", "r") as f:
            ranges = int(json.load(f)['ranges_to_calculate'])
        with open(f'{csv_file}', "r") as file:
            last_line = file.readlines()[-1]
            start = int(last_line.split(';')[0].split('-')[1])
    except Exception:
        return
    finally:
        json_conf = {
            'start'              : start,
            'ranges_to_calculate': ranges
        }
        with open('data.json', 'w') as f:
            json.dump(json_conf, f, indent=2)


if __name__ == '__main__':
    update_data_json()
    start_calculate_json()
    update_data_json()
