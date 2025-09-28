import math
def main():
  num_1 = float(input("Enter the first number: "))
  char_1 = input("Enter the operator: ")
  if char_1 in ("+","-","X","x","*","/","÷","^"):
    arith(num_1,char_1)
  elif char_1 in ("sqrt","Sqrt","!","cbrt","Cbrt","√","fact"):
    non_arith(num_1,char_1)
  elif char_1 in ("Combination","C","c","Comb","p","Permutation","permute","P"):
    selection(num_1,char_1)
def arith(num_1,char_1):## used the same Variables for easier recognition 
  num_2 = float(input("Enter the Second Number: "))
  match char_1:
    case "+":
      print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case "-":
      print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case "X"|"x"|"*":
      print (f"{num_1 } x {num_2} = {num_1 * num_2}")
    case "/"|"÷":
      print(f"{num_1} ÷ {num_2} = {num_1 / num_2}")
    case "^":
      from sympy import symbols,pretty
      base = symbols(str(int(num_1)))
      print(f"{pretty(base ** int(num_2))} = {int(num_1) ** int(num_2)}")
def non_arith(num_1,char_1):
  match char_1:
    case "sqrt"|"Sqrt"|"√":
      if num_1 < 0:
        print("Invalid Enteries")
      else:
          print(f"The Square root of {num_1} is {math.sqrt(num_1)}")
    case "cbrt"|"Cbrt":
      if num_1 < 0:
        print("Invalid Enteries")
      else:
        print(f"The Cube root of {num_1} is {math.cbrt(num_1)}")
    case "fact"|"!":
      if num_1<0:
        print("Invalid Entry")
      print(f"The Factorial of {int(num_1)} is {math.factorial(int(num_1))}")
def selection(num_1,char_1):
  num_2=int(input("Enter the number of items to be selected: "))
  from sympy import symbols,pretty
  match char_1:
    case "P"|"Permutation"|"p"|"permute":
      print(f"{int(num_1)} P {int(num_2)} = {math.perm(int(num_1),int(num_2))}")
    case "C"|"c"|"Combination"|"comb":
      print(f"{int(num_1)} C {int(num_2)} = {math.comb(int(num_1),int(num_2))}")
main()