
# gets score based on amount of critical tracks ridden, lines and time used
# but also checks for previously used tracks so it doesnt award points for covering them
def get_score(lines, data, used_tracks=[]):
    # REMOVED THIS FROM FUNCTION PARAMETER WAS UNUSED


    if not isinstance(lines, list):
        lines = [lines]

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

            if key1 in data.tracks:
                if key1 not in used_tracks:
                    if key1 not in ridden_tracks and data.tracks[key1].critical:
                        ridden_tracks.update({key1: data.tracks[key1]})
            elif key2 in data.tracks:
                if key2 not in used_tracks:
                    if key2 not in ridden_tracks and data.tracks[key2].critical:
                        ridden_tracks.update({key2: data.tracks[key2]})

    percentage = len(ridden_tracks) / data.num_crit_tracks
    score = percentage * 10000 - trains * 20 - (total_time / 10)

    return score

def score_track(track, data):

    crit_points = data.points_per_crit

    if track.critical:
        score = crit_points - (track.duration/10)
    else:
        score = - (track.duration/10)
    return score