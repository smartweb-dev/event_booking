import eventpro

print("Welcome To D’Atrium Halls Booking System")
def all_func_exec():
    for i in range(len(eventpro.user_action)):
        print(f"({i+1}) {eventpro.user_action[i]}")
    
    while True:
        try:
           choice = int(eventpro.check_empty_input("Choose from the options above: "))
           if choice > 0 and choice <= len(eventpro.user_action):
               choice_selection = eventpro.user_action[choice - 1]
               break
           else:
            print("Please select a valid number from the options above")
        except ValueError:
            print("Your option must be a Number")

    if choice_selection == 'Make a Booking':
        eventpro.make_bookings()  
    elif choice_selection ==  'Filter Events':
        time_slot = eventpro.check_empty_input("Enter a Time Slot: ").capitalize()
        eventpro.filter_events(time_slot)
    elif choice_selection == 'Reschedule an Event':
         phone_number = eventpro.get_valid_phone_number()
         eventpro.reschedule_event(phone_number)
    elif choice_selection =='Cancel a Booking':
        eventpro.cancel_booking()
    elif choice_selection == 'Complete a Booking':
        eventpro.complete_booking()
    elif choice_selection == 'Exit':
        return
    


     

all_func_exec()


# eventpro.manager_table()
# eventpro.manager_csv()

