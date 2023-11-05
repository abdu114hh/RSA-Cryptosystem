import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primes_list = _primes(lo, hi)
    # get a random sample from primes_list
    p, q = _sample(primes_list, 2)
    # compute n and m using the given formulas
    n = p*q
    m = (p-1)*(q-1)

    list_primes = _primes(2, m)
    # shuffle list_primes in place
    stdrandom.shuffle(list_primes)
    # initialize e and find its value
    e = 0
    for i in list_primes:
        if m % i != 0:
            e = i
            break

    # initialize d and find its value
    d = 0

    for j in range(1, m+1):
        if (e * j) % m == 1:
            d = j
        # if ed mod m == 1, break
            break

    keygen_tuple = (n, e, d)
    # return the tuple (n, e, d)
    return keygen_tuple


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    encryption = x ** e % n
    return encryption


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    decryption = y ** d % n
    return decryption


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    primesList = []
    for i in range(lo, hi):
        # Set j (potential divisor of i) to 2.

        j = 2
        while j <= i / j:
            # As long as j is less than or equal to i / j...
            if i % j == 0:
                # If j divides i, break (i is not a prime).
                break
            # Increment j by 1.
            j += 1

        # if i is a prime number, add it to primesList
        if i >= 2 and j > i / j:
            primesList += [i]

    return primesList


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # create an empty list
    samples_list = []
    # create a copy of list a
    b = a[:]
    # shuffle b in place
    stdrandom.shuffle(b)
    # pick and return 2 random samples stored in a list from b
    for i in range(k):
        x = b[i]
        samples_list += [x]
    return samples_list


# Returns a random item from the list a.
def _choice(a):
    # shuffle a in place and return a single item
    stdrandom.shuffle(a)
    return a[1]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    stdio.writeln(keygen(25, 100))
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
