import psutil
import platform
import socket
import time

# Record application start time
START_TIME = time.time()


def get_system_metrics():
    uptime_seconds = int(time.time() - START_TIME)

    return {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "uptime_seconds": uptime_seconds,
    }