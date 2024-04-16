#!/bin/bash

# Function to display an error message and exit
show_error_message() {
    echo "Error: $1"
    exit 1
}

# Function to run a process with output displayed
run_process_with_output() {
    local script="$1"
    local message="$2"

    echo "Running: $script"
    echo "Message: $message"

    echo "Starting $message..."
    python3 "$script"
    local status=$?  # Capture the exit status of the Python script
    if [ $status -ne 0 ]; then
        show_error_message "Error running $script"
    fi
}

# Run each process with output displayed
run_process_with_output "calibration_images.py" "Capturing calibration images..."
run_process_with_output "calibration.py" "Calibrating..."
run_process_with_output "disparity.py" "Calculation of disparity map..."

# Display success message
echo "All processes completed successfully."

# Exit the script
exit 0













