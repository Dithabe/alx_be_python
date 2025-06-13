def perform_operation(num1, num2, operation):
    
    num1 = float(num1)
    num2 = float(num2)
    operation = str(operation)
    
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "devide":
            
            if num2 != 0:
                return num1 / num2
            else:
                print(f"The num1 value you have entered is {num2}. This is results to maths error")
        case _:
            print("Invalid choice, recheck and try again")
    
    
    
