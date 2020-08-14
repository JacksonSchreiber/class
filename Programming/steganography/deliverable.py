#!/usr/bin/env python3
import part3
import part4

def sentinel():
    return chr(128)

def encode_pgm(msg,coverfilename,outputfilename):
    '''Encodes a message in a PGM file
    Args:
        msg (str): the message to encode
        coverfilename (str): the name of the PGM file on disk to use as the cover
        outputfilename (str): the name of the new PGM file to write
    Returns:
        None
    '''
    content = part4.read_pgm(coverfilename)
    #encode message
    #use part 3 to do encoding
    part3.steg_encode(msg+chr(128),content[1]) #128 is a non readable ascii char. good stop point
    #write encoded file out using outputfilename
    part4.write_pgm(outputfilename,content)
    #done
    pass

def decode_pgm(filename):
    '''Decodes a message hidden in a PGM file
    Args:
        filename (str): the name of the PGM file that contains a hidden message
    Returns:
        str: the message that was encoded in the PGM file
    '''
    #open filename, read contents
    enc_content = part4.read_pgm(filename)
    #extract LSBs from each pixel
    # use part 3 to decode each char
    return part3.steg_decode(enc_content[1])
    #return the message
    pass

if __name__ == '__main__':
    #encode_pgm("this is A Message", 'plain.pgm', 'encoded.pgm')
    decoded_msg = decode_pgm('encoded.pgm')
    print("This is the decoded message:", decoded_msg)


    pass
