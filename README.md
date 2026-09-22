# TCP Port Scanner

A Python-based TCP port scanner designed to check the status of ports on a target host.

## Features

- Scan a single host
- Scan a range of TCP ports
- Detect OPEN and CLOSED ports
- Handle connection timeouts
- Multithreaded scanning for better performance
- Exception handling
- Display scan results in the terminal
- Save scan results to a log file
- Display scan summary and timestamps

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP
- Threading / ThreadPoolExecutor
- File Logging

## How It Works

The scanner attempts to establish a TCP connection with each specified port.

```text
Target Host
     |
     v
TCP Connection Attempt
     |
     +----> OPEN
     |
     +----> CLOSED
     |
     +----> TIMEOUT

## How to Run

```text
Make sure Python 3 is installed.

Run:

python port_scanner.py

The program will ask for:

1. Target host
2. Starting port
3. Ending port

Example:

Target host: 127.0.0.1
Starting port: 1
Ending port: 100

## Example Output

Port 22 - CLOSED
Port 80 - OPEN
Port 443 - OPEN
Port 8080 - CLOSED

Scan completed.
Results saved to port_scanner.log

## Learning Objectives

This project was built to practice:
- TCP socket programming
- Network ports and services
- Basic network reconnaissance
- Python concurrency
- Exception handling
- Security-related logging

## Project Purpose

This project is intended for cybersecurity and networking education.

Only scan systems and networks that you own or have explicit permission to test.

## Author

Abdullah Malik
