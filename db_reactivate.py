import sqlite3
import time


def reactivate_id(id, table_name):
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
    
    possible_responses = ['REACTIVATE', 'NO']
    
    while True:
        to_reactivate = input(f"\nAre you sure you want to REactivate?\n"
                        "Type REACTIVATE to reactivate\n"
                        "Type NO to cancel\n"
                        ">>> "
        )
        
        if to_reactivate in possible_responses:
            break
        else:
            continue
        
    if to_reactivate == 'NO':
        return 'Do Again'
    elif to_reactivate == 'REACTIVATE':
        
        
        sql_update = f"UPDATE {table_name} SET active=? WHERE {label_for_id}=?"
        reactivation_values = ('1', id)
        cursor.execute(sql_update, reactivation_values)
        if table_name == 'Student_Cohort_Registrations':
            check_if_already_active = cursor.execute(f"SELECT drop_date FROM Student_Cohort_Registrations WHERE student_id=? AND {label_for_id}=?", reactivation_values).fetchall()
            for i in check_if_already_active:
                i = [str(x) for x in i]
                if i[0] == None:
                    break
                else:
                    print("\n--Error: Record Already ACTIVE--\n")
                    return 'Do Again'
            sql_update2 = f"UPDATE {table_name} SET drop_date=? WHERE {label_for_id}=?"
            reactivation_values2 = (None, id)
            cursor.execute(sql_update2, reactivation_values2)
        
            
            

    connection.commit()
    print(f"\nSUCCESS:  {label_for_id}: {id} was reactivated in {table_name}!")
    return