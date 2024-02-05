from datetime import datetime, timedelta
import calendar
#  from lunarcalendar import Converter, Solar

def find_next_overlap(start_year, target_month, target_day, lunar_month, lunar_day):
    """
    查找下一次农历的某月某日与公历的某月某日重合的年份。
    start_year: 开始搜索的年份
    target_month, target_day: 目标公历的月和日
    lunar_month, lunar_day: 目标农历的月和日
    """

    # 从开始年份起，逐年检查农历的正月十二是否为公历的2月21日
    for year in range(start_year, start_year + 80):  # 假设在接下来的200年内总能找到一个匹配
        try:

            solar_date = Solar(year, lunar_month, lunar_day)  # 这里以2024年2月14日为例

            lunar_date = Converter.Solar2Lunar(solar_date)
            print(lunar_date)
            if target_month == lunar_date.month and target_day == lunar_date.day:
                print(year) # 找到重合的年份
        except Exception as e:
            print(f"Error converting year {year}: {e}")
            # 在某些年份，可能因为闰月等原因导致转换失败

    return None  # 如果没有找到，返回None

birthyear = 2000
find_next_overlap(birthyear, 9, 28, 10, 25)