#!/usr/bin/env python

# Not working yet!


_ESCAPE = '\033[{}m'

_CODES = {
    'tuple': {
        'special': {
            'all_reset': '0',
            'overwrite_line': 'F',
            },
        'style': {
            'bold': '1',
            'faint': '2',
            'highlight': '3',
            'underline': '4',
            'blink_slow': '5',
            'blink_rapid': '6',
            'negative': '7',
            'conceal': '8',
            'crossed-out': '9',
            # fonts not implemented (10--20)
            'nobold': '21',
            'normalcolor': '22',
            'noitalic': '23',
            'nounderline': '24',
            'noblink': '25',
            'positive': '27',
            'noconceal': '28',
            'nocrossed-out': '29',
            'framed': '51',
            'encircled': '52',
            'overlined': '53',
            'noframe': '54',
            'nooverline': '55',
            },
        },
    'string': {
        'fg': {
            'black': '30',
            'red': '31',
            'green': '32',
            'yellow': '33',
            'blue': '34',
            'magenta': '35',
            'cyan': '36',
            'white': '37',
            'default': '39',
            },
        'bg': {
            'black': '40',
            'red': '41',
            'green': '42',
            'yellow': '43',
            'blue': '44',
            'magenta': '45',
            'cyan': '46',
            'white': '47',
            'default': '49',
            },
        },
    'int': {
        'bg256': '48;5',
        'fg256': '38;5',
        }
    }

# rename default Python `print` to `_print`
_print = print

def format(string, **kwargs):
    ''' Return a string wrapped between the ANSI codes implementing the format
    passed as arguments. '''
    codes = []
    for kwd,val in kwargs.items():
        if kwd in _CODES['tuple'].keys():
            if isinstance(val, str):
                codes.append(_CODES['tuple'][kwd][val])
            else:
                for v in val:
                    codes.append(_CODES['tuple'][kwd][v])
        elif kwd in _CODES['string'].keys():
            codes.append(_CODES['string'][kwd][val])
        elif kwd in _CODES['int'].keys():
            codes.append('{};{}'.format(_CODES['int'][kwd], val))
        else:
            raise ValueError('Bad option')
    return '{}{}{}'.format(
        _ESCAPE.format(';'.join(codes)),
        string,
        _ESCAPE.format(_CODES['tuple']['special']['all_reset']),
        )

def print(*args, **kwargs):
    ''' Call ansi_format and print its output. '''
    ansi_kwargs = {}
    print_kwargs = {}
    for k,v in kwargs.items():
        if k in _CODES['tuple'].keys() \
                or k in _CODES['string'].keys() \
                or k in ['bg256', 'fg256']: # qnd
            ansi_kwargs.update({k:v})
        else:
            print_kwargs.update({k:v})
    print_args = []
    for arg in args:
        print_args.append(format(arg, **ansi_kwargs))
    _print(*print_args, **print_kwargs)
