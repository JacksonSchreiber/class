#!/usr/bin/env python3

def steg_encode(msg, cover):
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    msglist = list(msg)
    msgbin = []
    for i in range(len(msg)): #convert msg to ascii binary
        msgbin += list(format(ord(msg[i]), '0>8b'))

    for i in range(len(msgbin)): #replace last bit with msg
        cover[i] = list(format(int(cover[i]), '0>8b'))
        cover[i][-1] = msgbin[i]
        cover[i] = str(int(''.join(cover[i]), 2))


    pass

def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    stegocp = stego[:] #copy
    msg = ''
    for i in range(len(stegocp)):
        stegocp[i] = list(format(int(stegocp[i]), '0>8b')) #convert to binary
        stegocp[i] = stegocp[i][-1] #only save last bit (Least Signficant Bit)

    for i in range(0, len(stegocp), 8):
        if int(''.join(stegocp[i:i+8]), 2) == 128: #check if char's ascii is 128. this is the stop byte
            print("Stopped decoding on line", i)
            break

        msg += chr(int(''.join(stegocp[i:i+8]), 2)) #convert 8 bits to character
    return msg

if __name__ == '__main__':
    cover = [252, 241, 231, 210, 230, 250, 250, 251, 250, 251, 251, 251, 250, 251, 250, 250]
    msg = 'FU'
    print("Message:      ", msg)

    print("Cover:        ", cover)
    steg_encode(msg, cover)
    print("cover encoded:", cover)

    decode = steg_decode(cover)
    print("Cover Decoded:", decode)
