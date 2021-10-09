# Timers
# Execute code at timed intervals
# This is the first step in learning threading

# Imports and display

import time
from threading import Timer

def display(msg):
    print(msg + ' ' +  time.strftime('%H:%M:%S'))


# Basic Timer
def run_once():
    display('Run once: ')
    # This will wait for 5 seconds and call the display function in another thread
    t = Timer(5, display, ['Timeout:'])
    t.start()


run_once()
print('waiting...')

# Interval Timer
# Wrap it into a class
# Make it until we stop it
# Notice we can have multiple timers at once
class RepeatTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')


# Really we are making a thread and controlling it
timer = RepeatTimer(1, display, ['Repeating'])
timer.start()  # Going to call run() inside RepeatTimer class
print('threading started...')
time.sleep(10)  # suspends the execution for the given number of seconds
print('threading finishing...')

timer.cancel()