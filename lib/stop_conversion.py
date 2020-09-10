from typing import List, Dict
import json
import lib.coord_conversion as cc
import lib.wkt_parser as wkt

"""
def parse_wkt_stops(stops: List[str]) -> List[List[float]]:
    result = []

    for row in stops:
        row = row.strip("POINT (")
        row = row.split()
        row[1] = row[1].strip(')')
        lat = float(row[0])
        lon = float(row[1])
        new_entry = [lat, lon]
        result.append(new_entry)

    return result
"""

def build_list(stations: List[List[float]]) -> List[Dict]:
    json_list = []
    for coord in stations:
        new_station = {
            "name": "stop name",
            "coordinates": coord
        }
        json_list.append(new_station)

    return json_list


def make_stops(gps_coordinates: str) -> None:

    stops = []
    coords_list = cc.gps_list(gps_coordinates)

    with open("stations.wkt", 'r') as stations:
        stations = stations.readlines()
        stations = wkt.parse_wkt_stops(stations)

    with open("cities.wkt", 'r') as cities:
        cities = cities.readlines()
        cities = wkt.parse_wkt_stops(cities)

    for local, gps in coords_list:
        for station in stations:
            if local[0] == station[0] and local[1] == station[1]:
                stops.append(gps)
        for city in cities:
            if local[0] == city[0] and local[1] == city[1]:
                stops.append(gps)

    result = build_list(stops)

    stops_json = json.dumps(result, indent=2)

    with open("stops.json", "w") as file:
        file.write(stops_json)
