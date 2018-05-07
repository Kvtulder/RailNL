import score
from Line import Line
import df_helper
import helper


# creates a depth-first solution by finding the highest scoring routes for each station.
# already used tracks don't give any points, thereby deterring them
# plus depth_search checks for loops, thereby improving the runtime
# constraints: time limit, number of lines, previously used tracks
def depth_first(stations, tracks, num_of_lines, max_duration):
    best_lines = []
    used_tracks = []

    # keeps track of times depth_search1 function is called, thus a 'note' in the tree is created
    nodes = [0]

    print("Calculating Depth-First3")

    for key, station in stations.items():
        route_start = [station]

        best_line = depth_search(route_start, max_duration, tracks, nodes, used_tracks)

        if not best_line:
            best_line = Line(route_start)
        else:
            helper.update_used(best_line, tracks, used_tracks)

        best_lines.append(best_line)

        # print the results for individual lines
        df_helper.print_line_results(best_line, best_lines, nodes, tracks, stations)

    best_lines = helper.select_best_lines(best_lines, num_of_lines, tracks)

    total_lines_score = score.get_score(best_lines, tracks)

    print("Total Nodes: ", nodes)

    return total_lines_score, best_lines


# recursively looks for the best route of given station
# by looking at looking at scores of potential routes
# to neighbouring stations and their neighbours
# checks for loops, which improves runtime
def depth_search(route_so_far, max_duration, tracks, nodes, used_tracks):
    best_line = None
    nodes[0] += 1

    cur_route = list(route_so_far)
    cur_station = route_so_far[-1]

    for key, connection in cur_station.connections.items():

        if not df_helper.check_loop(cur_route, connection.destination):
            new_route = list(cur_route)
            new_route.append(connection.destination)

            temp_line = Line(new_route)

            if temp_line.get_total_time() > max_duration:
                temp_line.remove_last_station()
                return temp_line
            else:
                new_line = depth_search(new_route, max_duration, tracks, nodes, used_tracks)

            best_line = df_helper.update_best_line(best_line, new_line, tracks, used_tracks)

    return best_line
