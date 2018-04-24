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


# Draws a map of the Netherlands with all stations and tracks
def draw_map(stations, tracks, map_boundaries=map_netherlands):

    lat = []
    long = []
    latcritical = []
    longcritical = []

    # sort stations in two lists: critical and non-critical
    for key in stations:
        if stations[key].critical:
            latcritical.append(float(stations[key].latitude))
            longcritical.append(float(stations[key].longitude))
        else:
            lat.append(float(stations[key].latitude))
            long.append(float(stations[key].longitude))

    # draw a map of the netherlands
    my_map = Basemap(projection='merc', resolution='h', area_thresh=30,
                     llcrnrlon=map_boundaries.left,
                     llcrnrlat=map_boundaries.bottom,
                     urcrnrlon=map_boundaries.right,
                     urcrnrlat=map_boundaries.top)

    # fill the map
    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='moccasin')

    # draw the lines between the stations
    for key in tracks:
        x1, y1 = my_map(tracks[key].start.longitude,
                        tracks[key].start.latitude)
        x2, y2 = my_map(tracks[key].destination.longitude,
                        tracks[key].destination.latitude)

        plt.plot([x1, x2], [y1, y2], 'grey')

    # plot the stations as points
    x, y = my_map(long, lat)
    plt.plot(x, y, 'ro', markersize=4,)
    x, y = my_map(longcritical, latcritical)
    plt.plot(x, y, 'bo', markersize=4)

    track_patch = mpatches.Patch(color='grey', label='Tracks')
    station_patch = mpatches.Patch(color='red', label='Station')
    critical_patch = mpatches.Patch(color='blue', label='Critical station')

    plt.legend(handles=[track_patch, station_patch, critical_patch])
    plt.show()
