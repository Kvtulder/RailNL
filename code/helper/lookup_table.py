from score import score
import random
# creates lookup table with each track and their score
# score purely based of points per ridden crit minus cost
def lookup_score(data):
    lookup_tracks_score = {}

    for key, track in data.tracks.items():
        lookup_tracks_score.update({track.key: score.score_track(track, data)})
    return lookup_tracks_score


def lookup_score_random(data):
    lookup_table = {}

    for key, track in data.tracks.items():

        score_track = score.score_track(track, data) * random.uniform(.5, 1.)

        lookup_table.update({track.key: score_track})
    return lookup_table


# changes value based on the amount of surrounding stations
# thus 'predicting' the future use of a track
def lookup_predicting(data):
    lookup_table = {}

    for key, track in data.tracks.items():
        surround_connections = len(track.destination.connections) + len(track.start.connections)

        score_track = score.score_track(track, data) * (1 - surround_connections/30)

        lookup_table.update({track.key: score_track})
    return lookup_table

# scores tracks based on their time with shorter tracks gaining more score
def lookup_time(data):
    lookup_table = {}

    for key, track in data.tracks.items():
        lookup_table.update({track.key: - track.duration})
    return lookup_table

def update_lookup(line, look_up):
    tracks = line.get_all_tracks()

    for track in tracks:
        look_up[track.key] = - track.duration / 10 - 50

    return look_up

# updates the lookup function by removing the score of ridden
# detracts extra points for tracks already ridden
def update_lookup_punish(line, look_up):
    tracks = line.get_all_tracks()

    for track in tracks:
        look_up[track.key] = - track.duration/10 - 50

    return look_up