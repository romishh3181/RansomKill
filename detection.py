import time
from collections import defaultdict
from process_killer import kill_ransomware_process

file_modifications = defaultdict(list)

class RansomwareDetector:
    def __init__(self, mod_threshold=10, time_window=5):
        self.mod_threshold = mod_threshold
        self.time_window = time_window

    def on_file_modified(self, file_path):
        file_modifications[file_path].append(time.time())
        print(f"File modified: {file_path}")
        self.detect_ransomware()

    def detect_ransomware(self):
        curr_t = time.time()
        recent_modifications = 0

        for file, timestamps in file_modifications.items():
     
            timestamps = [t for t in timestamps if curr_t - t <= self.time_window]
            recent_modifications += len(timestamps)
            file_modifications[file] = timestamps  

        print(f"Recent modifications: {recent_modifications}")

        if recent_modifications > self.mod_threshold:
            print("Suspicious activity detected! Stopping ransomware now...")
            kill_ransomware_process(file_modifications)
