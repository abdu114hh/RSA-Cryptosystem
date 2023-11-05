import rsa
import stdio
import sys


# Entry point.
def main():
    # accept lo(int) and hi(int) as command line arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    # get the keys using the rsa library

    keys = rsa.keygen(lo, hi)
    # write the elements of the tuple keys to standard output
    for i in keys:
        stdio. write(str(i) + " ")
    stdio.writeln()


if __name__ == '__main__':
    main()
