import score
import helper
from Line import Line


def prim(stations, tracks, num_of_lines, max_duration):
    used_tracks = []
    best_lines = []
    lookup_tracks_score = {}

    points_crit_track = score.points_per_crit_track(tracks)
    num_crit_tracks = score.num_crit_tracks(tracks)

    for key, track in tracks.items():
        lookup_tracks_score.update({track.id: score.score_track(track, tracks)})

    while len(used_tracks) < num_crit_tracks and len(best_lines) != num_of_lines:
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
                        if connection.id not in used_connections:
                            if new_line.total_time + connection.duration < max_duration:
                                if not best_connection:
                                    best_connection = connection
                                elif lookup_tracks_score[connection.id] > lookup_tracks_score[best_connection.id]:
                                    best_connection = connection

                if best_connection:
                    if best_connection.destination.name in new_line.stations[0].connections:
                        new_line.stations.insert(0, best_connection.destination)
                    else:
                        new_line.stations.append(best_connection.destination)
                    new_line.total_time = new_line.get_total_time()

                    used_connections.append(best_connection.id)

                    ends = [new_line.stations[0], new_line.stations[-1]]

                else:
                    line_completed = True

            new_line = trim_line(new_line, lookup_tracks_score)
            lines.append(new_line)

        best_line = helper.select_best_lines(lines, num_of_lines, tracks, used_tracks)
        best_lines.append(best_line[0])

        used_tracks = helper.update_used(best_lines[-1], tracks,used_tracks, lookup_tracks_score, points_crit_track)

    return score.get_score(best_lines, tracks), best_lines



def update_used(new_line, tracks, used_tracks, lookup_track_scores, points_crit_track):

    for i in range(len(new_line.stations) - 1):
        cur_station = new_line.stations[i]
        next_station = new_line.stations[i + 1]

        used_track = cur_station.connections[next_station.name]
        used_track_key = 0

        for key, track in tracks.items():
            if track.id == used_track.id:
                used_track_key = key

        if used_track_key not in used_tracks:
            if used_track.critical:
                used_tracks.append(used_track_key)

                if lookup_track_scores:
                    lookup_track_scores[used_track.id] = lookup_track_scores[used_track.id] - points_crit_track

    return used_tracks


def trim_line(line, lookup_tracks_score):
    front_done = False
    end_done = False

    i = 0

    while not end_done or not front_done:
        track_front = line.stations[0].connections[line.stations[1].name]
        track_end = line.stations[-1].connections[line.stations[-2].name]

        if not end_done:
            if lookup_tracks_score[track_end.id] < 0:
                line.stations.pop()
            else:
                end_done = True

        if not front_done:
            if lookup_tracks_score[track_front.id] < 0:
                line.stations.remove(line.stations[i])
            else:
                front_done = True

        if len(line.stations) < 2:
            break

    line.total_time = line.get_total_time()
    return line
