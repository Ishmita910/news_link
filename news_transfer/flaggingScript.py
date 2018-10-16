import time
import sys
import logging
import datetime as dt


from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
# changes = ''
class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
       
        print(event.src_path, event.event_type) # print now only for debug



    def on_modified(self, event):
        self.process(event)

  
if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
            # print('checking')
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

