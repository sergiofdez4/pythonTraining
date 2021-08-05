import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        print(mins, secs)
        time.sleep(1)
        t -= 1

t = input("Enter the time in seconds: ")

countdown(int(t))