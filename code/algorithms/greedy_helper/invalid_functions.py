# checks if route is valid
def invalid(line, connection, used_connections, data):

    if connection.key in used_connections or line.total_time + connection.duration > data.max_duration:
        return True
    else:
        return False

# blocks long tracks of appearing in the middle of route
def invalid_long_tracks(line, connection, used_connections, data):

    if connection.key in used_connections or line.total_time + connection.duration > data.max_duration:
        return True

    line_tracks = line.get_all_tracks(data)

    if len(line_tracks) - 1 >= data.bound:
        if connection.key in line.stations[0].connections:
            if line_tracks[data.bound].duration > data.max_track_duration:
                return True
        else:
            if line_tracks[-data.bound - 1].duration > data.max_track_duration:
                return True

    return False


# also checks if number of tracks in line doesnt exceed maximum
def invalid_max_tracks(line, connection, used_connections, data):

    if connection.key in used_connections or line.total_time + connection.duration > data.max_duration:
        return True

    line_tracks = line.get_all_tracks()

    if len(line_tracks) - 1 >= data.max_tracks:
        return True

    return False

