import score

# checks if current and next station would for duo that have occured before
def check_loop(cur_route, cur_station):
    times = 0

    if len(cur_route) > 2:
        if (cur_route[-1], cur_station) == (cur_route[-3], cur_route[-2]):
            times += 1
        elif(cur_station, cur_route[-1]) == (cur_route[-3], cur_route[-2]):
            times += 1

    if times > 0 and len(cur_route[-1].connections) > 1:
        return True
    else:
        return False


# print information about how many lines of total have been calculated
# plus information about score and nodes
def print_line_results(line, best_lines, nodes, tracks, stations):
    tracks_calculated = len(best_lines) - 1
    line_score = score.get_score(line,tracks)

    print(tracks_calculated, "out of", len(stations), "tracks calculated: ")

    if line:
        for station in line.stations:
            print(station.name, ",", end=' ')
    else:
        print("No route could be found")
    print("")

    print("Score: ", line_score)
    print("Nodes: ", nodes)


# updates best line by checking if new line is higher
def update_best_line(best_line, new_line, tracks, used_tracks=[]):
    if not best_line:
        best_line = new_line
    elif new_line:

        score_best_line = score.get_score(best_line, tracks, used_tracks)
        score_new_line = score.get_score(new_line, tracks, used_tracks)

        if score_best_line < score_new_line:
            best_line = new_line

    return best_line


