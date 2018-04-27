from score import *
from Line import *


# creates a depth-first solution by finding the highest scoring routes for each station
# constraints: time limit, number of lines
def depth_first1(stations, tracks, num_of_lines, max_duration):
    tracks_calculated = 0
    lines = []

    for key, station in stations.items():
        line_route = [station]

        route = depth_search1(station, line_route, max_duration, tracks)

        lines.append((Line(route[1]), route[0]))

        tracks_calculated += 1

        print("tracks calculated: ",tracks_calculated)

    best_lines = update_best_line(lines, num_of_lines)

    score = get_score(best_lines, tracks)

    return score, best_lines

# similiar to depth_first1 in finding a solution but routes can't use previously used tracks
# constraints: time limit, number of lines, previously used tracks
def depth_first2(stations, tracks, num_of_lines, max_duration):
    lines_and_scores = []
    used_tracks = {}

    # keeps track of times depth_search1 function is called, thus a 'note' in the tree is created
    nodes = [0]

    print("Calculating Depth-First2")

    for key, station in stations.items():
        route_start = [station]

        best_line = depth_search1(route_start, max_duration, tracks, nodes, used_tracks)

        if not best_line:
            best_line_score = 0
        else:
            best_line_score = get_score(best_line, tracks, used_tracks)
            update_used_tracks(best_line, used_tracks, tracks)

        lines_and_scores.append([best_line, best_line_score])

        # print the results for individual lines
        print_line_results(best_line, lines_and_scores, nodes, tracks, stations)

    best_lines = select_best_lines(lines_and_scores, num_of_lines)

    total_lines_score = get_score(best_lines, tracks)

    print("Total Nodes: ", nodes)

    return total_lines_score, best_lines


# similiar to depth_first2 in finding a solution with routes can't use previously used tracks
# uses depth_search2 instead of 1, this drastically reduces calculation time (see nodes)
# constraints: time limit, number of lines, previously used tracks
def depth_first3(stations, tracks, num_of_lines, max_duration):
    lines_and_scores = []
    used_tracks = {}

    # keeps track of times depth_search1 function is called, thus a 'note' in the tree is created
    nodes = [0]

    print("Calculating Depth-First3")

    for key, station in stations.items():
        route_start = [station]

        best_line = depth_search2(route_start, max_duration, tracks, nodes, used_tracks)

        if not best_line:
            best_line_score = 0
        else:
            best_line_score = get_score(best_line, tracks, used_tracks)
            update_used_tracks(best_line, used_tracks, tracks)

        lines_and_scores.append([best_line, best_line_score])

        # print the results for individual lines
        print_line_results(best_line, lines_and_scores, nodes, tracks, stations)

    best_lines = select_best_lines(lines_and_scores, num_of_lines)

    total_lines_score = get_score(best_lines, tracks)

    print("Total Nodes: ", nodes)

    return total_lines_score, best_lines


# recursively looks for the best route of given station
def depth_search1(route_so_far, max_duration, tracks, nodes, used_tracks=[]):
    best_line = None
    nodes[0] += 1

    cur_route = list(route_so_far)
    cur_station = route_so_far[-1]

    for key ,connection in cur_station.connections.items():
        new_route = list(cur_route)
        new_route.append(connection.destination)

        temp_line = Line(new_route)

        if temp_line.get_total_time() > max_duration:
            temp_line.remove_last_station()
            return temp_line
        else:
            new_line = depth_search1(new_route, max_duration, tracks, nodes, used_tracks)

        best_line = update_best_line(best_line, new_line, tracks)

    return best_line


# recursively looks for the best route of given station
# by looking at looking at scores of potential routes
# to neighbouring stations and their neighbours
def depth_search2(route_so_far, max_duration, tracks, nodes, used_tracks):
    best_line = None
    nodes[0] += 1

    cur_route = list(route_so_far)
    cur_station = route_so_far[-1]

    for key ,connection in cur_station.connections.items():

        if not check_loop(cur_route, connection.destination):
            new_route = list(cur_route)
            new_route.append(connection.destination)

            temp_line = Line(new_route)

            if temp_line.get_total_time() > max_duration:
                temp_line.remove_last_station()
                return temp_line
            else:
                new_line = depth_search2(new_route, max_duration, tracks, nodes, used_tracks)

            best_line = update_best_line(best_line, new_line, tracks, used_tracks)

    return best_line

def check_loop(cur_route, cur_station):
    times = 0

    if len(cur_route) > 2:
        if (cur_route[-1], cur_station) == (cur_route[-3], cur_route[-2]):
            times += 1
        elif((cur_station, cur_route[-1]) == (cur_route[-3], cur_route[-2])):
            times += 1

    if times > 0 and len(cur_route[-1].connections) > 1:
        return True
    else:
        return False


def print_line_results(line, lines_and_scores, nodes, tracks, stations):
    tracks_calculated = len(lines_and_scores) - 1
    line_score = lines_and_scores[-1][1]

    print(tracks_calculated, "out of", len(stations), "tracks calculated: ")

    if line:
        for station in line.stations:
            print(station.name, ",", end=' ')
    else:
        print("No route could be found")
    print("")

    print("Score: ", line_score)
    print("Nodes: ", nodes)


# returns a max given number of routes based on their scores
def select_best_lines(lines, number):
    sort_lines = sorted(lines, key=lambda lines: lines[1], reverse=True)

    sorted_list = []

    for line in sort_lines:
        if line[1] > 0 and len(sorted_list) <= number:
            sorted_list.append(line[0])

    return sorted_list


# updates best line by checking if new line is higher
def update_best_line(best_line, new_line, tracks, used_tracks=[]):
    if not best_line:
        best_line = new_line
    elif new_line:

        score_best_line = get_score(best_line, tracks, used_tracks)
        score_new_line = get_score(new_line, tracks, used_tracks)

        if score_best_line < score_new_line:
            best_line = new_line

    return best_line


# updates the used track dict
def update_used_tracks(line, used_tracks, tracks):
    for i in range (len(line.stations) - 1):
        current_station = line.stations[i]
        destination = line.stations[i + 1]

        key1 = "{}-{}".format(current_station.name, destination.name)
        key2 = "{}-{}".format(destination.name, current_station.name)

        if key1 in tracks:
            if key1 not in used_tracks and tracks[key1].critical:
                used_tracks.update({key1: tracks[key1]})
        elif key2 in tracks:
            if key2 not in used_tracks and tracks[key2].critical:
                used_tracks.update({key2: tracks[key2]})

