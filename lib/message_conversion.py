import coord_conversion
import json


def make_received(local_coordinates: str, gps_coordinates: str):
    dict_list = []

    received_timestamps = coord_conversion.timestamps_list(local_coordinates)
    received_gps = coord_conversion.gps_list(gps_coordinates)
    received_final_coords = coord_conversion.final_list(received_timestamps, received_gps)

    for name, gps, timestamp in received_final_coords:
        new_dict = {}
        new_dict["name"] = name
        new_dict["coordinates"] = gps
        new_dict["timestamp"] = timestamp
        new_dict["notification"] = "receiving message"

        dict_list.append(new_dict)

    json_file = json.dumps(dict_list, indent=2)

    with open("received_messages.json", "w") as file:
        file.write(json_file)
