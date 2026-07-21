class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operator = '+'
        n = len(s)
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if operator == '+':
                    stack.append(current_number)
                elif operator == '-':
                    stack.append(-current_number)
                elif operator == '*':
                    stack.append(stack.pop() * current_number)
                elif operator == '/':
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-((-prev) // current_number))
                    else:
                        stack.append(prev // current_number)
                
                operator = char
                current_number = 0
                
        return sum(stack)