
# RansomKill

**RansomKill** is a lightweight, cross-platform tool designed to detect and mitigate ransomware attacks in real-time. By monitoring file modification activities, it identifies suspicious behavior that could indicate ransomware trying to encrypt files and stops the process before it spreads throughout the system.

## Features

- **Real-time Directory Monitoring**: Continuously watches specified directories for changes.
- **Ransomware Detection**: Detects abnormal activity by tracking rapid file modifications over a short period of time.
- **Automated Process Termination**: Once ransomware-like behavior is detected, RansomKill automatically kills the suspicious process.
- **Customizable Settings**: Users can set their own thresholds for the number of file modifications and time window to suit their environment.

## How It Works

1. **Directory Monitoring**: RansomKill uses the `watchdog` library to monitor file modifications within a user-specified directory.
2. **Detection**: The tool observes file modification patterns, and if a high volume of modifications is detected within a short period, it flags the behavior as suspicious.
3. **Prevention**: Once suspicious behavior is detected, the tool terminates the ransomware process using `psutil`.
   
## Requirements

- Python 3.x
- `psutil`: For process management and termination.
- `watchdog`: For monitoring file system changes.
  
You can install these dependencies using:
```bash
pip install psutil watchdog 
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/romishh3181/RansomKill.git
   ```

2. Navigate to the project folder:
   ```bash
   cd RansomKill
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:
   ```bash
   python3 main.py
   ```

## Usage

1. Run the program.
2. Specify the directory to monitor.
3. You will be asked whether to use default or custom settings for the file modification threshold and time window.
4. RansomKill will monitor the directory and terminate any process that exhibits ransomware-like behavior.

## Example

```bash
python3 main.py
```

You can monitor a directory for file changes, and RansomKill will stop any process that appears suspicious based on the modification activity.

## ScriptDetails

1. `main.py` - main script that welcomes ans asks for a directory to monitor and options to change monitor threshold and time window.
2. `monitor.py` - it works with the Watchdog API and monitors the directory, it also keeps updating the detector about the files modified.
3. `detector.py` - it contains the detection logic, that keeps track of the number of files modified in a specific given time windows, and if it exceeds the threshold, then it trigger the process-killer.
4. `process-killer.py` - it makes use of the psutil library and checks for every process running and if it is one of the files_modified, then it immediately terminates it. 

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/your-username/RansomKill/issues) for open issues or to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
