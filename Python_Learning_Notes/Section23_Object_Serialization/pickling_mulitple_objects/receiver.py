import pickle

f = open("emp2.ser", "rb")
print("Deserialize Employee Object & Printing Data")

while True:
    try:
        e = pickle.load(f)
        e.display()
    except EOFError:
        break
        
print("All Employee Objects Deserialized")