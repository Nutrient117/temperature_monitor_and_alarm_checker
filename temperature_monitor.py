
# TEMPERATURE MONITOR AND ALARM CHECKER


# Import sound module
try:
    import winsound
except ImportError:
    winsound = None


# Function for triggering audible alarm
def trigger_alarm():

    print("\nAUDIBLE ALARM ACTIVATED!")

    if winsound is not None:
        for alarm_count in range(3):
            winsound.Beep(1000, 1000)
    else:
        print("\a" * 3)


def temperature_monitor():

    print("\nTEMPERATURE MONITOR AND ALARM")

    # Define temperature limits
    warning_limit = 40
    safe_limit = 60

    # Store temperature readings
    temperatures = []

    # Collect five valid temperature readings
    for reading_number in range(5):

        while True:
            try:
                reading = float(
                    input(f"Enter temperature {reading_number + 1} in Celsius: ")
                )
                temperatures.append(reading)
                break

            except ValueError:
                print("Invalid input! Please enter a number.")

    # Display all readings
    print("\nTEMPERATURE READINGS")

    for reading_number, reading in enumerate(temperatures, start=1):
        print(f"Reading {reading_number}: {reading:.2f} °C")

    # Calculate temperature statistics
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    # Display results
    print("\nRESULTS")
    print(f"Highest temperature: {highest:.2f} °C")
    print(f"Lowest temperature:  {lowest:.2f} °C")
    print(f"Average temperature: {average:.2f} °C")

    # Check overall machine status
    print("\nMACHINE STATUS")

    if highest > safe_limit:
        print("ALARM! Temperature is critically high.")
        print("Machine status: CRITICAL")

        # Trigger audible alarm
        trigger_alarm()

    elif highest > warning_limit:
        print("WARNING! Temperature is rising.")
        print("Machine status: WARNING")

    else:
        print("Temperature is within the normal range.")
        print("Machine status: NORMAL")

    # Check individual temperature readings
    print("\nINDIVIDUAL ALERTS")

    for reading_number, reading in enumerate(temperatures, start=1):

        if reading > safe_limit:
            print(f"Reading {reading_number}: {reading:.2f} °C - CRITICAL!")

        elif reading > warning_limit:
            print(f"Reading {reading_number}: {reading:.2f} °C - WARNING!")

        else:
            print(f"Reading {reading_number}: {reading:.2f} °C - NORMAL")

    print("\nTemperature monitoring complete.")


# Run the program
temperature_monitor()
