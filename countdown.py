# Countdown timer using functions

# Module
import time

# Countdown function
def countdown(x, y = 1):
    while x > 0:
        timer(x)
        time.sleep(y)
        x -= 1
    print("Blastoff!")

# Timer display function
def timer(i):
    seconds = i % 60
    minutes = (i // 60) % 60 
    hours = (i // 3600) % 24
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# Example usage
countdown(10) 
