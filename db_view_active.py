import sqlite3
import db_view
import quick_search

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")

def view_active(the_switch, the_label, row_checker, search_mode=0):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    verification_list = []
    active_ins = [" ", " ", "to see all active cohorts for a chosen course", "to see all active registrations for a chosen cohort", ]
    
    while True:
        if the_switch == 1 or search_mode == 1:
            break
        search = input(f"\nPlease enter an exact ID {active_ins[the_switch]}, or\n"
                        "to resume previous search, press 'Enter'.\n"
                        "\n>>> "
        )
        if search == '':
            return 'cancelled'
        
        try:
            search_int = int(search)
        except:
            print("\nInvalid Entry: Non-Numeric Characters Entered. Please Try Again.\n")
            continue
          
        for i in row_checker:
            i = [str(x) for x in i]
            verification_list.append(i[0])
        
        if search in verification_list:
            break
    

    if the_switch == 1 or search_mode == 0:
        while True:
            the_question = input("\nWould you like to view only ACTIVE records? (Y/N)\n"
                                "\n>>> ")
            print()
            yes_or_no = ['Y', 'N']
            if the_question.upper() in yes_or_no:
                if the_question.upper() == 'Y':
                    break
                elif the_question.upper()== 'N':
                    return 'cancelled'
                
        
        rows = cursor.execute("SELECT * FROM People WHERE active=1").fetchall()
        
    if the_switch != 1 and search_mode == 1:
        while True:
            the_question = input("\nWould you like to view only ACTIVE records? (Y/N)\n"
                                "\n>>> ")
            print()
            yes_or_no = ['Y', 'N']
            if the_question.upper() in yes_or_no:
                if the_question.upper() == 'Y':
                    break
                elif the_question.upper()== 'N':
                    main_menu = input("\n<Press 'Enter' to return to Main Menu>")
                    if main_menu == '': 
                        return 'cancelled'
                    else:
                        return 'cancelled'
            
    if the_switch == 2:
        if search_mode == 1:
            rows = cursor.execute("SELECT coh.* FROM Cohorts coh WHERE coh.active=1").fetchall()
        else:
            rows = cursor.execute("SELECT coh.*, p.first_name, p.last_name, c.name FROM People p JOIN Cohorts coh ON p.person_id = coh.instructor_id JOIN Courses c ON c.course_id = coh.course_id WHERE coh.active=1 AND c.course_id=?", (search,)).fetchall()
    elif the_switch == 3:
        if search_mode == 1:
            # rows = cursor.execute("SELECT scr.* FROM Student_Cohort_Registrations scr WHERE scr.active=1").fetchall()
            rows = cursor.execute('''
                SELECT scr.*, p.first_name as student_fn, p.last_name as student_ln, i.instructor_pid, i.instructor_fn, i.instructor_ln
                FROM Student_Cohort_Registrations scr
                JOIN People p
                ON scr.student_id = p.person_id
                JOIN
                    (SELECT ch.*, pi.person_id as instructor_pid, pi.first_name as instructor_fn, pi.last_name as instructor_ln
                    FROM Cohorts ch
                    JOIN People pi
                    ON ch.instructor_id = pi.person_id) as i
                ON scr.cohort_id = i.cohort_id;
            ''').fetchall()
        else:
            rows = cursor.execute("SELECT scr.*, p.first_name, p.last_name FROM Student_Cohort_Registrations scr JOIN People p ON p.person_id = scr.student_id WHERE scr.active=1 AND cohort_id=?", (search,)).fetchall()
    elif the_switch == 4:
        if search_mode == 1:
            rows = cursor.execute("SELECT * FROM Courses WHERE active=1").fetchall()
    
    if search_mode == 1:
        db_view.search_view(the_label, rows, search_mode=1)
    else:
        db_view.search_view(the_label, rows)
    
    
    
    
    # "(Answering 'N' will resume previous search if 'Search' was initially chosen.\n"
    #                              "Otherwise, you will be Returned to the MAIN MENU.)\n"