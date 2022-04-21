import box
import db_search
import db_insert
import db_view
import db_table

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")
move_on = lambda: input("\n<Press 'Enter' to return to Main Menu>")
db_view_dict = {'1':'people', '2':'Courses', '3':'Cohorts'}

starter = 0
box_line1 = "To De/Reactivate a record:"
box_line2 = "begin with a search"

while True:
    if starter == 0:
        print("\n***** Cohort Database *****\n"
              "---------------------------\n"
            "\n"
            "[1] View A Table\n"
            "[2] Search Records\n"
            "[3] Add a New Record\n"
            "[Q] Quit\n"
            "\n\n"
        )
        box.print_a_box(box_line1, box_line2)
        choice = input("\x1b[6A>>> ")
        starter += 1
    else:
        print("***** Cohort Database *****\n"
              "---------------------------\n"
              "\n"
              "[1] View A Table\n"
              "[2] Search Records\n"
              "[3] Add a New Record\n"
              "[Q] Quit\n"
              "\n\n"
    )
        box.print_a_box(box_line1, box_line2)
        choice = input("\x1b[6A>>> ")
    
    
    choice_list = ['1', '2', '3', 'Q']
    choice = choice.upper()
    
    print()
    
    if choice in choice_list:
        # VIEW DATABASE
        if choice == '1':
            chosen_table = db_table.which_table()
            if chosen_table == 'Menu':
                CLEAR_ALL()
                continue
            else:
                data_view = db_view.database_view(chosen_table)
                if data_view == 'cancelled':
                    CLEAR_ALL()
                    continue
                else:
                    move_on()
                    CLEAR_ALL()
                    continue
        # SEARCH DATABASE
        elif choice == '2':
            result = db_search.database_search(db_table.which_table())
            if result == 'cancelled':
                CLEAR_ALL()
                continue
            else:
                move_on()
                CLEAR_ALL()
                continue
        # ADD RECORDS
        elif choice == '3':
            CLEAR_ALL()
            result = db_insert.database_insert()
            if result == 'cancelled':
                CLEAR_ALL()
                continue
            else:
                move_on()
                CLEAR_ALL()
                continue
        # QUIT PROGRAM
        elif choice == 'Q':
            CLEAR_ALL()
            break
        
        
