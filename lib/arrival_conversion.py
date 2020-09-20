import lib.coord_conversion as cc
import json


def make_arrivals(local_coordinates: str, gps_coordinates: str):
    dict_list = []

    arrivals_timestamps = cc.timestamps_list(local_coordinates)
    arrivals_gps = cc.gps_list(gps_coordinates)
    arrivals_final_coords = cc.final_list(arrivals_timestamps, arrivals_gps)

    for name, gps, timestamp, messages in arrivals_final_coords:
        new_dict = {}
        new_dict["name"] = name
        new_dict["coordinates"] = gps
        new_dict["timestamp"] = timestamp
        new_dict["color"] = [253, 128, 93]

        dict_list.append(new_dict)

    json_file = json.dumps(dict_list, indent=2)

    with open("arrivals.json", "w") as file:
        file.write(json_file)
