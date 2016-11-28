
ansi_codes
==========

Format Python terminal output using ANSI escape codes.


Most of existing escape codes are supported, regardless of their support on
different terminal emulators.

Methods
-------

This package provides two methods:

- `ansi_format(string, **kwargs)` which returns a string preceded by the
  ANSI-codes implementing the specifications passed as keyword arguments and
  followed by the code to reset the output format,
- `ansi_print(string, **kwargs)` which calls `ansi_format` and prints its
  result.

Parameters
----------

- `string`: `string`
    The string to format.

- `**kwargs`:

Instructions for formatting the string, with values in the following table:

+---------------+-----------------------------------+------------+
| Keyword       | Values (tuple of given values)    | Ansi code  |
+---------------+-----------------------------------+------------+
| special       | Tuple containing any of:          |            |
|               | 'all_reset'                       | 0          |
|               | 'overwrite_line'                  | F          |
+---------------+-----------------------------------+------------+
| style         | Tuple containing any of:          |            |
|               | 'bold'                            | 1          |
|               | 'faint'                           | 2          |
|               | 'highlight'                       | 3          |
|               | 'underline'                       | 4          |
|               | 'blink_slow'                      | 5          |
|               | 'blink_rapid'                     | 6          |
|               | 'negative'                        | 7          |
|               | 'conceal'                         | 8          |
|               | 'crossed-out'                     | 9          |
|               | 'nobold'                          | 21         |
|               | 'normalcolor'                     | 22         |
|               | 'noitalic'                        | 23         |
|               | 'nounderline'                     | 24         |
|               | 'noblink'                         | 25         |
|               | 'positive'                        | 27         |
|               | 'noconceal'                       | 28         |
|               | 'nocrossed-out'                   | 29         |
|               | 'framed'                          | 51         |
|               | 'encircled'                       | 52         |
|               | 'overlined'                       | 53         |
|               | 'noframe'                         | 54         |
|               | 'nooverline'                      | 55         |
+---------------+-----------------------------------+------------+
| fg or bg      | Any of the following values:      |            |
|               | 'black'                           | 30 or 40   |
|               | 'red'                             | 31 or 41   |
|               | 'green'                           | 32 or 42   |
|               | 'yellow'                          | 33 or 43   |
|               | 'blue'                            | 34 or 44   |
|               | 'magenta'                         | 35 or 45   |
|               | 'cyan'                            | 36 or 46   |
|               | 'white'                           | 37 or 47   |
|               | 'default'                         | 39 or 49   |
+---------------+-----------------------------------+------------+
| fg256 or      | Any integer (i) in range 0,256.   | 38;5;i or  |
| bg256         |                                   | 48;5;i     |
+---------------+-----------------------------------+------------+
