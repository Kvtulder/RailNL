import helper as helper
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


# sorts lines and returns best score
def sort_lines_on_score(lines, used_tracks, data):
    lines_and_scores = []

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, data, used_tracks)])

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
        helper.update_lookup(new_line, lookup_track_scores)

    return used_tracks


def select_best_scoring_connection(connections, lookup_table):
    best_connection = None

    for key, connection in connections.items():
        connect_poor = False
        if len(connection.destination.connections) < 2 or len(connection.start.connections) < 2:
            connect_poor = True


        if not connection:
            continue
        elif connect_poor and lookup_table[connection.key] > 0:
            best_connection = connection
        elif not best_connection:
            best_connection = connection
        elif lookup_table[connection.key] > lookup_table[best_connection.key]:
            best_connection = connection

    return best_connection





