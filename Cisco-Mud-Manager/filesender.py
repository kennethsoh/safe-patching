import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor(FileSystemEventHandler):

    def on_created(self, event):
        filename, ext = os.path.splitext(event.src_path)
        if (ext == ".json"):
            print(f"Sending {event.src_path} to proxy.tpamc.com:/proxy/files") 
            os.system(f'scp {event.src_path} 192.168.1.11:/proxy/files')
            time.sleep(1)
            os.system("rm -f *.json")
            print(f"Removed {event.src_path} ") 
            pass
        else:
            pass

if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    event_handler=Monitor()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")
    observer.start()
    try:
        while(True):
           time.sleep(1)
           
    except KeyboardInterrupt:
            observer.stop()
            observer.join()
