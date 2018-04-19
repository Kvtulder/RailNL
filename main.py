import load
import visualise


def __main__():
    stations = load.load_stations()
    tracks = load.load_tracks(stations)
    visualise.draw_map(stations, tracks)


__main__()
