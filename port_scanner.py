import socket
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


# Create log file
logging.basicConfig(
    filename="port_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def scan_port(host, port, timeout=1):
    """
    Scan one TCP port and return its status.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            return port, "OPEN"

        return port, "CLOSED"

    except socket.timeout:
        return port, "TIMEOUT"

    except socket.error as error:
        logging.error(f"Port {port} - Socket error: {error}")
        return port, "ERROR"

    except Exception as error:
        logging.error(f"Port {port} - Unexpected error: {error}")
        return port, "ERROR"

    finally:
        sock.close()


def main():

    print("=" * 55)
    print("              TCP PORT SCANNER")
    print("=" * 55)

    host = input("Enter host/IP address: ").strip()

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if start_port < 1 or end_port > 65535:
            print("Error: Ports must be between 1 and 65535.")
            return

        if start_port > end_port:
            print("Error: Starting port cannot be greater than ending port.")
            return

    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print("\nStarting scan...")
    print(f"Host: {host}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Start time: {datetime.now()}")
    print("-" * 55)

    logging.info("=" * 50)
    logging.info(f"Scan started - Host: {host}")
    logging.info(f"Port range: {start_port}-{end_port}")

    open_ports = []
    closed_ports = []
    timeout_ports = []

    ports = range(start_port, end_port + 1)

    # Create multiple threads
    with ThreadPoolExecutor(max_workers=20) as executor:

        results = executor.map(
            scan_port,
            [host] * len(ports),
            ports
        )

        for port, status in results:

            print(f"Port {port:5} : {status}")

            logging.info(
                f"Host: {host} | Port: {port} | Status: {status}"
            )

            if status == "OPEN":
                open_ports.append(port)

            elif status == "CLOSED":
                closed_ports.append(port)

            elif status == "TIMEOUT":
                timeout_ports.append(port)

    print("-" * 55)

    print("\nSCAN SUMMARY")
    print("-" * 55)

    print(f"Open ports    : {len(open_ports)}")
    print(f"Closed ports  : {len(closed_ports)}")
    print(f"Timeout ports : {len(timeout_ports)}")

    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            print(f"  -> {port}")

    print("-" * 55)
    print(f"End time: {datetime.now()}")
    print("Results saved to: port_scanner.log")
    print("=" * 55)

    logging.info(f"Scan finished - Host: {host}")
    logging.info(f"Open ports: {open_ports}")
    logging.info("=" * 50)


if __name__ == "__main__":
    main()