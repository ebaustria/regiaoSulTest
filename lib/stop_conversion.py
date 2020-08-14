import json


def build_list(stations):
    json_list = []
    for line, coord in stations:
        new_station = {
            "name": "stop name",
            "address": "nowhere",
            "exits": "1",
            "coordinates": coord
        }
        json_list.append(new_station)
    return json_list


def make_stops():
    line_stops_1 = []
    with open("gps_stops_brazil.csv", 'r') as stops:
        reader = stops.readlines()
        for row in reader:
            route_stops = row.split('[')
            route_stops[0] = route_stops[0].strip(',"')
            route_stops[1] = route_stops[1].strip(']"\n')
            route_stops[1] = route_stops[1].split('), (')

            new_entry = (route_stops[0], route_stops[1])
            line_stops_1.append(new_entry)

    line_stops_2 = []
    for route, stops in line_stops_1:
        for stop in stops:
            stop = stop.strip('()')
            stop = stop.split(', ')
            stop[0] = float(stop[0])
            stop[1] = float(stop[1])
            new_stop = [stop[1], stop[0]]
            new_entry = (route, new_stop)
            line_stops_2.append(new_entry)

    result = build_list(line_stops_2)

    stops_json = json.dumps(result, indent=2)

    with open("stops_brazil.json", "w") as file:
        file.write(stops_json)

