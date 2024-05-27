import psutil
import time
import csv
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


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


def visualize_data(input_file):
    data = pd.read_csv(input_file)
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(data['timestamp'], data['cpu_usage'], label='CPU Usage (%)')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Over Time')
    plt.xticks(rotation=45)
    plt.legend()

    plt.subplot(2, 1, 1)
    plt.plot(data['timestamp'], data['memory_usage'], label='Memory Usage (%)', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Memory Usage (%)')
    plt.title('Memory Usage Over Time')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

print('Tracking...')
collect_data(interval=5, duration=60, output_file='usage_log.csv')
print('Tracking stopped.')

print('Plotting...')
visualize_data(input_file='usage_log.csv')
print('Completed.')
