studentname = str(input('Please enter name:'))
mark1 = int(input('Enter mark of IT Homework:'))
mark2 = int(input('Enter mark of IT Homework:'))
mark3 = int(input('Enter mark of IT Homework:'))

def totalGrade(mark1, mark2, mark3):
    if mark1 <= mark1/25:
      print('studentname:' + '%')
    elif mark2 <= mark2/50:
      print('studentname:' + '%')
    elif mark3 <= mark3/100:
      print('studentname:' + '%')
    else:
        result = str(mark1+mark2+mark3)
        if result >= 80:
               mark = 'A'
        elif  result >= 64:
               mark = 'B'
        elif result >= 54:
               mark = 'C'
        elif result >= 45:
              mark = 'D'
    
    return mark
print('studentname:',studentname,'grade is', totalGrade)