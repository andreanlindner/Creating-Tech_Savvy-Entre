import math

def quadratic(a,b,c):
    """
    takes in a, b, and c to solve for x using the quadratic function (ax^2 + bx + c = 0)

    a = an int
    b = an int
    c = an int
    """

    part1= int((-b)/(2*a))
    sqroot = int((b**2) - (4*a*c))
    part2 = math.sqrt(sqroot)/(2*a)
    return "The values of x are "+ (part1-part2) + " and "+ (part1+part2)+ "."

def main():
    return quadratic(2,4,5)

if __name__ == '__main__':    
    main()