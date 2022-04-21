import db_search
import time

def do_quick_search(viewed_table):

    quick_input = input("\nWould you like to do a quick search? (Y/N)\n"
                        "\n>>> ")
    print()
    
    if quick_input.upper() == 'Y':
        db_search.database_search(viewed_table)
    elif quick_input.upper() == 'N':
        return
    else:
        print("\nWrong input received. Moving on...\n")
        time.sleep(3)
        return