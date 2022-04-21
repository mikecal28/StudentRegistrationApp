import sqlite3
import db_deactivate
import db_reactivate
import db_view
import db_view_active
import time
CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")
result = ''
verification_list = []

def database_search(table_choice):
    possible_responses = ['N', 'I']
    r_or_d = ''
    activation_choice = ''
    switch = 0
    type_switch = 0

    connection = sqlite3.connect('my_database.db')

    cursor = connection.cursor()
    
    if table_choice == 'Menu':
        return 'cancelled'
    
    while True:
        if table_choice == 'Cohorts':
            search_type = input("\nSearch by (N)ame of Student in Cohort, or by the Cohort (I)D?\n"
                            "\n>>> "
            )
        else:
            search_type = input("\nSearch by (N)ame or (I)D?                \n"
                            "\n>>> "
            )
        if search_type.upper() in possible_responses:
            if search_type.upper() == 'N' and table_choice != 'Registrations':
                type_switch = 1
            elif search_type.upper() == 'I' and table_choice != 'Registrations':
                type_switch = 2
            elif search_type.upper() == 'N':
                type_switch = 3
            else:
                type_switch = 2
            break
        else:
            print("\nInvalid Response, Please Try Again\n")
    
    if type_switch == 1 or type_switch == 0:  
        search = input("\nPlease enter a query (Partial terms are permitted).\n"
                    "To return to the main menu, press 'Enter'.\n"
                    "\n>>> "
    )
        if search == '':
            return 'cancelled'
    
    elif type_switch == 2:
        search = input("\nPlease enter an exact ID, or\n"
                    "to return to the main menu, press 'Enter'.\n"
                    "\n>>> "
    )
        if search == '':
            return 'cancelled'
    
    
    
    
    if table_choice == 'People':
        if type_switch == 1:
            rows = cursor.execute("SELECT * FROM People WHERE first_name LIKE ? OR last_name LIKE ?", ['%'+search+'%','%'+search+'%']).fetchall()
        elif type_switch == 2:
            try:
                search = int(search)
                rows = cursor.execute("SELECT * FROM People WHERE person_id=?", (search,)).fetchall()
            except:
                print("\nInvalid Entry: Non-Numeric Characters Entered. Returning to Main Menu")
                time.sleep(4)
                return 'cancelled'
        db_view.search_view('People', rows)
        switch = 1
        id_label = 'People'
        active_records = db_view_active.view_active(switch, id_label, rows)
        while True:
            if active_records == 'cancelled':
                break
            else:
                activation_choice = 'D'
                break
        id_choice = 'ID'
    elif table_choice == 'Courses':
        if type_switch == 1:
            rows = cursor.execute("SELECT * FROM Courses WHERE name LIKE ?", ('%'+search+'%',)).fetchall()
        elif type_switch == 2:
            try:
                search = int(search)
                rows = cursor.execute("SELECT * FROM Courses WHERE course_id=?", (search,)).fetchall()
            except:
                print("\nInvalid Entry: Non-Numeric Characters Entered. Returning to Main Menu")
                time.sleep(4)
                return 'cancelled'
        db_view.search_view('Courses', rows)
        switch = 2
        id_label = 'Courses'
        db_view_active.view_active(switch, 'Cohorts', rows)
        id_choice = 'Course ID'
    elif table_choice == 'Cohorts':
        if type_switch == 1:
            rows = cursor.execute("SELECT coh.*, p.first_name, p.last_name, c.name FROM People p JOIN Cohorts coh ON p.person_id = coh.instructor_id JOIN Courses c ON c.course_id = coh.course_id WHERE p.first_name LIKE ? OR p.last_name LIKE ?", ['%'+search+'%','%'+search+'%']).fetchall()
        elif type_switch == 2:
            try:
                search = int(search)
                rows = cursor.execute("SELECT coh.*, p.first_name, p.last_name, c.name FROM People p JOIN Cohorts coh ON p.person_id = coh.instructor_id JOIN Courses c ON c.course_id = coh.course_id WHERE cohort_id=?", (search,)).fetchall()
            except:
                print("\nInvalid Entry: Non-Numeric Characters Entered. Returning to Main Menu")
                time.sleep(4)
                return 'cancelled'
        db_view.search_view('Cohorts', rows)
        switch = 3
        id_label = 'Cohorts'
        db_view_active.view_active(switch, 'Registrations', rows)
        id_choice = 'Cohort ID'
    elif table_choice == 'Registrations':
        if type_switch == 3:
            # rows = cursor.execute("SELECT scr.*, p.first_name, p.last_name FROM Student_Cohort_Registrations scr JOIN People p ON p.person_id = scr.student_id WHERE p.first_name LIKE ? OR p.last_name LIKE ?", ['%'+search+'%','%'+search+'%']).fetchall()
            while True:
                search_kind = input("\nSearch by (I)nstructor or (S)tudent?\n"
                                    "\n>>> "
                )
                search = input("\nPlease enter a query (Partial terms are permitted).\n"
                    "To return to the main menu, press 'Enter'.\n"
                    "\n>>> "
                )
                if search == '':
                    return 'cancelled'
                if search_kind.upper() == 'I':
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
                        ON scr.cohort_id = i.cohort_id
                        WHERE i.instructor_fn LIKE ?
                        OR i.instructor_ln LIKE ?;
                    ''', ['%'+search+'%','%'+search+'%']).fetchall()
                    break
                elif search_kind.upper() == 'S':
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
                        ON scr.cohort_id = i.cohort_id
                        WHERE p.first_name LIKE ?
                        OR p.last_name LIKE ?;
                    ''', ['%'+search+'%','%'+search+'%']).fetchall()
                    break
                else:
                    print("\nInvalid Entry: Please Try Again\n")
        elif type_switch == 2:
            try:
                search = int(search)
                rows = cursor.execute("SELECT scr.*, p.first_name, p.last_name FROM Student_Cohort_Registrations scr JOIN People p ON p.person_id = scr.student_id WHERE student_id=?", (search,)).fetchall()
            except:
                print("\nInvalid Entry: Non-Numeric Characters Entered. Returning to Main Menu")
                time.sleep(4)
                return 'cancelled'
        db_view.search_view('Registrations', rows)
        switch = 4
        id_label = 'Student_Cohort_Registrations'
        id_choice = 'Student ID'
        
    
    while True:
        if switch == 4:
            break
        move_forward = input(f"\n<Press ENTER to close current Table\nand continue to De/Reactivation for TABLE: {id_label}>")
        if move_forward == '':
            CLEAR_ALL()
            db_view.search_view(id_label, rows)
            break
    
    
    # Begins De/Reactivation logic:
    go_back = 0
    inner_loop_breaker = 0
    while True:
        if go_back == 1:
            CLEAR_ALL()
            db_view.search_view(table_choice, rows)
            go_back = 0
        if inner_loop_breaker == 1:
            break
        while True:
            if activation_choice == 'D':
                r_or_d = 'D'
                break
            possible_in_reactivate_or_deactivate = ['R', 'D', '']
            reactivate_or_deactivate = input("\nID: (R)eactivate or (D)eactivate?\n"
                                            "<Hit ENTER to return to MAIN MENU>\n"
                                        "\n>>> "
            )
            print()
            if reactivate_or_deactivate.upper() in possible_in_reactivate_or_deactivate:
                if reactivate_or_deactivate.upper() == 'R':
                    r_or_d = 'R'
                    break
                elif reactivate_or_deactivate.upper() == 'D':
                    r_or_d = 'D'
                    break
                elif reactivate_or_deactivate == '':
                    return 'cancelled'
        
        
        # To DEactivate an ID:
        inner_loop_breaker = 0 
        while True:
            if go_back == 1:
                break
            if inner_loop_breaker == 1:
                break
            if r_or_d == 'R':
                break
            while True:
            
                choose_deactivate_id = input(f"\nType the {id_choice} you would like to deactivate,\n"
                                            "or hit ENTER to go BACK\n"
                                            "\n>>> "
                )
                
                if choose_deactivate_id == '':
                    go_back = 1
                    break
                
                
                for i in rows:
                    i = [str(x) for x in i]
                    verification_list.append(i[0])
                
                if choose_deactivate_id in verification_list:
                    break
                    
            if go_back == 1:
                break
            if r_or_d == 'D':
                deactivation_station = db_deactivate.deactivate_id(choose_deactivate_id, id_label)
            
                if deactivation_station == 'cancelled':
                    return 'cancelled'
                elif deactivation_station != 'Do Again':
                    inner_loop_breaker = 1
                if deactivation_station == 'Do Again':
                    go_back = 0
                    db_view.search_view(table_choice, rows)

            
            
        
        
        # To REactivate an ID:
        while True:
            if go_back == 1:
                break
            if inner_loop_breaker == 1:
                break
            if r_or_d == 'D':
                break
            while True:
                
                choose_reactivate_id = input(f"\nType the {id_choice} you would like to reactivate,\n"
                                            "or hit ENTER to go BACK\n"
                                            "\n>>> "
                )
                
                if choose_reactivate_id == '':
                    go_back = 1
                    break
                
                
                for i in rows:
                    i = [str(x) for x in i]
                    verification_list.append(i[0])
                
                if choose_reactivate_id in verification_list:
                    break
            
            if go_back == 1:
                break       
            if r_or_d == 'R':
                reactivation_station = db_reactivate.reactivate_id(choose_reactivate_id, id_label)
            
                if reactivation_station == 'cancelled':
                    return 'cancelled'
                elif reactivation_station != 'Do Again':
                    inner_loop_breaker = 1
                if reactivation_station == 'Do Again':
                    go_back = 0
                    db_view.search_view(table_choice, rows)
                    
            
            
