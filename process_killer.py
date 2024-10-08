import psutil

def kill_ransomware_process(file_modifications):
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_files = process.open_files()
            for file in process_files:
               
                if file.path in file_modifications and file_modifications[file.path]:
                    print(f"Killing this Process: {process.info['name']} (PID: {process.info['pid']})")
                    
                    
                    process.terminate()
                    
                  
                    process.wait(timeout=3)
                    break  # Exit after terminating the process
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
           
            print(f"Could not kill process: {process.info['name']} (PID: {process.info['pid']}) due to: {e}")
            continue
