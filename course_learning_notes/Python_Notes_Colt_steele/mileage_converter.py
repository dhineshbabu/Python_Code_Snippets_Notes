print("How manu kilometers did you cycle today?")
kms = float(input())
#miles = str(float(kms) / 1.690934)
miles = float(kms) / 1.690934
miles = round(miles, 2)  # to reduce it to 2 decimal places
print(f"You have crossed {kms} kilometers and this is equal to {miles} miles")
