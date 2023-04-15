def add_time(start, duration, day=None):
    start_time_split = start.split(':')
    start_time_hour = int(start_time_split[0])
    start_time_mins = int(start_time_split[1][:2])
    am_or_pm = start_time_split[1][-2:].strip()

    day_of_week = ['Monday', 'Tuesday', 'Wednesday',
                   'Thursday', 'Friday', 'Saturday', 'Sunday']

    if am_or_pm == 'PM' and start_time_hour != 12:
        start_time_hour += 12

    duration_split = duration.split(':')
    duration_hour = int(duration_split[0])
    duration_mins = int(duration_split[1])

    start_mins_total = start_time_hour * 60 + start_time_mins
    duration_mins_total = duration_hour * 60 + duration_mins

    new_mins_total = start_mins_total + duration_mins_total

    num_days_later = new_mins_total // 1440
    new_mins_total %= 1440

    new_hour = new_mins_total // 60
    new_mins = new_mins_total % 60
    new_am_or_pm = 'AM' if new_hour < 12 else 'PM'
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12

    if new_hour < 10:
        new_time_solution = f'{new_hour}:{new_mins:02d} {new_am_or_pm}'
    else:
        new_time_solution = f'{new_hour:02d}:{new_mins:02d} {new_am_or_pm}'

    if day:
        start_day_idx = day_of_week.index(day.capitalize())
        curr_day_idx = (start_day_idx + num_days_later) % 7

        if num_days_later == 0:
            new_time = str(new_time_solution) + ', ' + \
                str(day_of_week[curr_day_idx])
        elif num_days_later == 1:
            new_time = str(new_time_solution) + ', ' + \
                str(day_of_week[curr_day_idx]) + ' (next day)'
        else:
            new_time = str(new_time_solution) + ', ' + str(day_of_week[curr_day_idx]) + ' ' + '(' + \
                str(num_days_later) + ' days later)'
    else:
        if num_days_later == 0:
            new_time = new_time_solution
        elif num_days_later == 1:
            new_time = str(new_time_solution) + ' (next day)'
        else:
            new_time = str(new_time_solution) + ' ' + \
                '(' + str(num_days_later) + ' days later)'

    return new_time
