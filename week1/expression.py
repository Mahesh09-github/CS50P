def main():
   expression=input(" Enter the Expression: ")
   print(calculate_expression(expression))

def calculate_expression(expression): 
   x,y,z=expression.split()
   x=float(x)
   z=float(z)
   if y=="+":
      return x+z
   elif y=="-":
      return x-z
   elif y=="*":
      return x*z
   elif y=="/":
      return x/z
   else:
      return "enter a valid expression"


 
