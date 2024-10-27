#!/usr/bin/python3
import sys
import signal

# Initialize the total file size and status code dictionary
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_code_counts.keys())

# Function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for keyboard interrupt
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Bind the signal handler to SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Process each line from standard input
line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            # Split the line into parts and attempt to parse status code and file size
            try:
                parts = line.split()
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update the counters if status code is valid
                if status_code in valid_status_codes:
                    status_code_counts[status_code] += 1
                    total_file_size += file_size
                    line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()
            except (IndexError, ValueError):
                # Skip line if it doesn't match the expected format
                continue
except KeyboardInterrupt:
    # On keyboard interrupt, print the final stats
    print_stats()
    sys.exit(0)

# Print any remaining stats at the end of input
print_stats()

