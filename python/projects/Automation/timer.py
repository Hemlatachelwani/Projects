import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1) # by this, it will wait n display after 1 sec, try commenting it.
        seconds -= 1
    print("Time's up!")

# Set the desired countdown time in seconds
countdown_time = 6 # For example, a 10-second timer
countdown_timer(countdown_time)

# output :
/Users/hemlata/IdeaProjects/ApnaCollegePython/venv/bin/Python /Users/hemlata/IdeaProjects/DSAJavaApnaColgCoursePrcts/src/TimerPython/timerr.py 
Time remaining: 6 seconds
Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!

Process finished with exit code 0
