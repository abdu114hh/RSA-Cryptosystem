import rsa
import stdio
import sys


# Entry point.
def main():
    # accept n (int) and e (int) as command line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    # find the bit length of n and  set it equal to width
    width = rsa.bitLength(n)
    # read the message to be encrypted from standard input
    message = stdio.readAll()
    # initialize encryption
    encryption = 0

    # iterate over every character in message
    for c in message:
        # turn c into an integer using ord()
        x = ord(str(c))
        # encrypt x
        encryption = rsa.encrypt(x, n, e)
        # write encrypted x in width-long binary
        stdio.write(rsa.dec2bin(encryption, width))

    stdio.writeln()


if __name__ == '__main__':
    main()
