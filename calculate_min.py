time_value = float(input("Enter time value: "))

in_minutes = int(time_value*60)

in_hours = int(in_minutes//60)

minutes = int((time_value - in_hours)* 60)

if __name__ == '__main__':

    print(f"You have been working for {in_minutes} minutes or {in_hours}h and {minutes} min.")

if in_hours >= 8:
    too_many_minutes = in_minutes - 480
    remainder_hours = 0
    remainder_minutes = 0
    print(f"You are over your work limit by {too_many_minutes} minutes.")
elif in_hours < 8 and minutes == 0:
    remainder_hours = 8 - in_hours
    remainder_minutes = minutes
    too_many_minutes = 0
    print(f"You have {remainder_hours}h left to work (without breaks).")
else:
    remainder_hours = 7 - in_hours
    remainder_minutes = 60 - minutes
    too_many_minutes = 0
    print(f"You have {remainder_hours}h and {remainder_minutes} min left to work (without breaks).")
