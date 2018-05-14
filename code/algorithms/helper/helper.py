import environment
import score

# returns a max given number of routes based on their scores
def select_best_lines(lines, used_tracks, num_of_lines=0):

    lines_and_scores = []

    if num_of_lines == 0:
        num_of_lines = environment.get_num_of_lines

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, used_tracks)])

    sort_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    best_lines = []

    if num_of_lines == 1:
        return sort_lines[0][0]
    else:
        for line in sort_lines:
            if line[1] > 0 and len(best_lines) <= num_of_lines:
                best_lines.append(line)

    return best_lines


def update_used(new_line, used_tracks, lookup_track_scores=None):
    tracks_of_line = new_line.get_all_tracks()

    for track in tracks_of_line:
        if track.key not in used_tracks:
            if track.critical:
                used_tracks.append(track.key)

                if lookup_track_scores != None:
                    update_lookup(track, lookup_track_scores)

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

# creates lookup table with each track and their score
# score purely based of points per ridden crit minus cost
def lookup_score():
    lookup_tracks_score = {}

    tracks = environment.get_tracks()

    for key, track in tracks.items():
        lookup_tracks_score.update({track.key: score.score_track(track)})
    return lookup_tracks_score


def update_lookup(track, look_up):
    look_up[track.key] = look_up[track.key] - environment.get_points_per_crit()



