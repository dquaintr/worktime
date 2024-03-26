from calculate_min import remainder_minutes, remainder_hours, too_many_minutes
from datetime import datetime, timedelta

def add_time_to_current(hours, minutes):
    # Get the current time
    current_time = datetime.now()

    # Create a timedelta object for the specified hours and minutes
    time_delta = timedelta(hours = hours, minutes = minutes)

    # Add the timedelta to the current time
    new_time = current_time + time_delta
    return(new_time.strftime("%H:%M"))

def take_time_from_current(too_many_minutes):
    current_time = datetime.now()

    hours_over_time = int(too_many_minutes // 60)

    minutes_over_time = int((too_many_minutes - (hours_over_time * 60)))
    # Create a timedelta object for the specified hours and minutes

    time_delta = timedelta(hours=hours_over_time, minutes=minutes_over_time)

    # Add the timedelta to the current time
    new_time = current_time - time_delta
    return (new_time.strftime("%H:%M"))

if too_many_minutes == 0:
    feierabend = add_time_to_current(remainder_hours,remainder_minutes)
    print(f"You will finish your work at {feierabend}.")
else:
    feierabend = take_time_from_current(too_many_minutes=too_many_minutes)
    print(f"You should have finished your work at {feierabend}.")
