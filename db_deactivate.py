import sqlite3
from datetime import datetime
import time

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")


def deactivate_id(id, table_name):
    connection = sqlite3.connect('my_database.db')

    cursor = connection.cursor()
    
    if table_name == 'People':
        label_for_id = 'person_id'
    elif table_name == 'Courses':
        label_for_id = 'course_id'
    elif table_name == 'Cohorts':
        label_for_id = 'cohort_id'
    elif table_name == 'Student_Cohort_Registrations':
        label_for_id = 'student_id'
    
    possible_responses = ['DELETE', 'NO']
    
    while True:
        to_deactivate = input(f"\nAre you sure you want to deactivate?\n"
                        "Type DELETE to deactivate\n"
                        "Type NO to cancel\n"
                        ">>> "
        )
        
        if to_deactivate in possible_responses:
            break
        else:
            continue
        
    if to_deactivate == 'NO':
        return 'Do Again'
    elif to_deactivate == 'DELETE':
        
        
        sql_update = f"UPDATE {table_name} SET active=? WHERE {label_for_id}=?"
        deactivation_values = ('0', id)
        cursor.execute(sql_update, deactivation_values)
        if table_name == 'Student_Cohort_Registrations':
            check_if_already_inactive = cursor.execute(f"SELECT active FROM Student_Cohort_Registrations WHERE {label_for_id}=?", (id,)).fetchall()
            for i in check_if_already_inactive:
                i = [str(x) for x in i]
                if i[0] == '1':
                    break
                else:
                    CLEAR_ALL()
                    print("\n--Error: Record Already INACTIVE--\n"
                          "Try Again in: 5\n")
                    time.sleep(1)
                    CLEAR_ALL()
                    print("\n--Error: Record Already INACTIVE--\n"
                          "Try Again in: 4\n")
                    time.sleep(1)
                    CLEAR_ALL()
                    print("\n--Error: Record Already INACTIVE--\n"
                          "Try Again in: 3\n")
                    time.sleep(1)
                    CLEAR_ALL()
                    print("\n--Error: Record Already INACTIVE--\n"
                          "Try Again in: 2\n")
                    time.sleep(1)
                    CLEAR_ALL()
                    print("\n--Error: Record Already INACTIVE--\n"
                          "Try Again in: 1\n")
                    time.sleep(1)
                    CLEAR_ALL()
                    return 'Do Again'
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql_update2 = f"UPDATE {table_name} SET drop_date=? WHERE {label_for_id}=?"
            deactivation_values2 = (now, id)
            cursor.execute(sql_update2, deactivation_values2)
        
            
            

    connection.commit()
    print(f"\nSUCCESS:  {label_for_id}: {id} was deactivated in {table_name}!")
    return