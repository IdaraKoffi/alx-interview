0x03. Log Parsing
Project Overview
This project involves creating a Python script that reads log entries from standard input in real time, parses each entry, and computes certain metrics. The script processes logs in a specific format, counting occurrences of each HTTP status code and summing up file sizes. This data is printed every 10 lines and also on keyboard interruption (CTRL + C).

The key components of this project include parsing text input, handling exceptions, and managing data in real-time. The output statistics help simulate basic log analysis functionality, which is useful for monitoring web traffic or server activity.

Requirements
Programming Language: Python 3
Platform: Ubuntu 20.04 LTS
File Format: Executable script starting with #!/usr/bin/python3
PEP 8 Compliance: All code should follow the PEP 8 style guide.
Learning Objectives
Through this project, you will:

Practice real-time data processing from standard input.
Implement text parsing to extract specific data.
Use dictionaries to count occurrences and accumulate values.
Manage exceptions and handle signals in Python.
Usage
The script expects input in the following format:

plaintext
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Example:
plaintext
Copy code
111.111.111.111 - [2022-01-01] "GET /projects/260 HTTP/1.1" 200 512
Each line should contain an IP address, a timestamp, a GET request, an HTTP status code, and a file size (in bytes).

Output
The script prints two types of metrics:

Total File Size: Sum of file sizes from all log entries.
Status Code Counts: Count of occurrences for each HTTP status code (if available).
Sample Output:
plaintext
Copy code
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
This output is printed every 10 lines or when the program is interrupted with CTRL + C.

Running the Script
To run the script with a simulated log stream:

Generate Log Entries: Use the provided 0-generator.py script:
bash
Copy code
./0-generator.py | ./0-stats.py
Keyboard Interrupt: Press CTRL + C to trigger the script to print the current statistics.
Error Handling
Lines that do not match the expected format are ignored.
The script continues running unless explicitly interrupted (CTRL + C).
Status codes outside of the predefined set (200, 301, 400, 401, 403, 404, 405, 500) are ignored.
Example
If you run:

bash
Copy code
./0-generator.py | ./0-stats.py
The output might look like:

plaintext
Copy code
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
Project Files
0-stats.py: The main script for parsing logs and computing metrics.
README.md: Documentation for the project.
Author
This project is part of the ALX Software Engineering Program.


