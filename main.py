import load
import objects


def __main__():
    stations = load.load_stations()
    tracks = load.load_tracks(stations)

    # test: create line between amsterdam centraal and amstel

    line1 = objects.Line(tracks)
    line1.add_station(stations[5])
    line1.add_station(stations[6])

    print("{}".format(line1))

    line1.add_station(stations[0])
    print("{}".format(line1))

__main__()
