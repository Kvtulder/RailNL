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

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, data, used_tracks)])

    sorted_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    return sorted_lines


def update_used(new_line, used_tracks, data, lookup_track_scores=None):
    tracks_of_line = new_line.get_all_tracks(data)

    for track in tracks_of_line:
        if track.key not in used_tracks:
            if track.critical:
                used_tracks.append(track.key)

                if lookup_track_scores != None:
                    update_lookup(track, data, lookup_track_scores)

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
def lookup_score(data):
    lookup_tracks_score = {}

    for key, track in data.tracks.items():
        lookup_tracks_score.update({track.key: score.score_track(track, data)})
    return lookup_tracks_score


def update_lookup(track, data, look_up):
    look_up[track.key] = look_up[track.key] - data.points_per_crit

def lookup_score2(data):
    lookup_tracks_score = {}


    for key, track in data.tracks.items():

        score_track = score.score_track(track, data) * random.uniform(.8, 1.1)

        lookup_tracks_score.update({track.key: score_track})
    return lookup_tracks_score


