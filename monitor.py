import time
import logging
import psutil

# Configure logging to save reports to a file
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define thresholds (in percentage)
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 85.0


def check_system_stats():
    print("Starting System Monitor... Press Ctrl+C to stop.")
    logging.info("System Monitor started.")

    try:
        while True:
            # Gather metrics
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage("/")

            # Display current stats on the terminal
            print(
                f"\r[CPU: {cpu_usage}%] | [Memory: {memory.percent}%] | [Disk: {disk.percent}%]",
                end="",
                flush=True,
            )

            # Log standard stats
            log_msg = f"CPU: {cpu_usage}%, Memory: {memory.percent}%, Disk: {disk.percent}%"
            logging.info(log_msg)

            # Check thresholds and trigger alerts
            if cpu_usage > CPU_THRESHOLD:
                alert_msg = (
                    f"HIGH CPU USAGE ALERT: {cpu_usage}% exceeds {CPU_THRESHOLD}%"
                )
                print(f"\n⚠️  {alert_msg}")
                logging.warning(alert_msg)

            if memory.percent > MEMORY_THRESHOLD:
                alert_msg = f"HIGH MEMORY USAGE ALERT: {memory.percent}% exceeds {MEMORY_THRESHOLD}%"
                print(f"\n⚠️  {alert_msg}")
                logging.warning(alert_msg)

            if disk.percent > DISK_THRESHOLD:
                alert_msg = (
                    f"HIGH DISK USAGE ALERT: {disk.percent}% exceeds {DISK_THRESHOLD}%"
                )
                print(f"\n⚠️  {alert_msg}")
                logging.warning(alert_msg)

            # Wait for 5 seconds before the next check
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nSystem Monitor stopped by user.")
        logging.info("System Monitor stopped by user.")
if __name__ == "__main__":
    check_system_stats()
    