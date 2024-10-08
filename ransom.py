import time

file_path = '/home/rohan/Downloads/test_directory/new_file.txt'

# Open a file and keep it open
with open(file_path, 'w') as f:
    while True:
        f.write(f"Keeping the file open at {time.time()}\n")
        f.flush()
        time.sleep(0.2)
