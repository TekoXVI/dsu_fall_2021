from graphics import *

def PrintDirections():
    print("This program displays a graph of the function provided by the user. Input is limited to numbers 0-9, one variable x, parentheses, and operations +, -, *, / with no spaces.")
        
def InfixToPostfix(infix):
    s = Stack().get_stack()
    
    postfix = ""
    for c in infix:
        if c in "0123456789x":
            postfix += c
        elif c in "+-":
            # all operators on the stack must come off
            while s != [] and s[-1] in "+-*/":
                postfix += s.pop()
            # operator c goes on stack
            s.append(c)
        elif c in "*/":
            # only */ need to come off
            while s != [] and s[-1] in "*/":
                postfix += s.pop()
            s.append(c)
        elif c == "(":
            s.append(c)
        elif c == ")":
            # while stack top is not "(", pop and move to postfix
            while s != [] and s[-1] != "(":
                postfix += s.pop()
            # then pop the "(" and discard
            s.pop()
    
    # anything left on the stack, pop and move to postfix
    while s != []:
        postfix += s.pop()
    
    return postfix
            
def EvaluatePostfix(postfix, x):
    s = Stack().get_stack()
    for c in postfix:
        if c in "0123456789":
            s.append(float(c))
        elif c == "x":
            s.append(x)
        elif c == "+":
            first = float(s[-2])
            second = float(s[-1])
            s.pop()
            s.pop()
            s.append(first + second)
        elif c == "-":
            first = float(s[-2])
            second = float(s[-1])
            s.pop()
            s.pop()
            s.append(first - second)
        elif c == "*":
            first = float(s[-2])
            second = float(s[-1])
            s.pop()
            s.pop()
            s.append(first * second)
        elif c == "/":
            first = float(s[-2])
            second = float(s[-1])
            s.pop()
            s.pop()
            s.append(first / second)
        
        
    
    answer = s.pop()
    
    return answer

def main():
    PrintDirections()
    infix = input("Enter your expression: ")
    postfix = InfixToPostfix(infix)
    # Collect point data
    points = []
    XLOW = -10
    XHIGH = 10
    YLOW = -10
    YHIGH = 10
    INC = .1
    x = XLOW
    while x < XHIGH:
        #y = x * x # Let the user input their own function.
        y = EvaluatePostfix(postfix, x)
        points.append( Point(x,y) )
        x += INC
    #print(points)
    
    # Draw the data
    win = GraphWin(infix, 500, 500)
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)
    for i in range(len(points)-1):
        l = Line(points[i], points[i+1])
        l.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


class Stack():
    
    def __init__(self):
        self.stack = []
        
    def pop(self):
        last = self.stack[-1]
        self.stack.remove(last)
        return last
        
    def get_stack(self):
        return self.stack


main()


'''
InfixToPostfix("1-(2+3/4*5)*(6-7+8)/9")
print("1234/5*+67-8+*9/-")

EvaluatePostfix("12+", 0)
EvaluatePostfix("9123*+4-6*-", 0)

EvaluatePostfix(InfixToPostfix("(3+4)*5/(x-6)"), 2)
'''