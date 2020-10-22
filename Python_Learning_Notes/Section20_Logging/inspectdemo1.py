import inspect

def getInfo():
    #print(inspect.stack()[1])
    print("Caller Module: ",inspect.stack()[1][1])
    print("Caller Function Name: ", inspect.stack()[1][3])
    
    