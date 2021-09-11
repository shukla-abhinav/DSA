"""
Given an expression, write a program to check whether the parentheses, braces, curly-braces are balanced correctly or not.
()
{()}}[]

Let’s see some examples.

Input: “[{}]([])”

Output: Balanced

Input: “{[}]([])”

Output: Not Balanced

We can use the stack to solve the above problem. Let’s see the steps to solve the problem.

Create a stack to store the characters.
If the length of the expression is odd, then the expression is Not Balanced  [(
Iterate through the given expression.
If the current character is the opening bracket from ( or { or [, then push it to stack.
Else if the current character is a closing bracket ) or } or ], then pop from the stack.
If the popped character is matching with the starting bracket then continue else brackets are not balanced.
After the iteration, if the stack is empty then the equation is Balanced else the equation is Not Balanced.

"""
## stack
class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
        
    def pop(self): 
        return self.elements.pop() 
    
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

def balance_check(expression):
    ## checking the length of the expression
    if len(expression) % 2 != 0:
        ## not balanced if the length is odd
        return False
    
    ## for checking
    opening_brackets = set('([{') 
    pairs = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    ## stack initialization
    stack = Stack()
    
    ## iterating through the given expression
    for bracket in expression:

        ## checking whether the current bracket is opened or not        
        if bracket in opening_brackets:
            ## adding to the stack 
            stack.push(bracket)
        else:
            ## popping out the last bracket from the stack
            popped_bracket = stack.pop()
        
            ## checking whether popped and current bracket pair
            if (popped_bracket, bracket) not in pairs:
                return False
    
    return stack.is_empty()

if __name__ == '__main__':
    if balance_check('[{}]([])'):
        print("Balanced")
    else:
        print("Not Balanced")
    
    if balance_check('{[}]([])'):
        print("Balanced")
    else:
        print("Not Balanced")