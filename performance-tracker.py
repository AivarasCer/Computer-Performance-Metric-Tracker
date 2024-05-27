import psutil
import time
import csv
from datetime import datetime


def collect_data(interval, duration, output_file):
    end_time = time.time() + duration
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'cpu_usage', 'memory_usage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while time.time() < end_time:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            writer.writerow({'timestamp': timestamp,
                             'cpu_usage': cpu_usage,
                             'memory_usage': memory_usage})
            time.sleep(interval - 1)

print('Tracking...')
collect_data(interval=5, duration=60, output_file='usage_log.csv')

