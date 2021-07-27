'''
File Name       : fsm.py
Author          : Kenneth Soh
Date created    : 30 June 2021
'''

import os
import sys
import time
from os import path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor(FileSystemEventHandler):

    def on_modified(self, event):
        filename, ext = os.path.splitext(event.src_path)
        if (ext == ".json"):
            print(f"python3 proxy.py {filename}")
            print(f"python3 proxy.py {ext}")
            print(f"python3 proxy.py {event.src_path}")
            os.system(f'python3 proxy.py {event.src_path}')
            pass
        else:
            pass

if __name__ == "__main__":
    if path.exists("files"):
        pass
    else:
        try:
            os.system("mkdir files")
        except:
            None
            
    src_path = sys.argv[1] if len(sys.argv) > 1 else 'files/'
    
    event_handler=Monitor()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")
    print(src_path)
    observer.start()
    try:
        while(True):
           time.sleep(1)
           
    except KeyboardInterrupt:
            observer.stop()
            observer.join()
