#!/usr/bin/python3

from datetime import datetime


def time_since_timestamp_str(timestamp_str, timestamp_format):
    timestamp_dt = datetime.strptime(timestamp_str, timestamp_format)
    now = datetime.utcnow()
    delta = now - timestamp_dt
    return delta

