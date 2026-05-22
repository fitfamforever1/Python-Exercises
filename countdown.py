import time

# Variable
x = int(input("Enter the number of seconds for the countdown: "))

# Countdown loop
for i in reversed(range(1, x + 1)):
    seconds = i % 60
    minutes = (i // 60) % 60 
    hours = (i // 3600) % 24
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)

# Final message
print("Time's up!")