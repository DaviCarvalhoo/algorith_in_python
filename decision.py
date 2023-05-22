import datetime
#Banner
import os
type = "Greetings"
os.system(f"figlet  -f ~/fonte_banner/figlet-fonts/3d.flf {type} | lolcat")

#Get the name
name = input("What's your name?")

# Get the current time
current_time = datetime.datetime.now().time()

# Define the greeting times
morning_start = datetime.time(6, 0)
afternoon_start = datetime.time(12, 0)
evening_start = datetime.time(18, 0)
night_start = datetime.time(0, 0)

# Check the current time and print the corresponding greeting
if current_time >= morning_start and current_time < afternoon_start:
    print("Good morning! "+name)
elif current_time >= afternoon_start and current_time < evening_start:
    print("Good afternoon! "+ name)
elif current_time >= evening_start or current_time < night_start:
    print("Good evening! "+name)
else:
    print("Good night! "+ name)