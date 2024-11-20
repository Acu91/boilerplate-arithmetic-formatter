import re
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

def arithmetic_arranger(problems, solve=False):
  if len(problems)>5:
    return "Error: Too many problems."
    
  sum=""
  first=""
  second=""
  operator=""
  

  lines=""
  res=""
  sumx=""
  firstN=""
  secondN=""

  
  for problem in problems:
    if re.search('[a-z]',problem):
      return("Error: Numbers must only contain digits.")
    elif re.search('["/*]',problem):
      return("Error: Operator must be '+' or '-'.")
      
  for problem in problems:  
    first=problem.split(" ")[0]
    operator=problem.split(" ")[1]
    second=problem.split(" ")[2]
    if len(first)>=5 or len(second)>=5:
      return("Error: Numbers cannot be more than four digits.")

    if operator=="+":
      sum=int(first)+int(second)
    else:
      sum=int(first)-int(second)

    
    lenght=max(len(first),len(second))+2
    
    top=str(first).rjust(lenght)
    bottom=operator + str(second).rjust(lenght-1)
    res=str(sum).rjust(lenght)
    
    line=""
    for i in range(lenght):
      line=line+"-"

    if problem != problems[-1]:
      firstN = firstN + top + '    '
      secondN = secondN + bottom + '    '
      lines = lines + line + '    '
      sumx = sumx + res + '    '
    else:
      firstN += top
      secondN += bottom
      lines += line
      sumx += res

  if solve:
    print(str(firstN)+ "\n" + str(secondN) + "\n" + lines + "\n" + str(sumx))
    string=str(firstN)+ "\n" + str(secondN) + "\n" + lines + "\n" + str(sumx)
  else:
    print(str(firstN)+ "\n" + str(secondN) + "\n" + lines)
    string=str(firstN)+ "\n" + str(secondN) + "\n" + lines

  return string
