# STRFTIME METHOD
import time

counter = 1
end = 5

while counter <= end:
    clock = time.strftime("%Y.%m.%d %H:%M:%S")
    print(clock, "\r", end="", flush=True)
    counter += 1
    time.sleep(1)