def isInt(n):
    try:
        n= int(n)
        return n
    except:
        print("{}Não é um numero{}".format("\033[1;31m","\033[m"))

def isIntPro(n,first,last):
    try:
        n= int(n)
        if not(first<n<=last):
            print("{}Não é um numero valido!{}".format("\033[1;31m","\033[m"))    
            return False 
        else:
            return n 
    except:
        print("{}Não é um numero{}".format("\033[1;31m","\033[m"))    
        return False    
