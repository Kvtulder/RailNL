from score import score


class Solution():
    def __init__(self, data, existing_lines=[]):
        self.data = data
        self.lookup_function = data.lookup_table_function

        self.lines = []
        self.used_tracks = []
        self.num_of_crit = 0

        if existing_lines:
            for line in existing_lines:
                self.add_line(line)

        # scoring variables
        self.score = 0
        self.overlap_tracks = 0
        self.short_tracks = []
        self.penalty_points = 0


    def add_line(self, line):
        self.lines.append(line)
        self.update_tracks()

        self.update_scoring_variables()

    def remove_line(self, line):
        self.lines.remove(line)

        self.update_tracks()
        self.update_scoring_variables()


    def update_scoring_variables(self):
        self.update_score()
        self.update_overlapping_tracks()
        self.update_penalty_points()
        self.update_short_tracks()

    def update_score(self):
        self.score = score.get_score(self.lines, self.data)

    def update_overlapping_tracks(self):
        self.overlap_tracks = len(self.used_tracks) - len(set(self.used_tracks))

    def update_penalty_points(self):
        self.penalty_points = self.overlap_tracks + 0.5* len(self.lines)

    def update_short_tracks(self):
        self.short_tracks = []
        for line in self.lines:
            if len(line.tracks) < 2:
                self.short_tracks.append(line)

    def update_tracks(self):
        self.used_tracks = []
        self.num_of_crit = 0

        for line in self.lines:
            self.add_tracks(line)

    def add_tracks(self, line):
        line_tracks = line.get_all_tracks()

        for track in line_tracks:
            if track.critical and track.key not in self.used_tracks:
                self.num_of_crit = self.num_of_crit + 1

            self.used_tracks.append(track.key)
