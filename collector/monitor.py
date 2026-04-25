import psutil
import time
import csv
from datetime import datetime

FILE = "data/metrics.csv"

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), cpu, memory, disk])

    print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    time.sleep(5)