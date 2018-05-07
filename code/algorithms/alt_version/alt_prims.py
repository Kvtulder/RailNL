import score
import helper
from Line import Line


def prim(stations, tracks, num_of_lines, max_duration):
    used_tracks = []
    used_crits = []
    best_lines = []
    lookup_tracks_score = {}

    num_of_crit = score.get_num_of_critical_tracks(tracks)
    points_crit_track = (1/num_of_crit) * 10000

    for key, track in tracks.items():
        lookup_tracks_score.update({track.id: score_track(track, points_crit_track)})

    while len(used_crits) < num_of_crit and len(best_lines) != num_of_lines:
        lines = []

        for key, station in stations.items():
            used_connections = []
            ends = [station]
            new_line = Line([station])

            line_completed = False

            while not line_completed:
                best_connection = None

                for end in ends:
                    for key2, connection in end.connections.items():
                        if connection.id not in used_tracks and connection.id not in used_connections:
                            if new_line.total_time + connection.duration < max_duration:
                                if not best_connection:
                                    best_connection = connection
                                elif lookup_tracks_score[connection.id] > lookup_tracks_score[best_connection.id]:
                                    best_connection = connection

                if best_connection:
                    if best_connection.destination.name in new_line.stations[0].connections:
                        new_line.stations = [best_connection.destination] + new_line.stations
                    else:
                        new_line.stations = new_line.stations + [best_connection.destination]

                    used_connections.append(best_connection.id)

                    new_line.total_time = new_line.get_total_time()

                    ends = [new_line.stations[0], new_line.stations[-1]]
                else:
                    line_completed = True

            lines.append(new_line)

        best_line = helper.select_best_line(lines, tracks)
        best_lines.append(best_line)

        used_tracks = update_used(best_line, used_crits, used_tracks)

        print("line calculated")

    print("total score: ", score.get_score(best_lines, tracks))
    return score.get_score(best_lines, tracks), best_lines


def select_best_line(lines, tracks):
    lines_and_scores = []

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, tracks)])

    sort_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    return sort_lines[0][0]


def update_used(new_line, used_crits, used_tracks):

    for i in range(len(new_line.stations) - 1):
        cur_station = new_line.stations[i]
        next_station = new_line.stations[i + 1]

        used_track = cur_station.connections[next_station.name]

        if used_track.id not in used_tracks:
            used_tracks.append(used_track.id)

        if used_track.id not in used_crits:
            if used_track.critical:
                used_crits.append(used_track.id)
    return used_tracks


def score_track(track, points_crit_track):
    if track.critical:
        score = points_crit_track - (track.duration/10)
    else:
        score = - (track.duration/10)
    return score


def track_from_id(track_id, track_list):
    for track in track_list:
        if track_id == track.id:
            track_object = track
            return track_object


