import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MonitorHandler(FileSystemEventHandler):
    def __init__(self, detector):
        self.detector = detector  
    
    def on_modified(self, event):  
        if event.is_directory:
            return
        self.detector.on_file_modified(event.src_path)

def monitor_directory(path, detector):
    event_handler = MonitorHandler(detector)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
