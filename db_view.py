import sqlite3
import quick_search

from db_view_active import view_active

def database_view(selection):
    string1 = ''
    string2 = ''
    string3 = ''
    string4 = ''
    people_table = ''
    courses_table = ''
    cohorts_table = ''
    registrations_table = ''

    connection = sqlite3.connect('my_database.db')

    cursor = connection.cursor()

    
    if selection == 'Menu':
        return 'Menu'
    elif selection == 'People':
        rows = cursor.execute("SELECT * FROM People").fetchall()
        header1 = f'{"ID":3}{"FIRST NAME":12}{"LAST NAME":12}{"EMAIL":30}{"PHONE":12}{"PASSWORD":15}{"ADDRESS":20}{"CITY":15}{"STATE":7}{"ZIPCODE":8}{"ACTIVE":8}'
        people_table = "TABLE: People"
        people_table = people_table.center(len(header1))
        print(f'\n{people_table}')
        print(f'\n{header1}')
        dashes_string1 = string1.ljust(len(header1), '-')
        print(dashes_string1)

        for person in rows:
            person = [str(x) for x in person]
            print(f'{person[0]:3}{person[1]:12}{person[2]:12}{person[3]:30}{person[4]:12}{person[5]:15}{person[6]:20}{person[7]:15}{person[8]:7}{person[9]:8}{person[10]:8}')
        
        active_records = view_active(1, "Courses", rows, 1)
        if active_records == 'cancelled':
            quick_search.do_quick_search(selection)
            return 'cancelled'
        
        return
    
    elif selection == 'Courses':
        rows = cursor.execute("SELECT * FROM Courses").fetchall()
        header2 = f'{"ID":3}{"NAME":15}{"DESCRIPTION":40}{"ACTIVE":8}'
        courses_table = "TABLE: Courses"
        courses_table = courses_table.center(len(header2))
        print(f'\n{courses_table}')
        print(f'\n{header2}')
        dashes_string2 = string2.ljust(len(header2), '-')
        print(dashes_string2)

        for course in rows:
            course = [str(x) for x in course]
            print(f'{course[0]:3}{course[1]:15}{course[2]:40}{course[3]:8}')
        
        active_records = view_active(4, "Courses", rows, 1)
        if active_records == 'cancelled':
            quick_search.do_quick_search(selection)
            return 'cancelled'
        
        return
    
    elif selection == 'Cohorts':
        rows = cursor.execute("SELECT * FROM Cohorts").fetchall()
        header3 = f'{"COHORT-ID":10}{"INSTRUCTOR-ID":15}{"COURSE-ID":10}{"START":21}{"END":21}{"ACTIVE":8}'
        cohorts_table = "TABLE: Cohorts"
        cohorts_table = cohorts_table.center(len(header3))
        print(f'\n{cohorts_table}')
        print(f'\n{header3}')
        dashes_string3 = string3.ljust(len(header3), '-')
        print(dashes_string3)

        for cohort in rows:
            cohort = [str(x) for x in cohort]
            print(f'{cohort[0]:10}{cohort[1]:15}{cohort[2]:10}{cohort[3]:21}{cohort[4]:21}{cohort[5]:8}')
        
        active_records = view_active(2, "Cohorts", rows, 1)
        if active_records == 'cancelled':
            quick_search.do_quick_search(selection)
            return 'cancelled'
        
        return

    elif selection == 'Registrations':
        # rows = cursor.execute("SELECT * FROM Student_Cohort_Registrations").fetchall()
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
        # header4 = f'{"STU-ID":8}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
        header4 = f'{"STU-ID":8}{"STU-1ST NAME":15}{"STU-LAST NAME":15}{"INSTR-ID":10}{"INSTR-1ST NAME":17}{"INSTR-LAST NAME":17}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
        registrations_table = "TABLE: Student Cohort Registrations (REG-ID = STU-ID)"
        registrations_table = registrations_table.center(len(header4))
        print(f'\n{registrations_table}')
        print(f'\n{header4}')
        dashes_string4 = string4.ljust(len(header4), '-')
        print(dashes_string4)

        for registration in rows:
            registration = [str(x) for x in registration]
            print(f'{registration[0]:8}{registration[6]:15}{registration[7]:15}{registration[8]:10}{registration[9]:17}{registration[10]:17}{registration[1]:11}{registration[2]:21}{registration[3]:21}{registration[4]:21}{registration[5]:8}')
        
        active_records = view_active(3, "Registrations", rows, 1)
        if active_records == 'cancelled':
            quick_search.do_quick_search(selection)
            return 'cancelled'
        
        return







def search_view(selection, row_code, search_mode=0):
    string1 = ''
    string2 = ''
    string3 = ''
    string4 = ''

    connection = sqlite3.connect('my_database.db')

    cursor = connection.cursor()

    
    if selection == 'Menu':
        return 'Menu'
    elif selection == 'People':
        
        rows = row_code
        header1 = f'{"ID":3}{"FIRST NAME":12}{"LAST NAME":12}{"EMAIL":30}{"PHONE":12}{"PASSWORD":15}{"ADDRESS":20}{"CITY":15}{"STATE":7}{"ZIPCODE":8}{"ACTIVE":8}'
        people_table = "TABLE: People"
        people_table = people_table.center(len(header1))
        print(f'\n{people_table}')
        print(f'\n{header1}')
        dashes_string1 = string1.ljust(len(header1), '-')
        print(dashes_string1)

        for person in rows:
            person = [str(x) for x in person]
            print(f'{person[0]:3}{person[1]:12}{person[2]:12}{person[3]:30}{person[4]:12}{person[5]:15}{person[6]:20}{person[7]:15}{person[8]:7}{person[9]:8}{person[10]:8}')
        
        
        
        return
    
    elif selection == 'Courses':
        
        rows = row_code
        header2 = f'{"ID":3}{"NAME":15}{"DESCRIPTION":40}{"ACTIVE":8}'
        courses_table = "TABLE: Courses"
        courses_table = courses_table.center(len(header2))
        print(f'\n{courses_table}')
        print(f'\n{header2}')
        dashes_string2 = string2.ljust(len(header2), '-')
        print(dashes_string2)

        for course in rows:
            course = [str(x) for x in course]
            print(f'{course[0]:3}{course[1]:15}{course[2]:40}{course[3]:8}')
            
        
        
        return
    
    elif selection == 'Cohorts':
        
        rows = row_code
        if search_mode == 1:
            header3 = f'{"COHORT-ID":11}{"INSTR-ID":10}{"COURSE-ID":11}{"START":21}{"END":21}{"ACTIVE":8}'
            cohorts_table = "TABLE: Cohorts"
            cohorts_table = cohorts_table.center(len(header3))
            print(f'\n{cohorts_table}')
            print(f'\n{header3}')
            dashes_string3 = string3.ljust(len(header3), '-')
            print(dashes_string3)

            for cohort in rows:
                cohort = [str(x) for x in cohort]
                print(f'{cohort[0]:11}{cohort[1]:10}{cohort[2]:11}{cohort[3]:21}{cohort[4]:21}{cohort[5]:8}')
        else:
            header3 = f'{"COHORT-ID":11}{"INSTR-ID":10}{"INSTR-FIRST NAME":18}{"INSTR-LAST NAME":18}{"COURSE-ID":11}{"COURSE NAME":15}{"START":21}{"END":21}{"ACTIVE":8}'
            cohorts_table = "TABLE: Cohorts"
            cohorts_table = cohorts_table.center(len(header3))
            print(f'\n{cohorts_table}')
            print(f'\n{header3}')
            dashes_string3 = string3.ljust(len(header3), '-')
            print(dashes_string3)

            for cohort in rows:
                cohort = [str(x) for x in cohort]
                print(f'{cohort[0]:11}{cohort[1]:10}{cohort[6]:18}{cohort[7]:18}{cohort[2]:11}{cohort[8]:15}{cohort[3]:21}{cohort[4]:21}{cohort[5]:8}')
            
            
            
        return
    
    elif selection == 'Registrations':
        
        rows = row_code
        if search_mode == 1:
            # header4 = f'{"STU-ID":8}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
            header4 = f'{"STU-ID":8}{"STU-1ST NAME":15}{"STU-LAST NAME":15}{"INSTR-ID":10}{"INSTR-1ST NAME":17}{"INSTR-LAST NAME":17}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
            registrations_table = "TABLE: Student Cohort Registrations (REG-ID = STU-ID)"
            registrations_table = registrations_table.center(len(header4))
            print(f'\n{registrations_table}')
            print(f'\n{header4}')
            dashes_string4 = string4.ljust(len(header4), '-')
            print(dashes_string4)

            for registration in rows:
                registration = [str(x) for x in registration]
                # print(f'{registration[0]:8}{registration[1]:11}{registration[2]:21}{registration[3]:21}{registration[4]:21}{registration[5]:8}')
                if registration[5] == '1':
                    print(f'{registration[0]:8}{registration[6]:15}{registration[7]:15}{registration[8]:10}{registration[9]:17}{registration[10]:17}{registration[1]:11}{registration[2]:21}{registration[3]:21}{registration[4]:21}{registration[5]:8}')
        else:
            # header4 = f'{"STU-ID":8}{"STU-FIRST NAME":16}{"STU-LAST NAME":16}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
            header4 = f'{"STU-ID":8}{"STU-1ST NAME":15}{"STU-LAST NAME":15}{"INSTR-ID":10}{"INSTR-1ST NAME":17}{"INSTR-LAST NAME":17}{"COHORT-ID":11}{"REGIST. DATE":21}{"COMPL. DATE":21}{"DROP DATE":21}{"ACTIVE":8}'
            registrations_table = "TABLE: Student Cohort Registrations (REG-ID = STU-ID)"
            registrations_table = registrations_table.center(len(header4))
            print(f'\n{registrations_table}')
            print(f'\n{header4}')
            dashes_string4 = string4.ljust(len(header4), '-')
            print(dashes_string4)

            for registration in rows:
                registration = [str(x) for x in registration]
                # print(f'{registration[0]:8}{registration[6]:16}{registration[7]:16}{registration[1]:11}{registration[2]:21}{registration[3]:21}{registration[4]:21}{registration[5]:8}')
                print(f'{registration[0]:8}{registration[6]:15}{registration[7]:15}{registration[8]:10}{registration[9]:17}{registration[10]:17}{registration[1]:11}{registration[2]:21}{registration[3]:21}{registration[4]:21}{registration[5]:8}')
        
        
        
        return
