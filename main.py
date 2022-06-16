import json

from src.rangeofnumbers import RangeOfNumbers

if __name__ == '__main__':
    with open("data.json", "r") as file:
        data = json.load(file)

    c = RangeOfNumbers(data["start"], data["end"])
    c.calculate()
    # 0 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
