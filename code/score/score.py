

# gets score based on amount of critical tracks ridden, lines and time used
# but also checks for previously used tracks so it doesnt award points for covering them
def get_score(lines, tracks, used_tracks=[]):
    # REMOVED THIS FROM FUNCTION PARAMETER WAS UNUSED
    num_of_critical_tracks = 0

    if not isinstance(lines, list):
        lines = [lines]

    if not num_of_critical_tracks:
        num_of_critical_tracks = num_crit_tracks(tracks)

    ridden_tracks = {}
    total_time = 0
    trains = len(lines)

    # calculate the amount of ridden critical tracks and total time
    for line in lines:

        # update time
        total_time += line.get_total_time()

        for i in range(0, len(line.stations) - 1):
            current_station = line.stations[i]
            destination = line.stations[i + 1]

            key1 = "{}-{}".format(current_station.name, destination.name)
            key2 = "{}-{}".format(destination.name, current_station.name)

            if key1 in tracks:
                if key1 not in used_tracks:
                    if key1 not in ridden_tracks and tracks[key1].critical:
                        ridden_tracks.update({key1: tracks[key1]})
            elif key2 in tracks:
                if key2 not in used_tracks:
                    if key2 not in ridden_tracks and tracks[key2].critical:
                        ridden_tracks.update({key2: tracks[key2]})

    percentage = len(ridden_tracks) / num_of_critical_tracks
    score = percentage * 10000 - trains * 20 - (total_time / 10)

    return score


def score_track(track, tracks):

    crit_points = points_per_crit_track(tracks)

    if track.critical:
        score = crit_points - (track.duration/10)
    else:
        score = - (track.duration/10)
    return score


def points_per_crit_track(tracks):
    number = num_crit_tracks(tracks)

    return (1/number) * 10000

# gets number of tracks that are critical
def num_crit_tracks(tracks):
    num_of_critical_tracks = 0

    # separate critical from non-critical
    for key in tracks:
        if tracks[key].critical:
            num_of_critical_tracks += 1

    return num_of_critical_tracks
