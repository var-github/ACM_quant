"""
Let x1 be amount invested in class 1
x2 be amount invested in class 2
x3 be amount invested in class 3
x4 be amount invested in class 4
x5 be amount invested in class 5
x1 + x2 + x3 + x4 + x5 = 75
x1, x2, x3, x4, x5 must all be unique (since they are invested in increments of 1 million)
let us take the case x1 < x2 < x3 < x4 < x5
Here we observe that
x2 = 1 + y2 + x1          since x2 must be atleast 1 million above x1
x3 = 1 + y3 + x2          since x3 must be atleast 1 million above x2
x4 = 1 + y4 + x3          since x4 must be atleast 1 million above x3
x5 = 1 + y5 + x4          since x5 must be atleast 1 million above x4
substituting this in original equation
5x1 + 4y2 + 3y3 + 3y4 + y5 = 65
x1, y2, y3, y4, y5 >= 0

No of solutions to this is given by coefficient of t**65 in the product of 5 geometric progressions
(1+t+t^2+t^3+t^4+....)*(1+t^2+t^4+t^6+....)*(1+t^3+t^6+t^9....)*(1+t^4+t^8+t^16+....)*(1+t^5+t^10+t^15+....)
That is coeff of t**65 in (GP where a = 1, d = t)*(GP where a = 1, d = t^2)*(GP where a = 1, d = t^3)*(GP where a = 1, d = t^4)*(GP where a = 1, d = t^5)
Highest power of t must not exceed 65 in any of the individual GPs - this condition gives the numbers of terms for each GP

By using this method we get the number of ways to spend 75 million in 5 classes where x1 < x2 < x3 < x4 < x5
To get all possible ways we have to multiply this by 5!
"""
from sympy import *
# declaring t as a variable
t = symbols('t')
total = int(input("Enter total amount to invest: "))
classes = int(input("Enter amount of classes to invest in: "))
"""
In the explanation above, when we substituted the conditions in the original eqn we got 5x1 + 4y2 + 3y3 + 3y4 + y5 = 65
from 75 we subtracted 10 on the RHS
this 10 = (no of classes - 1)*(no of classes)/2
NEW RHS = OLD RHS - (no of classes - 1)*(no of classes)/2
"""
n = int(total - (classes - 1)*classes/2)


# Returns factorial of a number
def fact(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


# Return a geometric progression where t is the variable, n = maximum power of t allowed in the GP, t**x is the common difference
def get_gp(t, n, x):
    a = "0"
    for i in range(0, n+1, x):
        a += f" + {t}**{i}"
    return a


eqn = 1
# Runs for each variable in the new equation (x1, y2, y3, y4, y5)
for i in range(1, classes + 1):
    # Getting geometric progression where t is the variable, a = 1, common difference is t**i, n = maximum power of t allowed in the GP
    a = get_gp(t, n, i)
    eqn = eqn*simplify(a)
# Now eqn has GP(t)*GP(t**2)*GP(t**3)*GP(t**4)*GP(t**5)

# Coeff of t**65 is the answer to number of ways of solving 5x1 + 4y2 + 3y3 + 3y4 + y5 = 65
# Total no of ways = (number of ways of solving 5x1 + 4y2 + 3y3 + 3y4 + y5 = 65)*5!
print("Number of ways to do that is: ", expand(eqn).coeff(t**n)*fact(classes))
