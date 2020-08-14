
def parse_wkt(nodes):
    list_to_build = []
    nodes = nodes.strip("LINESTRING ()")
    nodes = nodes.split(',')

    for node in nodes:
        node = node.split()
        node[0] = float(node[0])
        node[1] = float(node[1])
        new_node = [node[1], node[0]]
        list_to_build.append(new_node)

    return list_to_build


def build_list(name, color, nodes, route_list):

    new_route = {
        "name": name,
        "color": [0, 204, 102],
        "path": nodes
    }

    route_list.append(new_route)
    return route_list
