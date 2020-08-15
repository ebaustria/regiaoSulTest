# regiaoSul
files for long distance simulation of The-ONE

Steps for creating a deck.gl visualization:

1. Open default_settings.txt. Make sure Report.report1 is set to LocalCoordinatesReport (line 105).

2. Run the ONE. When the simulation is finished, it will write a report. Each line of the report has the following form: vehicle name, local coordinates, timestamp. The vehicle name is the name of the vehicle in question, the local coordinates are a pair of coordinates used in the ONE, and the timestamp is the simulation time at which the vehicle is located at the local coordinates in question.

3. Find the report and rename it as "local_coordinates_brazil.txt". Move this file to the "regiaoSul" repository and navigate to that repository.

4. Run readMap.py. On lines 136 and 137 of readMap.py, this will write a file called "gps_coordinates_brazil.csv" and a file called "gps_stops_brazil.csv". "gps_coordinates_brazil.csv" is a mapping of the local coordinates of each node (used in the ONE) to that node's corresponding GPS coordinates. "gps_stops_brazil.csv" is a mapping of each route name to the stops on that route. The stops are in GPS form. Running readMap.py also writes a WKT linestring file for each route that consists of GPS coordinates. These files are written on line 132. The WKT linestring file names have the format route_name + "_gps_nodes.wkt".

5. Run json_generator.py. No command line arguments are needed. The first function call in json_generator.py reads "local_coordinates_brazil.txt" and "gps_coordinates_brazil.csv", parses the data in each file, and uses it to build a list of dictionaries that each contain a list of GPS coordinates and a list of corresponding timestamps for a vehicle. This list of dictionaries is then written to a JSON file called "one_trace_brazil.json" that can be used to visualize vehicle movement in deck.gl. The second function call in json_generator.py reads in each of the WKT linestring files, parses the data in them, and creates a list of dictionaries that each contain a route name, a color, and a list of the route's GPS coordinates in linestring form. This list is then written to a JSON file called "routes_brazil.json" that can be used to visualize the transit lines in deck.gl. The third function call in json_generator.py reads "gps_stops_brazil.csv", parses the data in it, and builds a list of dictionaries that each contain a single pair of GPS coordinates. This list is then written to a JSON file called "stops_brazil.json" that can be used to visualize transit stops in deck.gl.

6. Push the three JSON files to the remote GitHub repository. Open the raw data for each file and copy its URL to the DATA_URL constant in app.js. The properties of each layer will also need to be included in the _renderLayers() function in app.js. The current version of app.js is located in this repository and can be consulted for an example.

7. Navigate to the repository being used to launch deck.gl and run the visualization using npm start.
