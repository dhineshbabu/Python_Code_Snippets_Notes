from emp import Employee
import pickle

f = open("emp2.ser", "wb")

while True:
    eno = int(input("Enter employee number: "))
    ename = input("Enter employee name: ")
    esal = float(input("Enter salary: "))
    eaddr = input("Enter address: ")
    e = Employee(eno, ename, esal, eaddr)
    pickle.dump(e,f)
    option = input("Do you want to serialize another object [yes/no] : ")
    if option.lower() == 'no':
        break
        
print(" Multiple Employee Objects Serialized")