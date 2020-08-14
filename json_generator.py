from lib import coord_conversion
from lib import route_conversion
from lib import stop_conversion

print("Making trips JSON...")
coord_conversion.make_trips()

print("Making routes JSON...")
route_conversion.make_routes()

print("Making stops JSON...")
stop_conversion.make_stops()

