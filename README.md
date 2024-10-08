# RansomKill

**RansomKill** is a cross-platform tool designed to detect and mitigate ransomware attacks in real-time. The tool monitors directories for suspicious file modifications and identifies 
potential ransomware processes based on abnormal activity, such as a large number of files being modified in a short time window. If ransomware-like behavior is detected, RansomKill 
automatically terminates the offending process before it can encrypt the entire system.

###Features:
- **Real-time Directory Monitoring**: Continuously tracks file changes in specified directories.
- **Ransomware Detection**: Alerts when a threshold of file modifications is surpassed within a given time window.
- **Automated Process Termination**: Identifies and kills suspicious processes that could be responsible for ransomware activity.
- **Customizable Settings**: Users can adjust the modification threshold and time window for fine-tuning detection sensitivity.

###Usage:
1. Specify the directory you want to monitor.
2. Adjust the modification threshold and time window, or use the default settings.
3. RansomKill will alert and terminate any process exhibiting ransomware-like behavior.

###ScriptDetails
1. main.py - main script that welcomes ans asks for a directory to monitor and options to change monitor threshold and time window.
2. monitor.py - it works with the Watchdog API and monitors the directory, it also keeps updating the detector about the files modified.
3. detector.py - it contains the detection logic, that keeps track of the number of files modified in a specific given time windows, and if it exceeds the threshold, then it trigger the process-killer.
4. process-killer.py - it makes use of the psutil library and checks for every process running and if it is one of the files_modified, then it immediately terminates it. 
