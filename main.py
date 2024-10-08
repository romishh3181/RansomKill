import os
import time
from detection import RansomwareDetector
from monitor import monitor_directory

def intro():
    logo = """
[31m                                ____                                 
                               |  _ \ __ _ _ __  ___  ___  _ __ ___  
                               | |_) / _` | '_ \/ __|/ _ \| '_ ` _ \ 
                               |  _ < (_| | | | \__ \ (_) | | | | | |
                               |_| \_\__,_|_| |_|___/\___/|_| |_| |_|
                                                                     
[0m                                             _  ___ _ _ 
                                            | |/ (_) | |
                                            | ' /| | | |
                                            | . \| | | |
                                            |_|\_\_|_|_|
     
                                                  --- By Rohan Mishra                                                      
"""
    print(logo)
    print("\n")
    print("Welcome to RansomKill - a cross-platform tool for detecting and mitigating ransomware threats !!!")

def get_input():
    intro()
    directory = input("Enter the directory you want to monitor: ")
    
    if not os.path.isdir(directory):
        print("The specified directory does not exist!!! Exiting...")
        exit()

    changes = input("\nDo you want to change the default modification threshold and time window? (y/n): ").strip().lower()
    
    if changes == 'y':
        mod_threshold = int(input("Enter the new modification threshold (default 10): "))
        time_window = int(input("Enter the new time window in seconds (default 5): "))
    else:
        mod_threshold = 10
        time_window = 5

    return directory, mod_threshold, time_window

if __name__ == "__main__":
    directory, modification_threshold, time_window = get_input()
    detector = RansomwareDetector(modification_threshold, time_window)
    
    print(f"\nMonitoring directory: {directory} with threshold {modification_threshold} and time window {time_window} seconds...")
    monitor_directory(directory, detector)
