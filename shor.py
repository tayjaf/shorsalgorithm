#InClass Activity 3

# import mod inverse math in python
import gmpy2

# mod inverse function from gmpy2 library
def mod_inverse(n, m):
    return gmpy2.invert(n, m)

# returns the GCD of two numbers a, b
def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a


# returns the solution of a^b mod N
def soln(a, b, N):
    ans = 1
    while (b > 0):
        if b % 2:
            ans = ans * a % N
        b = b // 2
        a = a * a
        # print("({}, {}, {}".format(a,b,N))
    return ans



# checks if a^b mod N is congruent to 1
def isCongruent(a, b, N):
    if (soln(a, b, N) == 1):
        return True
    else:
        return False


# checks if t is odd or even
def isEven(t):
    if t % 2 == 0:
        return True
    else:
        return False



# returns the period t given g and N
def checkForT(g, N):
    t = 1
    repeats = False
    end = False
    startPoint = soln(g, t, N)
    t += 1
    while end != True:
        if soln(g, t, N) != 1 and soln(g, t, N) != startPoint:
            t += 1
        elif soln(g, t, N) == startPoint:
            repeats = True
            t -= 1
            end = True
        else:
            end = True
    return t



# you just know
def doTheRest(g, N):
    print("g = {}".format(g))
    print("N = {}".format(N))

    print("t = {}".format(checkForT(g, N)))
    t = checkForT(g, N)
    # prints the period t

    if isEven(t) == True:
        print("t is even.")
    else:
        print("t is an odd number.")
        return t

    if isEven(t):
        a = (pow(g, t // 2) - 1) % N
        b = (pow(g, t // 2) + 1) % N
    print("a = {}^{}/2 - 1 mod {} = {}".format(g, t, N, a))
    print("b = {}^{}/2 + 1 mod {} = {}".format(g, t, N, b))
    print("a = {}".format(a))
    print("b = {}".format(b))

    p = gcd(a, N)
    q = gcd(b, N)
    print("GCD(a,N) = GCD({},{}) = {}".format(a, N, p))
    print("GCD(b,N) = GCD({},{}) = {}".format(b, N, q))

    for i in range(1, t + 1):
        r = pow(g, i, N)
        print("g^" + str(i) + " = " + str(r))
        
    return t


# QUESTION 2:
# {N, g, t}
# {1007,529,18}
# Starting values:
N = 1007
g = 529
given_t = checkForT(g, N)

t = doTheRest(g, N)


if isEven(t):
    if given_t == t:
        print("Therefore: <{},{},{}> is part of the ORDER and t = {} is the smallest value.\n\n".format(N, g, given_t, t))
    else:
        print(
            "Therefore: <{},{},{}> is not part of the ORDER and t = {} is the smallest value.\n\n".format(N, g, given_t, t))
