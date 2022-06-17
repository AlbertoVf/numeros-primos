import json

from src.rangeofnumbers import RangeOfNumbers

r = RangeOfNumbers.get_increment()


def start_calculate_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    calculate_n_ranges(data['start'], data['ranges_to_calculate'])


def calculate_n_ranges(start: int, ranges_to_calculate: int):
    for i in range(start, ranges_to_calculate + start):
        c = RangeOfNumbers(i * r)
        print(c)
        c.calculate()


def calculate_all_ranges():
    i = 0
    while True:
        c = RangeOfNumbers(i * r)
        print(c)
        c.calculate()
        i += 1


if __name__ == '__main__':
    start_calculate_json()
