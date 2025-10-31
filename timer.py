import time


class GameTimer:
    def __init__(self):
        self.start_time = time.time()
        self.paused = False
        self.pause_start = 0
        self.total_pause_time = 0

    def get_time(self):
        if self.paused:
            return self.pause_start - self.start_time - self.total_pause_time
        else:
            return time.time() - self.start_time - self.total_pause_time

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_start = time.time()

    def resume(self):
        if self.paused:
            self.paused = False
            self.total_pause_time += time.time() - self.pause_start

    def reset(self):
        self.start_time = time.time()
        self.total_pause_time = 0
        self.paused = False

    def set_time(self, new_time):
        self.start_time = time.time() - new_time
        self.initial_offset = new_time
        if self.paused:
            self.pause_start = time.time()
        self.total_pause_time = 0