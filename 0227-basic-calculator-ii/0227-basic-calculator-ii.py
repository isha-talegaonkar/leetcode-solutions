# class Solution:
#     def calculate(self, s: str) -> int:
#         if not s:
#             return 0
#         currentNumber = 0
#         operation = '+'
#         length = len(s)
        
#         stack = []
#         for i in range(length):
#             currentChar = s[i]
            
#             if currentChar.isdigit():
#                 currentNumber = currentNumber * 10 + int(currentChar)
            
#             if (not currentChar.isdigit() and not currentChar.isspace()) or i == length - 1:
#                 if operation == '+':
#                     stack.append(currentNumber)
#                 elif operation == '-':
#                     stack.append(-currentNumber)
#                 elif operation == '*':
#                     number = stack.pop()
#                     stack.append(number*currentNumber)
#                 elif operation == '/':
#                     number = stack.pop()
#                     stack.append(number/currentNumber)
            
#             operation = currentChar
#             currentNumber = 0
            
        
#         return sum(stack)
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        current_number = 0
        operation = '+'
        length = len(s)

        for i in range(length):
            current_char = s[i]

            if current_char.isdigit():
                current_number = (current_number * 10) + int(current_char)

            if (not current_char.isdigit() and not current_char.isspace()) or i == length - 1:
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack_top = stack.pop()
                    stack.append(stack_top * current_number)
                elif operation == '/':
                    stack_top = stack.pop()
                    # Use integer division that truncates towards zero
                    stack.append(int(stack_top / current_number))
                
                operation = current_char
                current_number = 0

        return sum(stack)
