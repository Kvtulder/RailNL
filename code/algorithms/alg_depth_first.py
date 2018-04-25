from score import *
from Line import *


# creates a depth-first solution by finding the highest scoring routes for each station
# constraints: time limit, number of lines
def depth_first1(stations, tracks, num_of_lines, max_duration):
    tracks_calculated = 0
    lines = []

    for key, station in stations.items():
        line_route = [station]

        route = depth_search(station, line_route, max_duration, tracks)

        lines.append((Line(route[1]), route[0]))

        tracks_calculated += 1

        print("tracks calculated: ",tracks_calculated)

    best_lines = best_combination(lines, num_of_lines)

    score = get_score(best_lines, tracks)

    return score, best_lines

# similiar to depth_first1 in finding a solution but routes can't use previously used tracks
# constraints: time limit, number of lines, previously used tracks
def depth_first2(stations, tracks, num_of_lines, max_duration):
    lines = []
    used_tracks = {}

    tracks_calculated = 0

    for key, station in stations.items():
        line_route = [station]

        route = depth_search(station, line_route, max_duration, tracks, used_tracks)

        lines.append((Line(route[1]), route[0]))
        update_used_tracks(route[1], used_tracks, tracks)

        tracks_calculated += 1

        print(tracks_calculated, "out of", len(stations), "tracks calculated: ",route)

    best_lines = best_combination(lines, num_of_lines)

    score = get_score(best_lines, tracks)

    return score, best_lines


# recursively looks for the best route of given station
## TO-DO REMOVING NECESSITY OF BOTH LINE AND STATION
def depth_search(station, line, max_duration, tracks, used_tracks=[]):

    best_route = (0,0)

    cur_line = list(line)
    temp_line = Line(line)

    for key, connection in station.connections.items():
        lines = []

        temp_line.add_station(connection.destination)

        if temp_line.get_total_time() > max_duration:

            temp_line.remove_last_station()
            lines.append(temp_line)

            return get_score(lines, tracks, used_tracks), cur_line
        else:

            cur_line.append(connection.destination)

            new_line = depth_search(connection.destination, cur_line, max_duration, tracks, used_tracks)


        cur_line = cur_line[:-1]
        temp_line.remove_last_station()

        if best_route == (0, 0):
            best_route = new_line
        elif best_route[0] < new_line[0]:
            best_route = new_line


    return best_route


# returns number of found routes sorted by their score
def best_combination(lines, number):
    sort_lines = sorted(lines, key=lambda lines: lines[1], reverse=True)

    sorted_list = []

    for line in sort_lines:
        if line[1] > 0 and len(sorted_list) <= number:
            sorted_list.append(line[0])

    return sorted_list

# updates the used track dict
def update_used_tracks(route, used_tracks, tracks):
    for i in range (len(route) - 1):
        current_station = route[i]
        destination = route[i + 1]

        key1 = "{}-{}".format(current_station.name, destination.name)
        key2 = "{}-{}".format(destination.name, current_station.name)

        if key1 in tracks:
            if key1 not in used_tracks and tracks[key1].critical:
                used_tracks.update({key1: tracks[key1]})
        elif key2 in tracks:
            if key2 not in used_tracks and tracks[key2].critical:
                used_tracks.update({key2: tracks[key2]})





