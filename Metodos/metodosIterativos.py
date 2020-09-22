import math 

def metIter(value, k):
    first_value = 0.0
    
    #attempt to Approximate e^x for a given value
    try:
        for item in range(k):
            next_value = float(value**item)/math.factorial(item)
            first_value += next_value

        return first_value

    #Raise TypeError if input is not a number     
    except TypeError:
        print ('Please enter an integer or a float value')

if __name__ == "__main__":
    
   maclaurin_exp1 =  metIter(0.5,100)
   print (maclaurin_exp1)
   maclaurin_exp2 =  metIter(3,100)
   print (maclaurin_exp2)
 