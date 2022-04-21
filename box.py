def print_a_box(inside_ln1, inside_ln2):
    box_text_ln1 = f'{inside_ln1:^31}'
    box_text_ln2 = f'{inside_ln2:^31}'
    symbols = ['\u250c', '\u2500', '\u2510',
               '\u2502', ' TEXT ', '\u2502',
               '\u2514', '\u2500', '\u2518'
    ]
    
    for i in range(133):
        if i == 0:
            print(symbols[0], end='')
        elif i in range(1, 32):
            print(symbols[1], end='')
        elif i == 32:
            print(symbols[2])
        elif i == 34:
            print(symbols[3], end='')
        elif i == 35:
            print(box_text_ln1, end='')
        elif i == 65:
            print(symbols[3])
        elif i == 66:
            print(symbols[3], end='')
        elif i == 67:
            print(box_text_ln2, end='')
        elif i == 98:
            print(symbols[3])
        elif i == 99:
            print(symbols[6], end='')
        elif i in range(100, 131):
            print(symbols[1], end='')
        elif i == 132:
            print(symbols[8])
            
        
            
            


# "\n\u250c-------------------------------\u2510\n"
#             "\u2502 To Update or Delete a record, \u2502\n"
#             "\u2502     begin with a search       \u2502\n"
#             "\u2514-------------------------------\u2518\x1b[5A\x1b[29D"


# "\n\u250c-------------------------------\u2510\n"
#               "\u2502 To Update or Delete a record, \u2502\n"
#               "\u2502     begin with a search       \u2502\n"
#               "\u2514-------------------------------\u2518\x1b[5A\x1b[29D"