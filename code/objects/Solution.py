from score import score
import copy

class Solution():
    def __init__(self, data, lookup_table=None, existing_lines=[]):
        self.data = data
        self.lines = []
        self.start_lookup_table = copy.copy(lookup_table)
        self.lookup_table = lookup_table
        self.used_tracks = []

        if existing_lines:
            for line in existing_lines:
                self.add_line(line)

        if len(existing_lines) > 1:
            self.update_score()
        else:
            self.score = 0


    def add_line(self, line):
        self.lines.append(line)

        tracks = line.get_all_tracks()

        self.add_to_used_tracks(line)

        self.update_score()

    def remove_line(self, line):
        self.lines.remove(line)

        tracks = line.get_all_tracks()

        self.get_used_tracks()

        self.update_score()

    def update_score(self):
        self.score = score.get_score(self.lines, self.data)

    def get_used_tracks(self):
        self.used_tracks = []
        for line in self.lines:
            self.add_to_used_tracks(line)

    def add_to_used_tracks(self, line):
        line_tracks = line.get_all_tracks()

        for track in line_tracks:
            if track.critical and track.key not in self.used_tracks:
                self.used_tracks.append(track.key)
