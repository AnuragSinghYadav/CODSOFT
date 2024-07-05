#making simple calculator using python
num_1 = int(input("Enter the number1 = "))
num_2 =  int(input("Enter the number2 ="))

operator = (input("Enter operator: "))

match operator:
    case "+":
        print("Sum is", num_1 + num_2)
    case "-":
        print("Difference is", num_1 - num_2)
    case "*":
        print("Product is", num_1 * num_2)
    case "/":
        print("Division is  = ", num_1 / num_2)
    case"%":
        print("Percentage is", num_1 % num_2)
    case _ :
        print("Enter a valid operatoer")            

        
        
