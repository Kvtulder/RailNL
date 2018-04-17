from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# define constants
MAP_TOP_BOUNDARY = 53.7
MAP_BOTTOM_BOUNDARY = 50.7
MAP_LEFT_BOUNDARY = 3.2130
MAP_RIGHT_BOUNDARY = 7.3


# Draws a map of the Netherlands with all stations and tracks
def draw_map(stations, tracks):

    lat = []
    long = []
    latcritical = []
    longcritical = []


    # sort stations in two lists: critical and non-critical
    for station in stations:
        if station.critical:
            latcritical.append(float(station.latitude))
            longcritical.append(float(station.longitude))
        else:
            lat.append(float(station.latitude))
            long.append(float(station.longitude))

    # draw a map of the netherlands
    my_map = Basemap(projection='merc', resolution='h', area_thresh=30,
                     llcrnrlon=MAP_LEFT_BOUNDARY, llcrnrlat=MAP_BOTTOM_BOUNDARY,
                     urcrnrlon=MAP_RIGHT_BOUNDARY, urcrnrlat=MAP_TOP_BOUNDARY)

    # fill the map
    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='moccasin')

    # draw the lines between the stations
    for track in tracks:
        x1, y1 = my_map(float(track.station_a.longitude),
                        float(track.station_a.latitude))
        x2, y2 = my_map(float(track.station_b.longitude),
                        float(track.station_b.latitude))

        plt.plot([x1, x2], [y1, y2], 'grey')

    # plot the stations as points
    x, y = my_map(long, lat)
    plt.plot(x, y, 'ro', markersize=4, label="Kritieke stations")
    x, y = my_map(longcritical, latcritical)
    plt.plot(x, y, 'bo', markersize=4, label="Niet-kritieke stations")
    plt.show()
