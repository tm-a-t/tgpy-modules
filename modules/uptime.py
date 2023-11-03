from datetime import datetime

start_time = datetime.now()


def uptime():
    return datetime.now() - start_time
