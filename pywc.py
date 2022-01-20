#!/usr/bin/env python3
# -*- coding: 'utf8' -*-

"""
description: implement wc in python
"""
__author__ =  'Andreas Juretzka'
__contact__ = 'a.juretzka@heinlein-support.de'
__version__ = '1.0.1'


import os
import argparse

# get arguments
def getopts():
    parser = argparse.ArgumentParser(
        description=(
            "Rebuilding wc in Python to count lines, "
            "words, bytes etc. in file"
        )
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s  {__version__} author: {__author__}'
    )

    parser.add_argument(
        "input_files", 
        help="files to process or stdin",
        nargs='*',
    )

    parser.add_argument(
        "-l", 
        help="count lines",
        action="store_true",
    )

    parser.add_argument(
        "-c",
        help="count chars",
        action="store_true",
    )

    parser.add_argument(
        "-w", 
        help="count words",
        action="store_true",
    )

    parser.add_argument(
        "-b", 
        help="count bytes",
        action="store_true",
    )

    
    args = parser.parse_args()

    if not (args.l or args.c or args.w or args.b):
        parser.error(
            "please choose at least one action see --help for further details"
        )

    if not args.input_files:
        args.input_files = [0]

    return args

#count file
def counting(args):
    for files in args.input_files:
        with open(files, 'r', encoding = 'utf8', errors='ignore') as infile:
            lines = 0
            lines_empty = 0
            words = 0
            chars = 0
            bytes_c = 0

            for line in infile:
                if len(line.strip()) == 0:
                    lines_empty += 1
                if args.l:
                    lines += 1
                if args.w:
                    words += len(line.split())
                if args.c:
                    chars += len(line)
                if args.b:
                    bytes_c = os.path.getsize(files)

            print(f'file:  {files}')
            print(f'lines: {lines} with {lines_empty} empty lines')
            print(f'words: {words}')
            print(f'chars: {chars}')
            print(f'bytes: {bytes_c}')


def main():
    args = getopts()
    counting(args)

if __name__ == '__main__':
    main()
