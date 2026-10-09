
def add_numbers(num1, num2):
  return num1 + num2
def subtract_numbers(num1, num2):
  return num1 - num2
def multiply_numbers(num1, num2):
  return num1 * num2
def divide_numbers(num1, num2):
  if num2 == 0:
    return "Cannot divide by zero."
  return num1 / num2 

def main():
  num1 = float(input("enter first number: "))
  num2 = float(input("enter second number: "))

  print("/nChoose operation:")
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  
  choice = input("Enter choice: ")

  if choice == "1":
    result = add_numbers(num1, num2)
    elif choice == "2":
        result = subtract_numbers(num1, num2)
    elif choice == "3":
        result = multiply_numbers(num1, num2)
    elif choice == "4":
        result = divide_numbers(num1, num2)
    else:
        result = "Invalid choice selected."

    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()

  
  
