import bin.environment


# gets score based on amount of critical tracks ridden, lines and time used
# but also checks for previously used tracks so it doesnt award points for covering them
def get_score(lines, used_tracks=[]):

    num_of_critical_tracks = bin.environment.get_num_of_tracks()
    tracks = bin.environment.get_tracks()

    # make sure the function also works with a sinlge line
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