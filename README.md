# Temperature Monitor and Alarm Checker

## Project Description

The Temperature Monitor and Alarm Checker is a Python-based engineering application designed to monitor temperature readings and identify when a machine's temperature exceeds its defined operating limits.

The program collects five temperature readings from the user, analyses the readings, calculates temperature statistics, and displays the machine's operating status.

It also features an audible alarm system that alerts the user when a critical temperature is detected.

## Features

- **Temperature Monitoring:** Collects five temperature readings from the user.
- **Input Validation:** Handles invalid inputs and requests a valid numerical value.
- **Temperature Statistics:** Calculates the highest, lowest, and average temperature.
- **Three-Level Alert System:** Classifies machine temperature as NORMAL, WARNING, or CRITICAL.
- **Individual Temperature Alerts:** Checks and displays the status of each reading.
- **Audible Alarm System:** Produces three warning beeps when the temperature exceeds the safe limit on supported systems.

## Temperature Alert Levels

| Temperature Range | Machine Status |
|---|---|
| 40°C and below | NORMAL |
| Above 40°C up to 60°C | WARNING |
| Above 60°C | CRITICAL |

## Technologies Used

- Python 3
- Winsound module (for Windows audible alarms)
- VS Code

## How to Run the Program

1. Install Python 3 on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code or another Python editor.
4. Run the Python file:

```bash
python temperature_monitor.py
```

5. Enter five temperature readings when prompted.
6. View the temperature statistics, machine status, and individual alerts.

## Sample Output

```text
TEMPERATURE MONITOR AND ALARM

Enter temperature 1 in Celsius: 25
Enter temperature 2 in Celsius: 35
Enter temperature 3 in Celsius: 45
Enter temperature 4 in Celsius: 55
Enter temperature 5 in Celsius: 70

TEMPERATURE READINGS
Reading 1: 25.00 °C
Reading 2: 35.00 °C
Reading 3: 45.00 °C
Reading 4: 55.00 °C
Reading 5: 70.00 °C

RESULTS
Highest temperature: 70.00 °C
Lowest temperature: 25.00 °C
Average temperature: 46.00 °C

MACHINE STATUS
ALARM! Temperature is critically high.
Machine status: CRITICAL

AUDIBLE ALARM ACTIVATED!
```

## Special Feature

### Audible Alarm System

The project includes an audible alarm system using Python's `winsound` module on Windows.

When a temperature reading exceeds 60°C, the program automatically triggers three warning beeps to alert the user of a critical temperature condition.

## What I Learned

Through this project, I practised and improved my understanding of:

- Python functions and function calls.
- Lists and data storage.
- For loops and while loops.
- Conditional statements.
- Exception handling using try and except.
- Built-in functions such as `max()`, `min()`, and `sum()`.
- Importing and using Python modules.
- Engineering temperature monitoring and alarm logic.

## Author

**Owodeyi Adam Akorede**

Mechatronics Engineering
