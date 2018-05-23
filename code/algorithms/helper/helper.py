import random
from score import score

# returns a max given number of routes based on their scores
def select_best_lines(lines, used_tracks, data, num_of_lines=0):
    best_lines = []
    sorted_by_score = sort_lines_on_score(lines, used_tracks, data)

    if num_of_lines == 0:
        num_of_lines = data.num_of_lines

    if num_of_lines == 1:
        return sorted_by_score[0][0]
    else:
        for line in sorted_by_score:
            if line[1] > 0 and len(best_lines) <= num_of_lines:
                best_lines.append(line)

    return best_lines


def sort_lines_on_score(lines, used_tracks, data):
    lines_and_scores = []
    lines_efficient = []

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, data, used_tracks)])

    # for line in lines:
    #     if line.total_time == 0:
    #         lines_and_scores.append(([line], 0))
    #     elif len(line.stations) < 4:
    #         lines_and_scores.append([line, (score.get_score(line, data, used_tracks)/line.total_time) * 0,5])
    #     else:
    #         lines_and_scores.append([line, (score.get_score(line, data, used_tracks)/line.total_time)])

    sorted_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)



    return sorted_lines


def update_used(new_line, used_tracks, lookup_track_scores=None):
    if not new_line:
        return used_tracks

    tracks_of_line = new_line.get_all_tracks()
    for track in tracks_of_line:
        if track.key not in used_tracks:
            if track.critical:
                used_tracks.append(track.key)

    if lookup_track_scores != None:
        update_lookup(new_line, lookup_track_scores)

    return used_tracks


def select_best_scoring_connection(connections, lookup_table):
    best_connection = None

    for key, connection in connections.items():
        connect_poor = False
        if len(connection.destination.connections) < 2 or len(connection.start.connections) < 2:
            connect_poor = True


        if not connection:
            continue
        # elif connect_poor and lookup_table[connection.key] > 0:
        #     best_connection = connection
        elif not best_connection:
            best_connection = connection
        elif lookup_table[connection.key] > lookup_table[best_connection.key]:
            best_connection = connection

    return best_connection


# creates lookup table with each track and their score
# score purely based of points per ridden crit minus cost
def lookup_score(data):
    lookup_tracks_score = {}

    for key, track in data.tracks.items():
        lookup_tracks_score.update({track.key: score.score_track(track, data)})
    return lookup_tracks_score


def update_lookup(line, look_up):
    tracks = line.get_all_tracks()

    for track in tracks:
        look_up[track.key] = - track.duration/10

    return look_up

def lookup_score_random(data):
    lookup_table = {}

    for key, track in data.tracks.items():

        score_track = score.score_track(track, data) * random.uniform(.8, 1.1)

        lookup_table.update({track.key: score_track})
    return lookup_table


# changes value based on the amount of surrounding stations
def lookup_predicting(data):
    lookup_table = {}

    for key, track in data.tracks.items():
        surround_connections = len(track.destination.connections) + len(track.start.connections)

        score_track = score.score_track(track, data) * (1 - surround_connections/30)

        lookup_table.update({track.key: score_track})
    return lookup_table


