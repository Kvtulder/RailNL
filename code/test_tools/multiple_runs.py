import visualise as vis
import algorithms.greedy_helper as gh

# runs an algorithm multiple times
# prints best results
# plots path to it
def multiple_runs(number, algorithm, data):
    best_result = 0, []

    x_values = []
    y_values = []


    for i in range(number):
        new_result = algorithm(data)

        if new_result[0] > best_result[0]:
            best_result = new_result

        y_values.append(best_result[0])
        x_values.append(i)


        print(i ,best_result[0])

    vis.print_results(algorithm, best_result, data)

    vis.plot_line(x_values, y_values)


# runs an algorithm multiple times
# change max duration of a line over runs
def multiple_runs_duration(number, algorithm, data):
    best_result = 0, []

    x_values = []
    y_values = []

    data.max_duration = 100

    for i in range(number):
        new_result = algorithm(data)

        if new_result[0] > best_result[0]:
            best_result = new_result

        y_values.append(new_result[0])
        x_values.append(data.max_duration)


        data.max_duration = data.max_duration + (5)
        print(data.max_duration)

        if data.max_duration == 180:
            break

    vis.print_results(algorithm, best_result, data)

    vis.plot_line(x_values, y_values)


# runs an algorithm multiple times
# limits use of tracks with long duration in middle of route
# changes max lenght of track and
# where in the route they can be placed over time
def multiple_runs_long_tracks(number, algorithm, data):
    best_result = 0, []

    # set starting testing variables
    max_track_duration_max = 40
    bound_max = 15
    variables = [[0, "max_track_duration"], [12, "bound"]]
    data.set_test_variables(variables)

    # for i in range(max_track_duration_max):
    #     data.bound = 0
    #     for y in range(bound_max):
    #         print(data.max_track_duration, data.bound)
    #
    #         new_result = algorithm(data, gh.invalid_long_tracks)
    #
    #         if new_result[0] > best_result[0]:
    #             best_result = new_result
    #             print(best_result)
    #             best_result_var = ([new_result[0], data.max_track_duration, data.bound])
    #
    #         data.bound = data.bound + 1
    #
    #     data.max_track_duration = data.max_track_duration + 1
    #
    #     print(data.max_track_duration)

    new_result = algorithm(data, gh.invalid_long_tracks)

    vis.print_results(algorithm, new_result,data)

# runs an algorithm multiple times
# change max duration of a line over runs
def multiple_runs_max_tracks(number, algorithm, data):
    best_result = 0, []
    best_track_count = 0

    x_values = []
    y_values = []

    variables = [[1, "max_tracks"]]
    data.set_test_variables(variables)

    for i in range(20):
        new_result = algorithm(data, gh.invalid_max_tracks)

        if new_result[0] > best_result[0]:
            best_result = new_result
            best_track_count = data.max_tracks

        y_values.append(new_result[0])
        x_values.append(data.max_tracks)

        data.max_tracks = data.max_tracks + 1

    vis.print_results(algorithm, best_result, data)
    print(best_track_count)

    vis.plot_line(x_values, y_values)