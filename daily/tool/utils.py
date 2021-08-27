from datetime import datetime
import time


def get_date_diff_days(begin: time.time, days=1):
    """
    获取开始日期的两个时间
    begin:开始日期
    days:相隔天数
    """
    now_time = int(begin)
    day_time = now_time - now_time % 86400 + time.timezone
    day_time_end = day_time + 86400 * (days - 1) + 86399
    print(datetime.fromtimestamp(day_time))
    print(datetime.fromtimestamp(day_time_end))
    return datetime.fromtimestamp(day_time),datetime.fromtimestamp(day_time_end)


def get_now_datetime():
    """
    获取中国当前日期时间
    """
    now = datetime.fromtimestamp(time.time())
    print(f"now={now}")
    return now


def get_today_str():
    d = datetime.today()
    return d.strftime('%Y%m%d')
