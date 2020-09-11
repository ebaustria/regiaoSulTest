# regiaoSul
A set of files for visualizing long-distance simulations from The-ONE

### Requirements
* Python 3.4+

### Getting Started
Clone the necessary repositories:

```
git clone https://github.com/ebaustria/regiaoSul.git
git clone https://github.com/ebaustria/deck.gl.git
git clone https://github.com/ebaustria/the-one.git
```

Navigate to the-one and switch to the correct branch:

```
cd the-one
git checkout longDistance
```

**Note**: Make sure that ```Report.report1``` on line 105 of ```the-one/default_settings.txt``` is set to ```LocalCoordinatesReport```. 

Compile the code and run the simulation:

```
./compile.sh
./one.sh regiaoSul_settings.txt
```

**Note**: If you are using Java 11, you will need to compile the program with ```./compileJava11.sh```. ```the-one/README.txt``` or ```the-one/README.md``` can be consulted for more information on compiling and running the-ONE, if necessary. It may be necessary to remove the flight recorder in order to run the simulation. If this is the case, open ```the-one/one.sh``` and remove ```-XX:+FlightRecorder  -XX:StartFlightRecording=duration=60s,filename=myrecording.jfr ``` from the file. Afterwards, it should work. When the simulation is finished, it will write a report. Each line of the report has the following form: vehicle name, local coordinates, timestamp. The vehicle name is the name of the vehicle in question, the local coordinates are a pair of local coordinates used in the ONE, and the timestamp is the simulation time at which the vehicle is located at the local coordinates in question.

Open ```the-one/reports```. Find the aforementioned report. It should be the most recent report and its name should end with ```LocalCoordinatesReport.txt```. If it is your first time running the simulation, it will be the only file in ```the-one/reports```. Rename the report as ```local_coordinates_brazil.txt```. Move this file to the ```regiaoSul``` repository.

Next, open ```the-one/data/regiaoSul```. Find ```stations.wkt``` and ```cities.wkt``` and copy them to the ```regiaoSul``` repository. Do not change the name of either file.

Navigate to ```regiaoSul```, create a virtual environment, and install the required dependencies:

```
cd ..
cd regiaoSul
python3 -m venv --without-pip .venv
curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
source .venv/bin/activate
pip install -r requirements.txt
```

### Creating JSON Files:
Run ```readMap.py```:

```
python3 -m readMap
```

On line 136, ```readMap.py``` writes a file called ```gps_coordinates_brazil.csv```. This file is a mapping of the local coordinates of each node (used in the ONE and taken from ```local_coordinates_brazil.txt```) to that node's corresponding GPS coordinates. Running ```readMap.py``` also writes a WKT linestring file for each route that consists of GPS coordinates. These files are written on line 132. The WKT linestring file names have the format ```route_name + _gps_nodes.wkt```.

Run ```json_generator.py```:

```
python3 -m json_generator
```

The first function call in ```json_generator.py``` reads ```local_coordinates_brazil.txt``` and ```gps_coordinates_brazil.csv```, parses the data in each file, and uses it to build a list of dictionaries that each contain a list of GPS coordinates and a list of corresponding timestamps for a vehicle. This list of dictionaries is then written to a JSON file called ```trips.json``` that can be used to visualize vehicle movement in deck.gl. The second function call in ```json_generator.py``` reads in each of the WKT linestring files, parses the data in them, and creates a list of dictionaries that each contain a route name, a color, and a list of the route's GPS coordinates in linestring form. This list is then written to a JSON file called ```routes_brazil.json``` that can be used to visualize the public transit lines in deck.gl. The third function call in ```json_generator.py``` reads ```stations.wkt``` and ```cities.wkt```, parses the data in each file, and builds a list of dictionaries that each contain a single pair of GPS coordinates. This list is then written to a JSON file called ```stops.json``` that can be used to visualize public transit stops in deck.gl. The third function call reads ```arrivals.txt``` (includes timestamps for when vehicles arrive at stops in the ONE) and ```gps_coordinates_brazil.csv```, parses the data in each file, and builds a list of dictionaries. Each dictionary contains a vehicle name, a set of coordinates, a single timestamp, and a color (RGB format). The list is written to a file called ```arrivals.json```, which is used to visualize the arrivals of vehicles at public transit stops in deck.gl.

### Visualizing the Data
Create a remote repository and add it if you haven't already. Stage the four JSON files from the previous section to be committed, commit them, and push them to your remote:

<pre>
git remote add <i>remote_name</i> https://github.com/<i>user</i>/<i>repo</i>.git
git add trips.json
git add routes_brazil.json
git add stops.json
git add arrivals.json
git commit -m "<i>message</i>"
git push <i>remote_name</i> master
</pre>

Open ```deck.gl/examples/website/trips/app.js```. Open the raw data for each JSON file in the remote GitHub repository from the previous step and assign each raw data URL to a variable in the ```DATA_URL``` constant in ```app.js```. The properties of each layer will also need to be included in the ```renderLayers()``` function in ```app.js```. The current version of ```app.js``` is located in the ```regiaoSul``` repository and can be consulted for an example. https://deck.gl/docs/api-reference/layers can also be consulted for more information on deck.gl's layers and their properties.

**Note**: If you would like to do a simpler version of this step, you should be able to navigate to ```deck.gl/examples/website/trips``` and replace the version of ```app.js``` that is located there with the version of ```app.js``` that is located in ```regiaoSul```.

Navigate to ```deck.gl/examples/website/trips```, install the dependencies, and run the visualization:

```
cd ..
cd deck.gl/examples/website/trips
npm install
npm start
```

https://deck.gl/docs can be consulted for more information, if necessary.

### License
This code is licensed under the MIT license.
