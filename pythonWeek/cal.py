while 1:
number1 = float (input('Please enter first number:'))
number2 = float (input('Please enter second number:'))
operator = char (input('Please enter your operator: +, -, *, /, or %')) 

if operator == '+':
   number3 = number1 + number2
   print(number3)
elif operator == '-':
  number3 = number1 - number2
  print(number3)
elif operator == '*': 
  number3 = number1 * number2
  print(number3)
elif operator == '/':
    number3 = number1 / number2
    print(number3)
elif operator == '%'
    number3 = number1 % number2
    print(number3)

else 
     print('incorrect operation')
     print(number3)