from score import *
from objects.Line import Line


# creates a greedy solution with two constrains: n tracks with a max duration of
# n minutes and all the stations need to be connected. Returns the generated lines
def greedy1(stations, tracks, num_of_lines, max_duration, num_of_critital_tracks=None):
    lines = []

    start_stations = []
    start_stations.extend(stations_short_con(stations, num_of_lines))

    for station in start_stations:
        route = Line([station])
        while route.get_total_time() <= max_duration:
            station = shortest_station(station).destination
            route.add_station(station)

        route.remove_last_station()
        lines.append(route)

    return get_score(lines, tracks), lines


def greedy2(stations, tracks, num_of_lines, max_duration, num_of_critital_tracks=None):
    lines = []

    start_stations = []
    start_stations.extend(stations_short_con(stations, num_of_lines))

    for station in start_stations:
        used_tracks = []

        temp_station = station
        route = Line([station])

        while (route.get_total_time() <= max_duration):
            connection_list = []

            station = route.stations[-1]

            for key, connection in station.connections.items():
                connection_list.append(connection)

            while True:
                # choose a random destination
                track = shortest_connection(connection_list)

                if track not in used_tracks:
                    # track to the destination isnt already used: ready to go!
                    used_tracks.append(track)
                    break
                elif len(connection_list) == 1:
                    # track is already used but no other possibility
                    break
                else:
                    # track is already used: try again
                    connection_list.remove(track)

            route.add_station(track.destination)

        route.remove_last_station()
        lines.append(route)

    return get_score(lines, tracks), lines

# calculates for provided station, the shortest neighbouring connection
def shortest_station(station):
    lowest_time_con = 0

    for key, track in station.connections.items():
        if lowest_time_con:
            if lowest_time_con.duration > track.duration:
                lowest_time_con = track
        else:
            lowest_time_con = track

    return lowest_time_con

# calculates which of connections has the shortest duration
def shortest_connection(connections):
    lowest_time_con = 0

    for connection in connections:
        if lowest_time_con:
            if lowest_time_con.duration > connection.duration:
                lowest_time_con = connection
        else:
            lowest_time_con = connection

    return lowest_time_con

# creates a list of stations sorted by their shortest connection to a neighbouring station
def stations_short_con(stations, number):
    if not isinstance(number, int):
        raise ValueError("Usage: stations, number (has to be int)")

    routes = []
    sorted_stations = []

    for key, station in stations.items():
        routes.append([station, shortest_station(station).duration])

    routes = sorted(routes, key=lambda route: route[1])

    for route in routes:
        sorted_stations.append(route[0])

    return sorted_stations[:number]


