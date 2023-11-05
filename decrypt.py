import rsa
import stdio
import sys


# Entry point.
def main():
    # accept n(int) and d(int) as command line arguments
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    # find the bit length of n and set it equal to width
    width = rsa.bitLength(n)
    # read the message to be decrypted from standard input
    message = stdio.readAll()
    # iterate from 0 to len(message)-1, with increments of width
    for i in range(0, len(message)-1, width):
        # set s to substring of message from i to i + width
        s = message[i:i+width]
        # convert s into decimal and set it equal to y
        y = rsa.bin2dec(s)
        # decrypt y
        decryption = rsa.decrypt(y, n, d)
        # find the character corresponding to the decrypted value
        chraracter = chr(decryption)
        stdio.write(chraracter)


if __name__ == '__main__':
    main()
