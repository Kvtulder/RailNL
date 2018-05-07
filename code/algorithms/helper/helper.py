import score

# returns a max given number of routes based on their scores
def select_best_lines(lines, number, tracks, used_tracks):
    lines_and_scores = []

    for line in lines:
        lines_and_scores.append([line, score.get_score(line, tracks, used_tracks)])

    sort_lines = sorted(lines_and_scores, key=lambda lines_and_scores: lines_and_scores[1], reverse=True)

    best_lines = []

    for line in sort_lines:
        if line[1] > 0 and len(best_lines) <= number:
            best_lines.append(line[0])

    return best_lines


def update_used(new_line, tracks, used_tracks, lookup_track_scores=[], points_crit_track=[]):

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
