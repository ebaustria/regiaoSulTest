# -*- coding: utf-8 -*-
from typing import List, Tuple, Set
import csv

WKT_BEGIN_LNSTR = 'LINESTRING ('
WKT_BEGIN_POINT = 'POINT ('
WKT_END = ')'
WKT_CRD_SEP = ' '
WKT_PNT_SEP = ', '
CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'
# what the hack is a fallback duration?
FALLBACK_DURATION = 3

def write_wkt_linestring(coords: List[Tuple[float, float]], file: str, append=False) -> None:
    content = ''
    if append:
        content += '\n\n'
    content += WKT_BEGIN_LNSTR

    for i, c in enumerate(coords):
        content += str(c[0]) + WKT_CRD_SEP + str(c[1])
        if i < len(coords) - 1:
            content += WKT_PNT_SEP

    content += WKT_END

    with open(file, 'a+' if append else 'w+') as fp:
        fp.write(content)

def write_wkt_points(coords: Set[Tuple[float, float]], file: str, append=False):
    content = ''
    if append:
        content += '\n\n'

    for i, c in enumerate(coords):
        content += WKT_BEGIN_POINT
        content += str(c[0]) + WKT_CRD_SEP + str(c[1])
        content += WKT_END
        if i < len(coords) - 1:
            content += '\n\n'

    with open(file, 'a+' if append else 'w+') as fp:
        fp.write(content)


def write_csv_stops(coords: List[Tuple[float, float]], durations: List[int], file: str):
    with open(file, 'w+') as fp:
        w = csv.writer(fp,
                       delimiter=CSV_DELIMITER,
                       quotechar=CSV_QUOTECHAR,
                       quoting=csv.QUOTE_MINIMAL)
        if not durations:
            durations = len(coords) * [FALLBACK_DURATION]
        for i, duration in enumerate(durations):
            c = coords[i]
            # write duration in seconds
            duration_s = 30
            if duration > 0:
                duration_s = duration * 60
            w.writerow([
                '{} {}'.format(c[0], c[1]),
                duration_s
            ])

def write_csv_schedule(schedule: List, file: str):
    with open(file, 'w+') as fp:
        w = csv.writer(fp,
                       delimiter=CSV_DELIMITER,
                       quotechar=CSV_QUOTECHAR,
                       quoting=csv.QUOTE_MINIMAL)
        w.writerows(schedule or [])

def write_local_and_gps(proj, routes):
    main_local_to_gps = []

    for route_name in routes.keys():
        nodes = routes[route_name]['nodes']
        stops = routes[route_name]['stops']

        if route_name == 'JaguaraoArroioGrandePedroOsorioBage':
            new_route_name = 'J.AG.PO.B'
        elif route_name == 'JaguaraoArroioGrandePelotas':
            new_route_name = 'J.AG.Pel'
        elif route_name == 'HervalArroioGrande':
            new_route_name = 'H.AG'
        elif route_name == 'HervalPedroOsorioPelotas':
            new_route_name = 'H.PO.Pel'
        elif route_name == 'HervalArroioGrandePelotas':
            new_route_name = 'H.AG.Pel'
        elif route_name == 'BagePinheiroMachadoPelotas':
            new_route_name = 'B.PM.Pel'
        elif route_name == 'PinheiroMachadoPedrasAltasHervalJaguarao':
            new_route_name = 'PM.PA.H.J'
        elif route_name == 'PelotasPedroOsorioPiratini':
            new_route_name = 'Pel.PO.Pi'
        elif route_name == 'PiratiniPinheiroMachadoviaJoaoSaraiva':
            new_route_name = 'Pi.PM'
        elif route_name == 'CangucuPiratini':
            new_route_name = 'Ca.Pi'
        elif route_name == 'PiratiniPelotas':
            new_route_name = 'Pi.Pel'
        elif route_name == 'CerritoPassoDasPedrasFaixaPelotas':
            new_route_name = 'Ce.Pp.Fa.Pel'
        elif route_name == 'PelotasCangucu':
            new_route_name = 'Pel.Ca'
        else:
            new_route_name = route_name

        for key, value in sorted(proj.local_to_gps.items()):
            if value in nodes or value in stops:
                main_local_to_gps.append((new_route_name, key, value))

    with open('gps_coordinates_brazil3.csv', 'w') as f:
        writer = csv.writer(f)
        for route_name, local, gps in sorted(main_local_to_gps):
            writer.writerow([route_name, local, gps])
