import load
import objects


def __main__():
    stations = load.load_stations()
    tracks = load.load_tracks(stations)

    # test: create line between amsterdam centraal and amstel

    line1 = objects.Line(tracks)
    line1.add_station(stations["Amsterdam Amstel"])
    line1.add_station(stations["Amsterdam Centraal"])

    print("{}".format(line1))

    line1.add_station(stations["Amsterdam Sloterdijk"])
    print("{}".format(line1))

    print(line1.get_total_time())

__main__()