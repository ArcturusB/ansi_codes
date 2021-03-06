#!/usr/bin/python
# vim: set fileencoding=utf-8

'''

ansi_codes
==========

Format Python terminal output using ANSI escape codes.


Most of existing escape codes are supported, regardless of their support on
different terminal emulators.

Methods
-------

This package provides two methods:

- `ansi_format(*args, **kwargs)` which returns a string preceded by the
  ANSI-codes implementing the specifications passed as keyword arguments and
  followed by the code to reset the output format,
- `ansi_print(*args, **kwargs)` which calls `ansi_format` and prints its
  result.

Parameters
----------

- `*args`: Passed to Python's `print`.

- `**kwargs`: Instructions for formatting the string, with values in the following table:

| Keyword           | Description                           | Values        |
|-------------------|---------------------------------------|---------------|
| `style`           | Text style and decoration             | **Tuple containing**: `bold`, `faint`, `highlight`, `underline`, `blink_slow`, `blink_rapid`, `negative`, `conceal`, `crossed-out`, `nobold`, `normalcolor`, `noitalic`, `nounderline`, `noblink`, `positive`, `noconceal`, `nocrossed-out`, `framed`, `encircled`, `overlined`, `noframe`, `nooverline` |
| `fg` /  `bg`      | Text (fg) /  background (bg) color    | **Any of:** `black`,`red`,`green`,`yellow`,`blue`,`magenta`,`cyan`,`white`,`default` |
| `fg256` /  `bg256`| 256-color support for text /  bg      | **Integer** in range `0, 256` |
| `special`         | Special formating                     | **Tuple containing:** `all_reset`, `overwrite_line` |


Remaining values are passed to Python’s `print`.


ANSI code correspondance table
------------------------------

| Keyword           | Values                            | ANSI code         |
|-------------------|-----------------------------------|-------------------|
| `style`           | `bold`                            | 1                 |
|                   | `faint`                           | 2                 |
|                   | `highlight`                       | 3                 |
|                   | `underline`                       | 4                 |
|                   | `blink_slow`                      | 5                 |
|                   | `blink_rapid`                     | 6                 |
|                   | `negative`                        | 7                 |
|                   | `conceal`                         | 8                 |
|                   | `crossed-out`                     | 9                 |
|                   | `nobold`                          | 21                |
|                   | `normalcolor`                     | 22                |
|                   | `noitalic`                        | 23                |
|                   | `nounderline`                     | 24                |
|                   | `noblink`                         | 25                |
|                   | `positive`                        | 27                |
|                   | `noconceal`                       | 28                |
|                   | `nocrossed-out`                   | 29                |
|                   | `framed`                          | 51                |
|                   | `encircled`                       | 52                |
|                   | `overlined`                       | 53                |
|                   | `noframe`                         | 54                |
|                   | `nooverline`                      | 55                |
|                   |                                   |                   |
| `fg` /  `bg`      | `black`                           | 30 /  40          |
|                   | `red`                             | 31 /  41          |
|                   | `green`                           | 32 /  42          |
|                   | `yellow`                          | 33 /  43          |
|                   | `blue`                            | 34 /  44          |
|                   | `magenta`                         | 35 /  45          |
|                   | `cyan`                            | 36 /  46          |
|                   | `white`                           | 37 /  47          |
|                   | `default`                         | 39 /  49          |
|                   |                                   |                   |
| `fg256` /  `bg256`| `i` in range `0, 256`             | 38;5;i /  48;5;i  |
|                   |                                   |                   |
| `special`         | `all_reset`                       | 0                 |
|                   | `overwrite_line`                  | F                 |

'''

__author__ = "Gabriel Pelouze"
__copyright__ = "Gabriel Pelouze 2016"
__license__ = "GPL v3"

from .ansi_codes import *
