from score import *
from Line import Line
from Environment import Environment


# creates a greedy solution with two constrains: n tracks with a max duration of
# n minutes and all the stations need to be connected. Returns the generated lines and score.
def greedy1(stations, tracks, num_of_lines, max_duration, num_of_critital_tracks=None):
    lines = []

    start_stations = []
    start_stations.extend(stations_short_con(stations, num_of_lines))

    for station in start_stations:
        route = Line([station])
        while route.get_total_time() <= max_duration:
            station = shortest_connection(station.connections).destination
            route.add_station(station)

        route.remove_last_station()
        lines.append(route)

    return get_score(lines, tracks), lines

# similar to greedy1 but with an extra constraint: line cant travel back to previously traveled track
def greedy2(stations, tracks, num_of_lines, max_duration, num_of_critital_tracks=None):
    lines = []

    start_stations = []
    start_stations.extend(stations_short_con(stations, num_of_lines))

    for station in start_stations:
        used_tracks = []

        route = Line([station])

        while route.get_total_time() <= max_duration:
            station = route.stations[-1]
            connections = {**station.connections}

            while True:
                # choose a random destination
                track = shortest_connection(connections)

                if track not in used_tracks:
                    # track to the destination isnt already used: ready to go!
                    used_tracks.append(track)
                    break
                elif len(connections) == 1:
                    # track is already used but no other possibility
                    break
                else:
                    # track is already used: try again
                    del(connections[track.destination.name])

            route.add_station(track.destination)

        route.remove_last_station()
        lines.append(route)

    return get_score(lines, tracks), lines


# calculates which of connections has the shortest duration
def shortest_connection(connections):
    lowest_time_con = 0

    for key, connection in connections.items():
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
        routes.append([station, shortest_connection(station.connections).duration])

    routes = sorted(routes, key=lambda route: route[1])

    for route in routes:
        sorted_stations.append(route[0])

    return sorted_stations[:number]


