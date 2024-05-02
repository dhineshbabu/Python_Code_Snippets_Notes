import time
import demo2
from imp import reload

demo2.add(10,20)
print("Enter into sleeping state")
time.sleep(40)
reload(demo2)
# print("Just wake up... tyring to module again")
# import demo2 #importing module again after update
demo2.mul(10,20)