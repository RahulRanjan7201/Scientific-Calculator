import math 

while True : 
    print("\n Choose the math Operation. \n\n" +
    "0 - Addition\n1 - Subtraction \n2 - Multiplication\n" + 
    "3 - Division \n4 - Modulo\n5 - Raising to a power \n" +
    "6 - Square Root\n7- Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    oper = input("\nYour option from the menu : ")
    
    if oper == "0" :
        val1 = float(input("\n First value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is : " + str(val1 + val2) + "\n")
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
    #Subtraction
    elif oper == "1" :
        val1 = float(input("\n First value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is : " + str(val1 - val2) + "\n")
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
    #Multiplication
    elif oper == "2" :
        val1 = float(input("\n First value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is : " + str(val1 * val2) + "\n")
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
            
    #Division
    elif oper == "3" :
        val1 = float(input("\n First value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is : " + str(val1 / val2) + "\n")
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
            
            
    #Modulo
    elif oper == "4" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(val1 % val2) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
    
    #Raising to the power
    elif oper == "5" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.pow(val1 , val2)) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
            
    #Square root
    elif oper == "6" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.sqrt(val1 , val2)) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
            
    #Logarithm
    elif oper == "7" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.log(val1 , val2)) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
            
    #Sine
    elif oper == "8" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break
    
    #Cosine
    elif oper == "8" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break    
    #Tangent
    #Cosine
    elif oper == "8" :
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        
        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
        
        #Going back to the main menu or exiting the program
        back = input("\n Go back to main menu? (y/n)")
        if back == "y" : 
            continue
        else :
            break        