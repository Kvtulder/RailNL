import load
#import visualise


def __main__():
    stations = load.load_stations()
    tracks = load.load_tracks(stations)

    print(stations, tracks)

    # create map
    # visualise.draw_map(stations, tracks)


__main__()
