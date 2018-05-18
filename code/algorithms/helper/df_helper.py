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


# returns a max given number of routes based on their scores
def select_best_lines(lines_and_scores, number):
    sort_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    sorted_list = []

    for line in sort_lines:
        if line[1] > 0 and len(sorted_list) <= number:
            sorted_list.append(line[0])

    return sorted_list



