#!/usr/bin/env python3
#File IO

def read_pgm(filename):
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    '''

    with open(filename) as f:
        full = f.read()
    full = full.split() #list of pgm lines

    return (full[0:4], full[4::]) #Tuple of 2 lists: lines 1-4 and lines 5-eof
    pass

def write_pgm(filename,content):
    '''Writes a PGM file
    Args:
        filename (str): the file name to be used for the written file
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    with open(filename, 'w') as f:
        for i in content:
            for x in i:
                f.write(str(x) + '\n')
        
    pass

def invert(content):
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''

    for i in range(len(content[1])):
        content[1][i] = str(255 - int(content[1][i]))
    
    pass

if __name__ == '__main__':

    filepath = 'plain.pgm'
    pgm = read_pgm(filepath)


    write_pgm('test.pgm', pgm)

    invert(pgm)
    write_pgm('inverted.pgm', pgm)

    pass


