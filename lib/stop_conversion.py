from typing import List, Dict
import json
import wkt_parser
import coord_conversion


def build_list(stations: List[List[float]]) -> List[Dict]:
    json_list = []
    for coord in stations:
        new_station = {
            "name": "stop name",
            "address": "nowhere",
            "exits": "1",
            "coordinates": coord
        }
        json_list.append(new_station)

    return json_list


def make_stops() -> None:
    coords_list = coord_conversion.coordinate_list()
    stops = []

    #with open("stations.wkt", 'r') as stations:
    #    stations = stations.readlines()
    #    stations = wkt_parser.parse_wkt_stops(stations)

    with open("cities.wkt", 'r') as cities:
        cities = cities.readlines()
        cities = wkt_parser.parse_wkt_stops(cities)

    for local, gps in coords_list:
        #for station in stations:
        #    if local[0] == station[0] and local[1] == station[1]:
        #        stops.append(gps)
        for city in cities:
            if local[0] == city[0] and local[1] == city[1]:
                stops.append(gps)

    result = build_list(stops)

    stops_json = json.dumps(result, indent=2)

    with open("stops_brazil.json", "w") as file:
        file.write(stops_json)
