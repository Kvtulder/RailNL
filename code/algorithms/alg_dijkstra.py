from copy import copy


def dijkstra(start):

    # dict with all the stations and the time it takes to reach it
    durations = {start.name: 0}
    routes = {start.name: [start]}

    queue = [start]
    while queue:
        current_station = queue[0]
        used_tracks = []
        duration_to_current = durations[current_station.name]

        # add items to queue
        while True:
            track = current_station.get_shortest_connection(used_tracks)
            if track:
                used_tracks.append(track)
                destination = track.get_other_station(current_station)

                time = duration_to_current + track.duration
                route = copy(routes[current_station.name])
                route.append(destination)

                if destination.name not in durations:
                    queue.append(destination)
                    durations.update({destination.name: time})
                    routes.update({destination.name: route})
                else:
                    if time < durations[destination.name]:
                        durations.update({destination.name: time})
                        routes.update({destination.name: route})

            else:
                # no more tracks left, exit loop
                break

        del queue[0]

    return routes, durations
