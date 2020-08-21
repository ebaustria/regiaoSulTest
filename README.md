# regiaoSul
files for long distance simulation of The-ONE

Steps for creating a deck.gl visualization:

1. Clone this repository.

2. Clone the repository located at https://github.com/visgl/deck.gl.

3. Clone the repository located at https://github.com/ebaustria/the-one/tree/longDistance.

4. Open the-one/default_settings.txt. Scroll down to line 105 and make sure Report.report1 is set to LocalCoordinatesReport.

5. Navigate to the-one and run the simulation. When the simulation is finished, it will write a report. Each line of the report has the following form: vehicle name, local coordinates, timestamp. The vehicle name is the name of the vehicle in question, the local coordinates are a pair of coordinates used in the ONE, and the timestamp is the simulation time at which the vehicle is located at the local coordinates in question.

6. Navigate to the-one/reports. Find the report mentioned in the previous step. It should be the most recent report and its name should end with LocalCoordinatesReport.txt. Rename the report as "local_coordinates_brazil.txt". Move this file to the "regiaoSul" repository. Overwrite the file in regiaoSul if it is already present in the repository.

7. Navigate to the-one/data/regiaoSul. Find "stations.wkt" and "cities.wkt" and copy them to the "regiaoSul" repository, again overwriting them if they are already present in the repository. Navigate to that repository.

8. Run readMap.py. On line 136 of readMap.py, this will write a file called "gps_coordinates_brazil.csv". "gps_coordinates_brazil.csv" is a mapping of the local coordinates of each node (used in the ONE) to that node's corresponding GPS coordinates. The GPS coordinates are needed for the deck visualization. Running readMap.py also writes a WKT linestring file for each route that consists of GPS coordinates. These files are written on line 132 within a for loop. The WKT linestring file names have the format route_name + "_gps_nodes.wkt".

9. Run json_generator.py. No command line arguments are needed. The first function call in json_generator.py reads "local_coordinates_brazil.txt" and "gps_coordinates_brazil.csv", parses the data in each file, and uses it to build a list of dictionaries that each contain a list of GPS coordinates and a list of corresponding timestamps for a vehicle. This list of dictionaries is then written to a JSON file called "one_trace_brazil.json" that can be used to visualize vehicle movement in deck.gl. The second function call in json_generator.py reads in each of the WKT linestring files, parses the data in them, and creates a list of dictionaries that each contain a route name, a color, and a list of the route's GPS coordinates in linestring form. This list is then written to a JSON file called "routes_brazil.json" that can be used to visualize the public transit lines in deck.gl. The third function call in json_generator.py reads "stations.wkt" and "cities.wkt", parses the data in each file, and builds a list of dictionaries that each contain a single pair of GPS coordinates. This list is then written to a JSON file called "stops_brazil.json" that can be used to visualize public transit stops in deck.gl.

10. Push the three JSON files to a remote GitHub repository. Open the raw data for each JSON file in the remote GitHub repository and copy its URL to the DATA_URL constant in app.js. The properties of each layer will also need to be included in the renderLayers() function in app.js. The current version of app.js is located in the regiaoSul repository and can be consulted for an example. If you would like to skip this step, you should be able to navigate to deck.gl/examples/website/trips and replace the version of app.js that is located there with the version of app.js that is located in regiaoSul.

11. Navigate to deck.gl/examples/website/trips and run the visualization using npm start.
