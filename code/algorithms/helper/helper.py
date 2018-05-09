import score

# returns a max given number of routes based on their scores
def select_best_lines(lines, data, used_tracks, num_of_lines=0):
    lines_and_scores = []

    if num_of_lines == 0:
        num_of_lines = data.num_of_lines

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, data, used_tracks)])

    sort_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    best_lines = []

    if num_of_lines == 1:
        return sort_lines[0][0]
    else:
        for line in sort_lines:
            if line[1] > 0 and len(best_lines) <= num_of_lines:
                best_lines.append(line)

    return best_lines


def update_used(new_line, used_tracks, data, lookup_track_scores=None):
    tracks_of_line = new_line.get_all_tracks(data)

    for track in tracks_of_line:
        if track.key not in used_tracks:
            if track.critical:
                used_tracks.append(track.key)

                if lookup_track_scores != None:
                    update_lookup(track, lookup_track_scores, data)

    return used_tracks

def select_best_scoring_connection(connections, lookup_table):
    best_connection = None
    for key, connection in connections.items():
        if not connection:
            continue
        elif not best_connection:
            best_connection = connection
        elif lookup_table[connection.key] > lookup_table[best_connection.key]:
            best_connection = connection

    return best_connection

def update_lookup(track, look_up, data):
    look_up[track.key] = look_up[track.key] - data.points_per_crit




def lookup_score(data):
    lookup_tracks_score = {}

    for key, track in data.tracks.items():
        lookup_tracks_score.update({track.key: score.score_track(track, data)})
    return lookup_tracks_score

