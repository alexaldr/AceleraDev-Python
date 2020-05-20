from datetime import datetime
import math

MINUTES = 60
FARE = 0.36
RATE = 0.09
START_HOUR = 360
END_HOUR = 1320

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def convert_time_minutes(time):
    return time.hour * MINUTES + time.minute + time.second / MINUTES


def calculate_price(start_time, end_time):
    start_time = datetime.fromtimestamp(start_time)
    end_time = datetime.fromtimestamp(end_time)

    start_time_minutes = convert_time_minutes(start_time)
    end_time_minutes = convert_time_minutes(end_time)

    if end_time_minutes > END_HOUR:
        day = END_HOUR - start_time_minutes
        if day < 0:
            total = FARE
        else:
            total = FARE + (day * RATE)
    elif start_time_minutes < START_HOUR:
        day = end_time_minutes - START_HOUR
        if day < 0:
            total = FARE
        else:
            total = FARE + (day * RATE)
    else:
        total = FARE + (math.floor(end_time_minutes
                                   - start_time_minutes) * RATE)
    return total


def update_records_value(record_list, value):
    for record in record_list:
        if record['source'] == value['source']:
            record['total'] = round(record['total'] + value['total'], 2)
    return record_list


def classify_by_phone_number(records):
    results = []

    for record in records:
        total = round(calculate_price(record['start'], record['end']), 2)
        item = {'source': record['source'], 'total': total}

        if not any(record['source'] == dic['source'] for dic in results):
            results.append(item)
        else:
            update_records_value(results, item)

    return sorted(results, key=lambda result: result['total'], reverse=True)


print(classify_by_phone_number(records))