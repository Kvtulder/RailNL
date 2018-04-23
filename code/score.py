def get_score(lines, tracks, num_of_critical_tracks=None):

    if not num_of_critical_tracks:
        num_of_critical_tracks = get_num_of_critical_tracks(tracks)

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
                if key1 not in ridden_tracks and tracks[key1].critical:
                    ridden_tracks.update({key1: tracks[key1]})
            elif key2 in tracks:
                if key2 not in ridden_tracks and tracks[key2].critical:
                    ridden_tracks.update({key2: tracks[key2]})

    percentage = len(ridden_tracks) / num_of_critical_tracks
    score = percentage * 10000 - trains * 20 - (total_time / 10)

    return score


def get_num_of_critical_tracks(tracks):
    num_of_critical_tracks = 0

    # separate critical from non-critical
    for key in tracks:
        if tracks[key].critical:
            num_of_critical_tracks += 1

    return num_of_critical_tracks
