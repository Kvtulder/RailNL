def get_score(lines, tracks):
    critical_tracks = {}
    ridden_tracks = {}
    total_time = 0
    trains = len(lines)

    # separate critical from non-critical
    for key in tracks:
        if tracks[key].critical:
            critical_tracks.update({key : tracks[key]})

    # calculate the amount of ridden critical tracks and total time
    for line in lines:

        total_time += line.get_total_time()

        for i in range(0, len(line.stations) - 1):
            current_station = line.stations[i]
            destination = line.stations[i + 1]

            key1 = "{}-{}".format(current_station.name, destination.name)
            key2 = "{}-{}".format(destination.name, current_station.name)

            if key1 in tracks:
                if key1 not in ridden_tracks:
                    ridden_tracks.update({key1 : tracks[key1]})
            elif key2 in tracks:
                if key2 not in ridden_tracks:
                    ridden_tracks.update({key2 : tracks[key2]})


    percentage = float(len(critical_tracks)) / len(ridden_tracks)
    score = percentage * 10000 - trains * 20 - (total_time / 10)

    return score