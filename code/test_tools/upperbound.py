import score

def upperboundz(data):

    crit_tracks = []

    for key,track in data.tracks.items():
        if track.critical:
            crit_tracks.append(track)

    routes = []
    all_time = 0

    while len(crit_tracks) > 0:
        total_time = 0
        route = []

        for crit_track in crit_tracks:
            if total_time + crit_track.duration <= data.max_duration:
                route.append(crit_track)
                total_time = total_time + crit_track.duration

        routes.append(route)
        all_time = all_time + total_time

        for t in route:
            crit_tracks.remove(t)

        if len(routes) == data.num_of_lines:
            break

    num_crit_tracks = data.num_crit_tracks

    percentage = (num_crit_tracks - len(crit_tracks))/ num_crit_tracks

    upperbound_score = percentage * 10000 - (all_time/10) - len(routes)*20
    return upperbound_score


