"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.
Hint: Use a counter (like wait_time) and break condition.
"""

import time
import random

wait_time = 0
page_load = False

def api_response():
    return random.choice([False,False,False,True])

while wait_time < 5:
    #page_load = input("Enter True/false")
    page_load = api_response()
    if page_load:
        print(f"page loaded in {wait_time+1} seconds")
        break

    else:
        print(f"Checking...(second {wait_time+1})")
        time.sleep(1)
        wait_time = wait_time + 1

if not page_load:
        print("Page load failed after 5 seconds")









'''
#import time
wait_time = 0

while wait_time < 5:
    page_loaded = input("Is the page loaded? (True/False): ").strip().lower()
    if page_loaded == "true":
        print("Page loaded successfully in ",wait_time + 1, "seconds.")
        break

    print("Attempt : ",page_loaded, "time taken : ",wait_time + 1, " : seconds")
    wait_time = wait_time + 1

else:
    print("Timeout: Page did not load within 5 seconds.")

'''