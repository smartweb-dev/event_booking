import sqlite3
from datetime import datetime
import calendar
import csv
import pandas as pd




# conn = sqlite3.connect('events.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM future_events")
# conn.commit()
# conn.close

def check_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")



user_action = ['Make a Booking','Filter Events','Reschedule an Event', 'Cancel a Booking','Complete a Booking','Exit']
timeSlot = ['Morning','Afternoon','Evening']
def choose_time_slot():
    for i in range(len(timeSlot)):
        print(f"({i+1}) {timeSlot[i]}")
    while True:  
            try:
                choice = int(check_empty_input("Select Time slot from the option above: "))
                if choice >= 1 and choice <= len(timeSlot):
                    time_slot = timeSlot[choice - 1]
                    return time_slot
                else:
                        print("Please select a valid number from the options above.")
            except ValueError:
                     print("Event type can only be a number.")


sub_type = ['Private','Corporate','Sponsored']
event_type = ['Book Launch','Fundraiser','Social Event/Gala Nite','Social/Networking','Birthday','Meeting','Social Event/Comedy','Conference','Entertainment','Camp Out','Seminar']
hall_list = {"Moyeni hall":1,"Bimpe hall":2,"Ade hall":3,"Azeez Hall":4, "Muyiwa hall":5, "Adeola hall":6}
current_month = datetime.now().month
remaining_months = [calendar.month_name[i][:3] for i in range(current_month,13)]
def days_left(user_month):
    current_year = datetime.now().year
    today = datetime.now().day
    all_days = {}
    for month_index, month_name in enumerate(remaining_months, current_month):
        if month_index == current_month:  # If it's the current month
            last_day = calendar.monthrange(current_year, month_index)[1]
            days_list = [day for day in range(today, last_day + 1)] 
        else:  
            last_day = calendar.monthrange(current_year, month_index)[1]
            days_list = [day for day in range(1, last_day + 1)]
        all_days[month_name] = days_list 
    for key in all_days.keys():
        if key == user_month:
            list_of_days = all_days[key]
            return list_of_days
                

        

# days_left('Nov')

def choose_day(days_left_arg):
    all_days = days_left(days_left_arg)
    for day in all_days:
        print(day)
    while True:  
        try:
            choice = int(check_empty_input("Select Day of the event from the options above: "))
            if choice >= 1 and choice <= len(all_days):
                user_day = choice
                return user_day
            else:
                 print("Please select a valid number from the options above.")
        except ValueError:
            print("Day can only be a number.")


# print(choose_day("Nov"))


def choose_event_type():
    for i in range(len(event_type)):
        print(f"({i+1}) {event_type[i]}")
    while True:  
        try:
            choice = int(check_empty_input("Select event type from the options above: "))
            if choice >= 1 and choice <= len(event_type):
                eventChoice = event_type[choice - 1]
                return eventChoice
            else:
                 print("Please select a valid number from the options above.")
        except ValueError:
            print("Event type can only be a number.")


def choose_event_subtype():
    for i in range(len(sub_type)):
        print(f"({i+1}) {sub_type[i]}")
    while True:
        try:
            choice = int(check_empty_input("Select event sub type from the options above: "))
            if choice >=1 and choice <= len(sub_type):
                subChoice = sub_type[choice - 1]
                return subChoice
            else:
                print("Please select a valid number from the options above.")
        except ValueError:
            print("Event sub type can only be a number.")


def choose_hall():
    hall_key = list(hall_list.keys())
    for i in range(len(hall_key)):
        print(f"({i+1}) {hall_key[i]}")
    while True:
        try:
            choice = int(check_empty_input("Select Hall from the options above: "))
            if choice >= 1 and choice <= len(hall_key):
                hallOption = hall_list[hall_key[choice - 1]]
                return hallOption
            else:
                print("Please select a valid number from the options above.")
        except ValueError:
            print("Hall choice can only be number")


def choose_month():
    for i in range(len(remaining_months)):
        print(f"({i+1}) {remaining_months[i]}")
    while True:
        try:
            choice = int(check_empty_input("Select month from the options above: "))
            if choice >= 1 and choice <= len(remaining_months):
                month_selection = remaining_months[choice - 1]
                return month_selection
            else:
                print("Please select a valid number from the options above.")
        except ValueError:
            print("Your selection must be a number")




def booking_availability(month,day,hall,time_slot):
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM quarter_events WHERE Month=? AND Day_in_month=? AND Hall=? AND Time_slot=?""",(month,day,hall,time_slot))
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False

# print(booking_availability("Jul",10,3,"Morning"))

# choose_month()
# choose_hall()
# choose_event_subtype()
# choose_event_type()
def make_bookings():
    eventName = check_empty_input("What is the Event name? ").capitalize()
    eventType = choose_event_type()
    subType = choose_event_subtype()
    while True:    
          month_of_year  = choose_month()
          day_of_month = choose_day(month_of_year)
          hall_name = choose_hall()
          time_slot = choose_time_slot()

          if booking_availability(month_of_year, day_of_month, hall_name, time_slot):
              print("The selected date is not available. Please choose a different option.")
          else:
             break      

    user_name = check_empty_input("Enter a username: ")
    user_phone = check_empty_input("Enter your phone number in this format 090/081/070 etc: ")
    payment_question = check_empty_input("would you like to make payment now. Answer with Yes/No: ").capitalize()
    if payment_question == "Yes":
        paymentStatus = "Confirmed"
        event_status = "Completed"
    elif payment_question == "No":
        paymentStatus = "Pending"
        event_status = "Pending"
    else:
        print("Invalid input")

    # if booking_availability(month_of_year,day_of_month,hall_name,time_slot) == True:
    #     print("The seleted date is not available.")
    #     return

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO quarter_events(Event_Name,Event_Type,'Sub-type',Month,Day_in_month,Hall,Time_slot,Username,Userphone,Event_Status,Payment_status)VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(eventName,eventType,subType,month_of_year,day_of_month,hall_name,time_slot,user_name,user_phone,event_status,paymentStatus))
    conn.commit()
    conn.close()


    
# make_bookings()


def filter_events(time_slot):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quarter_events WHERE Time_slot = ?",(time_slot,))
    query = "SELECT * FROM quarter_events WHERE Time_slot = ?"
    table = pd.read_sql_query(query, conn, params=(time_slot,))
    rows = cursor.fetchall()
    if rows:
         print(table)
    else:
        print("We don't have any data with that time slot in our database.")
    conn.close()



def reschedule_event(phone_number):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quarter_events WHERE Userphone=?",(phone_number,))
    rows = cursor.fetchall()
    if rows:
        while True:    
          month_of_year  = choose_month()
          day_of_month = choose_day(month_of_year)
          hall_name = choose_hall()
          time_slot = choose_time_slot()

          if booking_availability(month_of_year, day_of_month, hall_name, time_slot):
              print("The selected date is not available. Please choose a different option.")
          else:
             break
        final_question = check_empty_input("Are you sure you want to make this changes?answer with Yes or no:  ").capitalize()
        if final_question == "Yes":
            cursor.execute("""UPDATE quarter_events SET Month=?, Day_in_month=?,Hall=?,Time_slot=? WHERE Userphone=?""",(month_of_year,day_of_month,hall_name,time_slot,phone_number))
            conn.commit()
            print("Your Booking have been rescheduled")
        elif final_question =="No":
            print("your booking was not reschedule")
        else:
            print("Invalid input")
            return
    else:
        print("the phone number does not exist in the database.")
    conn.close()
    
    

# reschedule_event("07053426372")   


def cancel_booking():
    user_phone = check_empty_input("Enter your phone number ")
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quarter_events WHERE Userphone=?",(user_phone,))
    result = cursor.fetchone()
    
    if result:
        cancel = check_empty_input("Are you sure you want to cancel your booking?Answer with Yes/No ").capitalize()
        if cancel == "Yes":
            cursor.execute("UPDATE quarter_events SET Event_Status =?,Payment_status=? WHERE Userphone=?",("Cancelled","Cancelled",user_phone))
            cursor.execute("DELETE FROM future_events WHERE userphone=?",(user_phone,))
            conn.commit()
            print("Your booking have been cancelled")
    else:
        print("There is no data with that phone number in our database")
    
    conn.close()

# cancel_booking()

def future_bookings():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE future_events(event_name TEXT,event_type TEXT,sub_type TEXT,month TEXT,day NUMERIC,hall INTEGER,time_slot TEXT,username TEXT,userphone TEXT,event_status TEXT,payment_status TEXT)""")
    conn.commit()
    print("Table have been successfully created")
    conn.close()

# future_bookings()

def month_abbr_to_number(month_abbr):
    try:
        return datetime.strptime(month_abbr, '%b').month
    except ValueError:
        return None 


def manager_table():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    month = datetime.now().month
    day = datetime.now().day
    cursor.execute("SELECT * FROM quarter_events")
    rows = cursor.fetchall()
    all_rows = []


    for row in rows:
        if month_abbr_to_number(f"{row[3]}") >= month and row[4] > day and row[9] == "Completed"   :
           print(row[9])
           all_rows.append(row)
    if all_rows != []:
        for i in range(len(all_rows)):
            eventName = all_rows[i][0]
            eventType = all_rows[i][1]
            subType = all_rows[i][2]
            month_of_year = all_rows[i][3]
            day_of_month = all_rows[i][4]
            hall_name = all_rows[i][5]
            Time_slot = all_rows[i][6]
            user_name = all_rows[i][7]
            user_phone = all_rows[i][8]
            eventStatus = all_rows[i][9]
            PaymentStatus = all_rows[i][10]
            cursor.execute("""
                SELECT 1 FROM future_events
                WHERE event_name = ? AND month = ? AND day = ? AND time_slot=?
            """, (eventName, month_of_year, day_of_month,Time_slot))

            if not cursor.fetchone():
                cursor.execute("""INSERT INTO future_events(event_name,event_type,sub_type,month,day,hall,time_slot,username,userphone,event_status,payment_status) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(eventName,eventType,subType,month_of_year,day_of_month,hall_name,Time_slot,user_name,user_phone,eventStatus,PaymentStatus))
                conn.commit()
    else:
        print("There is no booking Available")
        

    conn.close()


    



def complete_booking():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    user_phone = check_empty_input("Enter your Phone number: ")
    cursor.execute("SELECT * FROM quarter_events WHERE Userphone = ?",(user_phone,))
    row = cursor.fetchone()
    if row:
        if row[9] == 'Pending':
            print("Your booking status is pending which mean you are yet to make payment")
            question = check_empty_input("Would you like to make payment now? Yes/No").capitalize()
            if question == "Yes":
                eventStatus = "Completed"
                paymentStatus = "Confirmed"
                cursor.execute("UPDATE quarter_events SET Event_Status=?,Payment_status=? WHERE Userphone=?",(eventStatus,paymentStatus,user_phone))
                conn.commit()
                print("Your payment have been confirmed")
            else:
                return
        elif row[9] == "Completed":
            print("Your Booking has already been confirmed")
        else:
            print("Your booking have been canceled")
    else:
        print("No Data")
    conn.close()

# complete_booking()

def all_data():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quarter_events")
    rows = cursor.fetchall()
    # table = pd.DataFrame({'event_name':[item[0] for item in rows],'event_type':[item[1] for item in rows],'sub_type':[item[2] for item in rows],'month':[item[3] for item in rows],'day':[item[4] for item in rows],'hall':[item[5] for item in rows],'time_slot':[item[6] for item in rows],'username':[item[7] for item in rows],'userphone':[item[8] for item in rows],'event_status':[item[9] for item in rows],'payment_status':[item[10] for item in rows]})
    table = pd.read_sql_query("SELECT * FROM quarter_events",conn)
    if rows:
        print(table)
    conn.close()


# all_data()


def manager_csv():
 
  conn = sqlite3.connect('events.db')
  cursor = conn.cursor()
  query = "SELECT * FROM future_events"
  cursor.execute(query)
  columns = [description[0] for description in cursor.description]
  rows = cursor.fetchall()
  
  with open('manage_data.csv', 'w') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(columns)
      writer.writerows(rows)

  table = pd.read_sql_query("SELECT * FROM future_events",conn)
  print(table)
  conn.close()


# manager_table()
# manager_csv()


