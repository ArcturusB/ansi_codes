#!/usr/bin/env python

from ansi_codes import print

# none, bold, faint

def print_256_per_col(cols, start, stop):
    col = 0
    for color in range(start, stop):
        if (col+1) % cols == 0:
            end_char = '\n'
        else:
            end_char = ''
        col += 1
        fg_string = '  {:>3} '.format(color)
        bg_string = 7*' '
        print(fg_string, fg256=color, end='')
        print('n', fg256=color, end='')
        print('b', fg256=color, style='bold', end='')
        print('f', fg256=color, style='faint', end=' ')
        print(bg_string, bg256=color, end=end_char)

ansi_colors = {
        0: 'black',
        1: 'red',
        2: 'green',
        3: 'yellow',
        4: 'blue',
        5: 'magenta',
        6: 'cyan',
        7: 'white',
        9: 'default',
        }

fg_string = '    9 '
bg_string = 7*' '
print(fg_string, fg='default', end='')
print('n', fg='default', end='')
print('b', fg='default', style='bold', end='')
print('f', fg='default', style='faint', end=' ')
print(bg_string, bg='default')

for color_code in range(7):
    color = ansi_colors[color_code]
    end_char = ''
    fg_string = '  {:>3} '.format(color_code)
    bg_string = 7*' '
    print(fg_string, fg=color, end='')
    print('n', fg=color, end='')
    print('b', fg=color, style='bold', end='')
    print('f', fg=color, style='faint', end=' ')
    print(bg_string, bg=color, end=end_char)
print('\n')

print_256_per_col(8, 0, 16)
print('')
print_256_per_col(6, 16, 256)
