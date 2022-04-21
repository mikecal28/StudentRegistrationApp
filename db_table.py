CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")

def which_table():
    CLEAR_ALL()
    table_dict = {'1':'People', '2':'Courses', '3':'Cohorts', '4':'Registrations', '':'Menu'}
    while True:
        the_tables = input("Choose from the following tables:\n"
                            "---------------------------------\n"
                            "[1] People\n"
                            "[2] Courses\n"
                            "[3] Cohorts\n"
                            "[4] Registrations\n"
                            "\n>>> \n"
                            "\n<Press 'Enter' to return to Main Menu>\x1b[2A\x1b[34D"
        )
        if the_tables in table_dict.keys():
            return table_dict.get(the_tables)
        else:
            print("\nInvalid Entry, Please Try Again\n")