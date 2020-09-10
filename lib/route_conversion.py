from typing import List, Dict
import json
import lib.wkt_parser as wkt
import pprint
import random

pp = pprint.PrettyPrinter(indent=4)


def make_color() -> List[int]:
    red = random.randint(50, 256)
    green = random.randint(50, 256)
    blue = random.randint(50, 256)

    if abs(red - green) < 50 or abs(red - blue) < 50 or abs(green - blue) < 50:
        return make_color()

    return [red, green, blue]


def build_route_list(name: str, color: List[int], nodes: List[List[float]], route_list: List[Dict]) -> List[Dict]:

    new_route = {
        "name": name,
        "color": [0, 204, 102],
        "path": nodes
    }

    route_list.append(new_route)

    return route_list


def make_routes() -> None:
    route_list = []
    with open("CerritoPassoDasPedrasFaixaPelotas_gps_nodes.wkt", 'r') as cerrito_pelotas:
        nodes = cerrito_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 0, 0]

    route_list = build_route_list("Cerrito Passo Das Pedras Faixa Pelotas", color, nodes_list, route_list)

    with open("PiratiniPelotas_gps_nodes.wkt", 'r') as piratini_pelotas:
        nodes = piratini_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 255, 0]

    route_list = build_route_list("Piratini Pelotas", color, nodes_list, route_list)

    with open("PiratiniPinheiroMachadoviaJoaoSaraiva_gps_nodes.wkt", 'r') as piratini_saraiva:
        nodes = piratini_saraiva.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 0, 255]

    route_list = build_route_list("Piratini Pinheiro Machadovia Joao Saraiva", color, nodes_list, route_list)

    with open("PelotasPedroOsorioPiratini_gps_nodes.wkt", 'r') as pelotas_piratini:
        nodes = pelotas_piratini.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [150, 0, 150]

    route_list = build_route_list("Pelotas Pedro Osorio Piratini", color, nodes_list, route_list)

    with open("PedroOsorioBage_gps_nodes.wkt", 'r') as pedro_bage:
        nodes = pedro_bage.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 255, 0]

    route_list = build_route_list("Pedro Osorio Bage", color, nodes_list, route_list)

    with open("PedroOsorioPelotas_gps_nodes.wkt", 'r') as pedro_pelotas:
        nodes = pedro_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 255, 255]

    route_list = build_route_list("Pedro Osorio Pelotas", color, nodes_list, route_list)

    with open("JaguaraoPelotas_gps_nodes.wkt", 'r') as jaguarao_pelotas:
        nodes = jaguarao_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 153, 255]

    route_list = build_route_list("Jaguarao Pelotas", color, nodes_list, route_list)

    with open("JaguaraoArroioGrande_gps_nodes.wkt", 'r') as jaguarao_grande:
        nodes = jaguarao_grande.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 255, 255]

    route_list = build_route_list("Jaguarao Arroio Grande", color, nodes_list, route_list)

    with open("HervalArroioGrande_gps_nodes.wkt", 'r') as herval_grande:
        nodes = herval_grande.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [204, 0, 102]

    route_list = build_route_list("Herval Arroio Grande", color, nodes_list, route_list)

    with open("CangucuPelotas_gps_nodes.wkt", 'r') as cangucu_pelotas:
        nodes = cangucu_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [153, 76, 0]

    route_list = build_route_list("Cangucu Pelotas", color, nodes_list, route_list)

    with open("ArroioGrandePelotas_gps_nodes.wkt", 'r') as arroio_pelotas:
        nodes = arroio_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 153, 0]

    route_list = build_route_list("Arroio Grande Pelotas", color, nodes_list, route_list)

    with open("CerritoPedroOsorio_gps_nodes.wkt", 'r') as cerrito_osorio:
        nodes = cerrito_osorio.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [178, 102, 255]

    route_list = build_route_list("Cerrito Pedro Osorio", color, nodes_list, route_list)

    with open("PiratiniCerrito_gps_nodes.wkt", 'r') as piratini_cerrito:
        nodes = piratini_cerrito.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 0, 255]

    route_list = build_route_list("Piratini Cerrito", color, nodes_list, route_list)

    with open("PinheiroMachadoPedrasAltasHervalJaguarao_gps_nodes.wkt", 'r') as pinheiro_jaguarao:
        nodes = pinheiro_jaguarao.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 204, 153]

    route_list = build_route_list("Pinheiro Machado Pedras Altas Herval Jaguarao", color, nodes_list, route_list)

    with open("PinheiroMachadoPedrasAltas_gps_nodes.wkt", 'r') as pinheiro_altas:
        nodes = pinheiro_altas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 128, 0]

    route_list = build_route_list("Pinheiro Machado Pedras Altas", color, nodes_list, route_list)

    with open("PedrasAltasHerval_gps_nodes.wkt", 'r') as pedras_herval:
        nodes = pedras_herval.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [160, 160, 160]

    route_list = build_route_list("Pedras Altas Herval", color, nodes_list, route_list)

    with open("JaguaraoPedroOsorio_gps_nodes.wkt", 'r') as jaguarao_osorio:
        nodes = jaguarao_osorio.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [102, 178, 255]

    route_list = build_route_list("Jaguarao Pedro Osorio", color, nodes_list, route_list)

    with open("HervalPedroOsorio_gps_nodes.wkt", 'r') as herval_osorio:
        nodes = herval_osorio.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 0, 127]

    route_list = build_route_list("Herval Pedro Osorio", color, nodes_list, route_list)

    with open("CangucuPiratini_gps_nodes.wkt", 'r') as cangucu_piratini:
        nodes = cangucu_piratini.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [0, 102, 102]

    route_list = build_route_list("Cangucu Piratini", color, nodes_list, route_list)

    with open("BagePelotas_gps_nodes.wkt", 'r') as bage_pelotas:
        nodes = bage_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [51, 255, 153]

    route_list = build_route_list("Bage Pelotas", color, nodes_list, route_list)

    with open("ArroioGrandePedroOsorio_gps_nodes.wkt", 'r') as arroio_osorio:
        nodes = arroio_osorio.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [255, 102, 102]

    route_list = build_route_list("Arroio Grande Pedro Osorio", color, nodes_list, route_list)

    with open("BagePedroOsorioArroioGrandeJaguarao_gps_nodes.wkt", 'r') as bage_jaguarao:
        nodes = bage_jaguarao.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [153, 153, 255]

    route_list = build_route_list("Bage Pedro Osorio Arroio Grande Jaguarao", color, nodes_list, route_list)

    with open("BagePiratini_gps_nodes.wkt", 'r') as bage_piratini:
        nodes = bage_piratini.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [153, 0, 0]

    route_list = build_route_list("Bage Piratini", color, nodes_list, route_list)

    with open("BagePinheiroMachadoPelotas_gps_nodes.wkt", 'r') as bage_pinheiro_pelotas:
        nodes = bage_pinheiro_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [102, 0, 51]

    route_list = build_route_list("Bage Pinheiro Machado Pelotas", color, nodes_list, route_list)

    with open("HervalPedroOsorioPelotas_gps_nodes.wkt", 'r') as herval_pelotas:
        nodes = herval_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [102, 102, 0]

    route_list = build_route_list("Herval Pedro Osorio Pelotas", color, nodes_list, route_list)

    with open("HervalArroioGrandePelotas_gps_nodes.wkt", 'r') as herval_arroio_pelotas:
        nodes = herval_arroio_pelotas.read()
        nodes_list = wkt.parse_wkt_route(nodes)
        #color = make_color()
        color = [153, 255, 51]

    route_list = build_route_list("Herval Arroio Grande Pelotas", color, nodes_list, route_list)

    routes_json = json.dumps(route_list, indent=2)

    with open("routes_brazil.json", "w") as file:
        file.write(routes_json)
