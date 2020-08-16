from typing import List, Tuple
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


def make_trips() -> None:
    final_coords = []
    time_coords_1 = []

    # Reads file with timestamps into program and stores it as a list of tuples.
    with open("local_coordinates_brazil.txt", 'r') as time:
        print("    Reading local coordinates and timestamps...")
        reader = time.readlines()
        for row in reader:
            coords_time = row.split()
            name = coords_time[0]
            x_y_vals = coords_time[1]
            time = coords_time[2]
            tup = (name, x_y_vals, time)
            time_coords_1.append(tup)

    # Reformats the coordinates in time_coords_1 and converts them from strings to numeric values.
    time_coords_2 =[]
    for name, entry, time in time_coords_1:
        time = time.strip(',')
        entry = entry[1:-1]
        entry = entry.split(',')
        entry[0] = float(entry[0])
        entry[1] = float(entry[1])
        float_coords = (entry[0], entry[1])
        new_tuple = (name, float_coords, time)
        time_coords_2.append(new_tuple)

    coords_list = coordinate_list()

    # Makes a list of tuples containing the GPS coordinates and timestamps from the previous two lists. Each tuple contains
    # a name, a set of coordinates and a timestamp.
    print("    Making list of GPS coordinates with timestamps...")
    for name, coords, timestamp in time_coords_2:
        timestamp = float(timestamp)
        x = coords[0]
        y = coords[1]
        for x_y, gps in coords_list:
            x1 = x_y[0]
            y1 = x_y[1]
            if x == x1 and y == y1:
                new = (name, gps, timestamp)
                final_coords.append(new)

    # Makes dictionary out of data from final_coords. Coordinates and timestamps are mapped to vehicle names.
    new_dict = {}
    for name, coords, timestamp in final_coords:
        new_dict[name] = []

    for name, coords, timestamp in final_coords:
        new_entry = (coords, timestamp)
        new_dict[name].append(new_entry)

    # Converts each key-value pair from new_dict into a dictionary and adds each dictionary to a list.
    print("    Making final list of dictionaries...")
    json_list = []
    for key in new_dict.keys():
        new_json = {
            "vendor": 0,
            "path": [],
            "timestamps": []
        }
        for coords, timestamp in new_dict[key]:
            new_json["path"].append(coords)
            new_json["timestamps"].append(timestamp)
        json_list.append(new_json)

    # Writes the list of dictionaries to a JSON file.
    json_file = json.dumps(json_list, indent=2)

    with open("one_trace_brazil.json", "w") as file:
        file.write(json_file)


def coordinate_list() -> List[Tuple]:
    # Reads file with GPS coordinates into program and stores it as a list of tuples.
    coords_list_1 = []
    with open("gps_coordinates_brazil.csv", 'r') as coordinates:
        print("    Making list of local-GPS tuples...")
        splt_char = ','
        n = 2
        c = coordinates.readlines()
        for row in c:
            row = row.replace(" ", "")
            row = row.replace('"', "")
            row = row.replace('\n', "")
            l = row.split(',')
            t = splt_char.join(l[:n]), splt_char.join(l[n:])
            tup = (t[1], t[0])
            coords_list_1.append(tup)

    # Reformat the data and convert it back to numeric values.
    coords_list_2 = []
    for gps, coords in coords_list_1:
        gps = gps[1:-1]
        coords = coords[1:-1]
        gps = gps.split(',')
        coords = coords.split(',')
        gps[0] = float(gps[0])
        gps[1] = float(gps[1])
        coords[0] = float(coords[0])
        coords[1] = float(coords[1])
        new_local_coords = (coords[0], coords[1])
        new_gps_coords = [gps[1], gps[0]]
        new_tuple = (new_local_coords, new_gps_coords)
        coords_list_2.append(new_tuple)

    return coords_list_2
