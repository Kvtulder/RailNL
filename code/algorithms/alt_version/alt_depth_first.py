import score
import Line
import df_helper


# creates a depth-first solution by finding the highest scoring routes for each station
# constraints: time limit, number of lines
def alt_depth_first1(stations, tracks, num_of_lines, max_duration):
    tracks_calculated = 0
    lines = []

    for key, station in stations.items():
        line_route = [station]

        route = df_helper.alt_depth_search1(station, line_route, max_duration, tracks)

        lines.append((Line(route[1]), route[0]))

        tracks_calculated += 1

        print("tracks calculated: ", tracks_calculated)

    best_lines = df_helper.update_best_line(lines, num_of_lines)

    total_score = score.get_score(best_lines, tracks)

    return total_score, best_lines


# similiar to depth_first1 in finding a solution but routes can't use previously used tracks
# constraints: time limit, number of lines, previously used tracks
def alt_depth_first2(stations, tracks, num_of_lines, max_duration):
    lines_and_scores = []
    used_tracks = {}

    # keeps track of times alt_depth_search1 function is called, thus a 'note' in the tree is created
    nodes = [0]

    print("Calculating Depth-First2")

    for key, station in stations.items():
        route_start = [station]

        best_line = df_helper.alt_depth_search1(route_start, max_duration, tracks, nodes, used_tracks)

        if not best_line:
            best_line_score = 0
        else:
            best_line_score = score.get_score(best_line, tracks, used_tracks)
            df_helper.update_used_tracks(best_line, used_tracks, tracks)

        lines_and_scores.append([best_line, best_line_score])

        # print the results for individual lines
        df_helper.print_line_results(best_line, lines_and_scores, nodes, tracks, stations)

    best_lines = df_helper.select_best_lines(lines_and_scores, num_of_lines)

    total_lines_score = score.get_score(best_lines, tracks)

    print("Total Nodes: ", nodes)

    return total_lines_score, best_lines


# recursively looks for the best route of given station
def alt_alt_depth_search1(route_so_far, max_duration, tracks, nodes, used_tracks=[]):
    best_line = None
    nodes[0] += 1

    cur_route = list(route_so_far)
    cur_station = route_so_far[-1]

    for key, connection in cur_station.connections.items():
        new_route = list(cur_route)
        new_route.append(connection.destination)

        temp_line = Line(new_route)

        if temp_line.get_total_time() > max_duration:
            temp_line.remove_last_station()
            return temp_line
        else:
            new_line = df_helper.alt_depth_search1(new_route, max_duration, tracks, nodes, used_tracks)

        best_line = df_helper.update_best_line(best_line, new_line, tracks)

    return best_line
