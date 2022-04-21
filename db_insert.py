import sqlite3
import db_view
import db_table
import time

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")

def database_insert():
    
    CLR = "\x1B[0K"
    record = []
    possible_choices = ['P', 'C', 'H', 'R', '']
    switch = 0

    connection = sqlite3.connect('my_database.db')

    cursor = connection.cursor()
    
    record_choice = ''
    
    
    chosen_table = db_table.which_table()
    if chosen_table == 'Menu':
        return 'cancelled'
    elif chosen_table == 'People':
        switch = 1
        record_choice = 'P'
    elif chosen_table == 'Courses':
        switch = 2
        record_choice = 'C'
    elif chosen_table == 'Cohorts':
        switch = 3
        record_choice = 'H'
    elif chosen_table == 'Registrations':
        switch = 4
        record_choice = 'R'
    
    CLEAR_ALL()
    
    print("Please complete the following:\n"
          "------------------------------\n"
    )
    
    # Create a record in the Cohorts table or the Student_Cohorts_Registrations table:
    if switch == 3 or switch == 4:
        error_message = 0
        if switch == 3:
            variables_list = ['instructors', 'Courses', 'course_id', 'starting', 'n ending', 'Cohorts',
                              'instructor_id, course_id, start_date, end_date', '?, ?, ?, ?']
        elif switch == 4:
            variables_list = ['students', 'Cohorts', 'cohort_id', 'registration', ' completion', 'Student_Cohort_Registrations',
                              'student_id, cohort_id, registration_date', '?, ?, ?']
        
        while True:
            print()
            db_view.database_view('People')
            person = input(f"\nPlease choose from the above list of {variables_list[0]}: \n"
                            f"(Choose by entering ID of {variables_list[0]})\n"
                            "\n>>> \n"
                            "\nHit ENTER now to Cancel and Return to MAIN MENU.\x1b[2A\x1b[44D"
            )
            if person == '':
                return 'cancelled'
            try:
                person = int(person)
                chosen_person = cursor.execute("SELECT person_id FROM People WHERE person_id=? AND active=1", (person,)).fetchone()
                error_message = 0
            except:
                error_message = 1
                if error_message == 1:
                    print("Invalid Entry, Please Try Again")
            
            if error_message == 0:
                break
                
        while True:
            print()
            print()
            print()
            db_view.database_view(variables_list[1])
            course_or_cohort = input(f"\nPlease choose from the above list of {variables_list[1]}: \n"
                            f"(Choose by entering ID of {variables_list[1]})\n"
                            "\n>>> \n"
                            "\nHit ENTER now to Cancel and Return to MAIN MENU.\x1b[2A\x1b[44D"
            )
            if course_or_cohort == '':
                return 'cancelled'
            try:
                course_or_cohort = int(course_or_cohort)
                chosen_course_or_cohort = cursor.execute(f"SELECT {variables_list[2]} FROM {variables_list[1]} WHERE {variables_list[2]}=? AND active=1", (course_or_cohort,)).fetchone()
                error_message = 0
            except:
                error_message = 1
                if error_message == 1:
                    print("Invalid Entry, Please Try Again")
            
            if error_message == 0:
                break
        
        # Cohort table row - start_date; Student_Cohort_Registrations table row - registration_date:
        start_day = input(f"\nPlease enter a {variables_list[3]} date:\n"
                            "(Must be in format YYYYMMDD)\n"
                            ">>> "
        )
        if switch == 3:
            # Cohort table row - end_date:
            end_day = input(f"\nPlease enter an ending date:\n"
                                "(Must be in format YYYYMMDD)\n"
                                ">>> "
            )
        # Row needed if adding a record to Student_Cohort_Registrations table: (actually not needed unless deactivating a registration)
        # if record_choice.upper() == 'R':
        #     drop_day = input("\nPlease enter a drop date:\n"
        #                         "(Must be in format YYYYMMDD)\n"
        #                         ">>> "
        #     )
        
        cohort_or_registration_list = [int(chosen_person[0]), int(chosen_course_or_cohort[0]), start_day]
        
        if switch == 3:
            cohort_or_registration_list.append(end_day)

        cursor.execute(f"INSERT INTO {variables_list[5]} ({variables_list[6]}) VALUES({variables_list[7]})", cohort_or_registration_list)

        if record_choice.upper() == 'H':
            finished_cohort = cursor.execute("SELECT cohort_id FROM Cohorts WHERE instructor_id=? AND course_id=? AND start_date=? AND end_date=?", cohort_or_registration_list).fetchone()
            print(f'\nSUCCESS: Cohort "{finished_cohort[0]}" Successfully added!')
        elif record_choice.upper() == 'R':
            finished_registration = cursor.execute("SELECT first_name, last_name FROM People WHERE person_id=?", chosen_person).fetchone()
            print(f'\nSUCCESS: Registration succesfully completed for student "{finished_registration[0]}" into cohort "{chosen_course_or_cohort[0]}"!')
        
        connection.commit()
        
        return
    
    
    
    while True:
        # Gets info to make a record in the People table:
        if record_choice.upper() in possible_choices:
            if record_choice.upper() == 'P':
                record.append((input("1st Name : \nSurname  : \nEmail    : \nPhone    : \nPassword : \nAddress  : \nCity     : \nST(Abbr) : \nZipCode  : \n \nHit ENTER now to return to MAIN MENU. \nOtherwise, you must finish form.\x1B[11A\x1b[21D")).title())
                if record[0] == '':
                    return 'cancelled'
                print(f'{CLR}', end='')
                record.append((input("Surname  : \nEmail    : \nPhone    : \nPassword : \nAddress  : \nCity     : \nST(Abbr) : \nZipCode  : \x1B[7A")).title())
                print(f'{CLR}', end='')
                record.append(input("Email    : \nPhone    : \nPassword : \nAddress  : \nCity     : \nST(Abbr) : \nZipCode  : \x1B[6A"))
                print(f'{CLR}', end='')
                record.append(input("Phone    : \nPassword : \nAddress  : \nCity     : \nST(Abbr) : \nZipCode  : \x1B[5A"))
                print(f'{CLR}', end='')
                record.append(input("Password : \nAddress  : \nCity     : \nST(Abbr) : \nZipCode  : \x1B[4A"))
                print(f'{CLR}', end='')
                record.append(input("Address  : \nCity     : \nST(Abbr) : \nZipCode  : \x1B[3A"))
                print(f'{CLR}', end='')
                record.append(input("City     : \nST(Abbr) : \nZipCode  : \x1B[2A"))
                print(f'{CLR}', end='')
                record.append((input("ST(Abbr) : \nZipCode  : \x1B[1A")).upper())
                print(f'{CLR}', end='')
                record.append(input("ZipCode  : "))
                break
            # Gets info to make a record in the Courses table:
            elif record_choice.upper() == 'C':
                record.append((input("Course Name : \nDescription : \n \nHit ENTER now to return to MAIN MENU. \nOtherwise, you must finish form.\x1B[4A\x1b[18D")).title())
                if record[0] == '':
                    return 'cancelled'
                print(f'{CLR}', end='')
                record.append(input("Description : "))
                break
        else:
            print("Invalid Entry, Please Try Again")
    
    
    if record_choice.upper() == 'P':
        cursor.execute("INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", record)
    elif record_choice.upper() == 'C':
        cursor.execute("INSERT INTO Courses (name, description) VALUES(?, ?)", record)
        
    connection.commit()
    
    print(f'\nSUCCESS: "{record[0]}" Successfully added!')
    
    return


