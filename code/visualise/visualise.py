from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



class MapBoundaries:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


# define constants
map_netherlands = MapBoundaries(53.7, 50.7, 3.2130, 7.3)


def draw_map(data, lines=[], map_boundaries=map_netherlands):
    """
    Draws a map of the Netherlands with all stations and tracks
    :param data:
    :param lines:
    :param map_boundaries:
    :return:
    """

    print("drawing a map...", end='', flush=True)


    lat = []
    long = []
    latcritical = []
    longcritical = []

    # sort stations in two lists: critical and non-critical
    for key in data.stations:
        if data.stations[key].critical:
            latcritical.append(float(data.stations[key].latitude))
            longcritical.append(float(data.stations[key].longitude))
        else:
            lat.append(float(data.stations[key].latitude))
            long.append(float(data.stations[key].longitude))


    # draw a map of the netherlands
    my_map = Basemap(projection='merc', resolution='h', area_thresh=30,
                     llcrnrlon=map_boundaries.left,
                     llcrnrlat=map_boundaries.bottom,
                     urcrnrlon=map_boundaries.right,
                     urcrnrlat=map_boundaries.top)

    print("\t\t\t DONE")

    # fill the map
    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='moccasin')



    # draw the lines between the stations
    for key in data.tracks:
        x1, y1 = my_map(data.tracks[key].start.longitude,
                        data.tracks[key].start.latitude)
        x2, y2 = my_map(data.tracks[key].destination.longitude,
                        data.tracks[key].destination.latitude)

        plt.plot([x1, x2], [y1, y2], 'grey')



    # plot the stations as points
    x, y = my_map(long, lat)
    plt.plot(x, y, 'bo', markersize=4,)
    x, y = my_map(longcritical, latcritical)
    plt.plot(x, y, 'ro', markersize=4)

    # draw the lines:
    for i in range(len(lines)):
        lines_x = []
        lines_y = []
        for station in lines[i].stations:
            line_x, line_y = my_map(station.longitude, station.latitude)
            lines_x.append(line_x)
            lines_y.append(line_y)
        plt.plot(lines_x, lines_y, '-', linewidth=3.0)



    track_patch = mpatches.Patch(color='grey', label='Tracks')
    station_patch = mpatches.Patch(color='blue', label='Station')
    critical_patch = mpatches.Patch(color='red', label='Critical station')


    plt.legend(handles=[track_patch, critical_patch, station_patch])

    plt.show()
