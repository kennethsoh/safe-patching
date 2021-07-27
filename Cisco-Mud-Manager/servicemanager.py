import os
import time
from multiprocessing import Process


def main():
    p1 = Process(target=mud_manager)
    p2 = Process(target=radiusd)
    p1.start()
    p2.start()

def mud_manager():
    print("Starting mud_manger")
    os.system("mud_manager -f mud_manager_conf_real.json")

def radiusd():
    print("Starting radiusd")
    os.system("radiusd")

if __name__ == "__main__":
    main()
