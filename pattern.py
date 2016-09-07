"""
Usage:
    pattern.py (--create=<arg> | --indexof=<arg> --file=<arg>) [--outfile=<arg>]
    pattern.py --help
    pattern.py --version

Options:
    -h --help                                       open help menu
    -v --version                                    show version

Required options:
    --create='size'                                 create pattern with specific size
    --indexof='string' --file='file with pattern'   get index of string from pattern inside file

Optional options:
    --outfile='file'                                output pattern to file (useful to locate index when needed)

"""
import os
import sys
from docopt import docopt, DocoptExit

class MyPatternCreator():
    
    def generate_pattern(self, size, charsets=None):
        """Method that generate pattern."""
        
        lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
        upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numeric = '0123456789'

        if charsets is None:
            charsets = (upper_alpha, lower_alpha, numeric)
        if size <= 0:
            return ''

        state = [0, 0, 0]
        output = []
        count = (size + 2) // 3

        while count > 0:
            output.append(charsets[0][state[0]] +
                          charsets[1][state[1]] +
                          charsets[2][state[2]])
            state[2] += 1
            if state[2] >= len(charsets[2]):
                state[2] = 0
                state[1] += 1
                if state[1] >= len(charsets[1]):
                    state[1] = 0
                    state[0] += 1
                    if state[0] >= len(charsets[0]):
                        state[0] = 0
            count -= 1
        return ''.join(output)[:size]

    def get_index_of(self, string, file):
        with open(file, 'r') as f:
            pattern = f.readline()
            try:
                print(pattern.index(string))
            except:
                print('[-] String: '+string+' not found!!')

def main():
    try:
        arguments = docopt(__doc__, version="Pattern creator 2016 - anarc0der")
        create = arguments['--create']
        indexof = arguments['--indexof']
        file = arguments['--file']
        outfile = arguments['--outfile']

    except DocoptExit as e:
        print("[-] You need to choose the right options..\n")
        os.system('python3 pattern.py --help')
        sys.exit(1)

    x = MyPatternCreator()
    if create:
        pattern = x.generate_pattern(int(create))
        if outfile:
            with open (outfile, 'w') as f: f.write (pattern+'\n')
    
    if indexof:
        x.get_index_of(indexof, file)

if __name__ == '__main__':
    main()
