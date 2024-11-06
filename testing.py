from datetime import datetime,timedelta
import calendar

# Get the current date
# current_date = datetime.now()

# # Get the current month
# current_month = current_date.month
# print(current_month)
# remaining_months = []
# # Print the remaining months using %b for abbreviated month names
# print("Remaining months of the year:")
# for month in range(current_month, 13):  # 13 to include December
#     month_name = datetime(current_date.year, month, 1).strftime('%b')
#     remaining_months.append(month_name)
#     print(remaining_months)






# Get the current month
# current_month = datetime.now().month

# # Print the remaining abbreviated months of the year
# print("Remaining months of the year:")
# remaining_months = [calendar.month_name[i][:3] for i in range(current_month, 13)]
# print(remaining_months)
# for month in remaining_months:
#     print(month)



# # Get the current date
# today = datetime.now()

# # Get the current year and month
# current_year = today.year
# current_month = today.month

# Calculate the last day of the current month
# if current_month == 12:
#     last_day = datetime(current_year + 1, 1, 1) - timedelta(days=1)
# else:
#     last_day = datetime(current_year, current_month + 1, 1) - timedelta(days=1)

# # Print the remaining days in the current month
# print("Remaining days in the current month:")
# for day in range(today.day, last_day.day + 1):
#     print(day)


# Get the current date
# today = datetime.now()

# # Get the current year and month
# current_year = today.year
# current_month = today.month

# # Calculate the last day of the current month
# last_day = calendar.monthrange(current_year, current_month+1)[1]
# print(last_day)

# Print the remaining days in the current month
# print("Remaining days in the current month:")
# remaining_days = []
# for day in range(today.day, last_day+1):
#     remaining_days.append(day)
# print(remaining_days)


# first_weekday, num_days = calendar.monthrange(2024, 10)
# print(first_weekday)  # Output: 0 (Monday)
# print(num_days)       # Output: 31


# def days_left():
#     today = datetime.now()
#     current_year = today.year
#     current_month = today.month
#     today_day = today.day
    
#     all_days = {}
    
#     # Get the current month index and create a list of remaining months
#     remaining_months = [calendar.month_name[i] for i in range(current_month, 13)]
    
#     for month_index, month_name in enumerate(remaining_months, start=current_month):
#         if month_index == current_month:  # If it's the current month
#             last_day = calendar.monthrange(current_year, month_index)[1]
#             days_list = [day for day in range(today_day, last_day + 1)] 
#         else:  # For future months
#             last_day = calendar.monthrange(current_year, month_index)[1]
#             days_list = [day for day in range(1, last_day + 1)]
        
#         all_days[month_name] = days_list  
    
#     print(all_days)
#     return all_days

# Call the function to test it
# days_left()

days = (1,2,3,4,5,6,7,8,9,10)
print(len(days))




