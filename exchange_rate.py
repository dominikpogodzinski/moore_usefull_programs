from operator import itemgetter
from datetime import datetime

rates = [
    {"date": "2019-11-02", "rate": 4.3422},
    {"date": "2019-11-03", "rate": 4.2210},
    {"date": "2019-11-04", "rate": 4.3455},
    {"date": "2019-11-05", "rate": 4.3456},
    {"date": "2019-11-06", "rate": 4.2311}
]
date_range = ["2019-11-03", "2019-11-05"]


def filter(range: list, rates: list) -> list:
    data_range = [datetime(*[int(x) for x in date.split('-')]) for date in range]
    return [dictio for dictio in rates
            if max(data_range) >= datetime(*[int(x) for x in dictio['date'].split('-')]) >= min(data_range)]


new_list = sorted(filter(date_range, rates), key=itemgetter('rate'))
output1 = {"min": new_list[0]}
output2 = {"max": new_list[-1]}

print(output1)
print(output2)
