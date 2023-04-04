import re

'''Function to convert a string time value to an int representing the total number of minutes'''
def str_to_int(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

'''Function to convert an int value representing the total number of minutes to a string representing the time'''
def int_to_str(number):
    h = number // 60
    m = number % 60
    return f"{h}:{m:02}"

'''Having the start time and the end of a free time meeting interval, adds it to the solution'''
def add_time(lower, upper, meeting_times):
    t1 = int_to_str(lower)
    t2 = int_to_str(upper)
    meeting_times.append([t1, t2])
    return meeting_times

'''After the iterations in the activity calendars, if any calendar was not fully explored,
finishes the list and looks for any left interals of free time'''
def finish_calendar(index, calendar, meeting_times):
    while index < len(calendar) - 1:
        current_end = str_to_int(calendar[index][1])
        next_start = str_to_int(calendar[index + 1][0])
        if next_start - current_end >= meet_time_minutes:
            meeting_times = add_time(current_end, next_start, meeting_times)
        index += 1
    return meeting_times

'''Initial problem data'''
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
range_limit1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '13:30'], ['14:30', '15:00'], ['16:00', '17:00']]
range_limit2 = ['10:00', '18:30']
meet_time_minutes = 30

i = 0
j = 0
meeting_times = []

'''Case 1: a free time interval can be made between the lower calendar range limits
and the start of each calendar's program'''
low_limit1 = str_to_int(range_limit1[0])
low_limit2 = str_to_int(range_limit2[0])
start1 = str_to_int(calendar1[0][0])
start2 = str_to_int(calendar2[0][0])
# Check if there is enough time for a meeting to happen between two time ranges.
# If the difference between the lower range limits and the start hour of each calendar
# is greater or equal to the meeting time minutes value, a meeting can be scheduled.
if start1 - low_limit1 >= meet_time_minutes:
    if start2 - low_limit2 >= meet_time_minutes:
        t1 = int_to_str(max(low_limit1, low_limit2))
        t2 = int_to_str(min(start1, start2))
        if t1 != t2 and low_limit1 < start2 and low_limit2 < start1:
            meeting_times.append([t1, t2])

'''Case 2: find the free time intervals between the activity intervals of the two calendars'''
while i < len(calendar1) - 1 and j < len(calendar2) - 1:
    current_start1 = str_to_int(calendar1[i][0])
    current_start2 = str_to_int(calendar2[j][0])
    current_end1 = str_to_int(calendar1[i][1])
    current_end2 = str_to_int(calendar2[j][1])
    next_start1 = str_to_int(calendar1[i + 1][0])
    next_start2 = str_to_int(calendar2[j + 1][0])
    next_end1 = str_to_int(calendar1[i + 1][0])
    next_end2 = str_to_int(calendar2[j + 1][0])

    # If the end of the first person's next time slot is earlier than the start of the second person's
    # current time slot, there is free time, so add it to the meeting_times list
    if next_end1 < current_start2:
        meeting_times = add_time(current_end1, next_start1, meeting_times)
        i += 1
    else:
        # If the end of the second person's next time slot is earlier than the start of the first person's
        # current time slot, there is free time, so add it to the meeting_times list
        if next_end2 < current_start1:
            meeting_times = add_time(current_end2, next_start2, meeting_times)
            j += 1
        else:
            if next_start1 - current_end1 >= meet_time_minutes:
                if next_start2 - current_end2 >= meet_time_minutes:
                    meeting_times = add_time(max(current_end1, current_end2), min(next_start1, next_start2), meeting_times)
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                i += 1
# If there are any remaining time slots in either person's calendar, add them to the meeting_times list
meeting_times = finish_calendar(i, calendar1, meeting_times)
meeting_times = finish_calendar(j, calendar2, meeting_times)

'''Case 3: a last free time interval might be made between the end of each calendar's frogram and the upper range limits'''
high_limit1 = str_to_int(range_limit1[1])
high_limit2 = str_to_int(range_limit2[1])
end1 = str_to_int(calendar1[i][1])
end2 = str_to_int(calendar2[j][1])
if high_limit1 - end1 >= meet_time_minutes:
    if high_limit2 - end2 >= meet_time_minutes:
        x = int_to_str(max(end1, end2))
        y = int_to_str(min(high_limit1, high_limit2))
        if x != y and high_limit1 > end2 and high_limit2 > end1:
            meeting_times.append([x, y])

print(meeting_times)