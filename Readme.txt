====WELCOME TO RANSOMKILL====
=>What is RansomKill?
---Well, RansomKill is a simple cross-platform Ransomware detection and mitigation software, that monitors any directory for unusual ransomware-like activities, and once triggered-- it kills 
that process instantly so that you dont have to empty your pockets later ... :)
=>What is a RansomWare?
---a type of malicious software designed to block access to a computer system until a sum of money is paid.(As Google says)..as said it locks or encrypts your files and then asks for a ransom
(a certain sum of money) to be paid in return of the decryption key.
=>What is the need?
--- Ransomwares are a rising problem nowadays as many ransomwares not only lock your files but also logs you out of your own system thus making it very hard to retreive anything, although it
is recommended to take personal help in such case, but RansomKill provides instant help and kills the process before it completes its assigned task.. 
=>is it cross platform?
--- Well, yes it is , i have tested it on both windows and linux, ans it works as specified so no need to worry :))
=>Is it tested?
---Yes, i have already tested it by simulating a basic ransomware attack on my kali machine(in a virtual environment for safety purposes).

BY--Rohan Mishra
Incase of any queries, Contact-- villaingaming81@gmail.com
All Rights Reserved by the Author 



# RansomKill

**RansomKill** is a cross-platform tool designed to detect and mitigate ransomware attacks in real-time. The tool monitors directories for suspicious file modifications and identifies 
potential ransomware processes based on abnormal activity, such as a large number of files being modified in a short time window. If ransomware-like behavior is detected, RansomKill 
automatically terminates the offending process before it can encrypt the entire system.

#Features:
- **Real-time Directory Monitoring**: Continuously tracks file changes in specified directories.
- **Ransomware Detection**: Alerts when a threshold of file modifications is surpassed within a given time window.
- **Automated Process Termination**: Identifies and kills suspicious processes that could be responsible for ransomware activity.
- **Customizable Settings**: Users can adjust the modification threshold and time window for fine-tuning detection sensitivity.

#Usage:
1. Specify the directory you want to monitor.
2. Adjust the modification threshold and time window, or use the default settings.
3. RansomKill will alert and terminate any process exhibiting ransomware-like behavior.

#ScriptDetails
1. main.py - main script that welcomes ans asks for a directory to monitor and options to change monitor threshold and time window.
2. monitor.py - it works with the Watchdog API and monitors the directory, it also keeps updating the detector about the files modified.
3. detector.py - it contains the detection logic, that keeps track of the number of files modified in a specific given time windows, and if it exceeds the threshold, then it trigger the process-killer.
4. process-killer.py - it makes use of the psutil library and checks for every process running and if it is one of the files_modified, then it immediately terminates it. 