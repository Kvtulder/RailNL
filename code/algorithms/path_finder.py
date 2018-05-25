from copy import copy

def dijkstra(start, end=None):
    """ Finds the fastest possible route between a given start and all possible
    end points or a given end point

    Keyword arguments:
    start   -- the start station object
    end     -- the end station object (default = None)
    """

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
            if not track:
                break

            used_tracks.append(track)
            destination = track.get_other_station(current_station)

            time = duration_to_current + track.duration
            route = copy(routes[current_station.name])
            route.append(destination)

            if destination.name not in durations:
                queue.append(destination)
                durations.update({destination.name: time})
                routes.update({destination.name: route})

                # check if station equals end station
                if end and destination == end:
                    return route, time
            else:
                if time < durations[destination.name]:
                    durations.update({destination.name: time})
                    routes.update({destination.name: route})

        del queue[0]

    return routes, durations


def depth_first(start, end, max_duration, duration=0.0, route=[], routes=[]):
    """ Finds all the possible routes between a given start and end with a maximum
    of n minutes.

    :argument start:        the start station object
    :argument end:          the end station object
    :argument max_duration: the maximum duration of the solution in minutes

    :returns a list with the found route(s)
    """
    # add first station to the route list if empty
    if not route:
        route.append(start)

    # loop over all the possible directions
    for key in start.connections:

        track = start.connections[key]
        duration += track.duration
        destination = track.get_other_station(start)

        if len(route) > 1:
            # make sure the route does not go backwards
            if destination == route[-2]:
                continue

        if duration > max_duration:
            # make sure the route does not exceed the max duration
            continue

        # copy to make sure there is a new memory reference
        new_route = copy(route)
        new_route.append(destination)

        if destination == end:
            # found the destination! append the route to the list
            routes.append(new_route)
        else:
            # not reached the destination (yet), continue searching
            depth_first(destination, end, max_duration, duration,
                        new_route, routes)

    return routes

