def truebooj(number):
    #instantiate an array of attributes to be applied to a given number
    attributes = []
    
    #if a number cleanly divides by three, add "true" to the attributes array
    if (number % 3 == 0):
        attributes.append("True")
        
    #if a number cleanly divides by five, add "booj" to the attributes array    
    if (number % 5 == 0):
        attributes.append("Booj")
        
    #if a number cleanly divides by ten, add "true booj" to the attributes array    
    if (number % 10 == 0):
        attributes.append("True Booj")
        
    #the if statements are constructed to be non-mutually exclusive -- ex: 30 should have all three attributes 
    print number, attributes