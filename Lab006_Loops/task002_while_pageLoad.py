"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""

import time

wait_time = 0

while wait_time < 5:
    page_loaded = input("Is the page loaded? (True/False): ").strip().lower()

    if page_loaded == "true":
        print("Page loaded successfully in ",wait_time + 1, "seconds.")
        break

    print("Attempt : ",page_loaded, "time taken : ",wait_time + 1, " : seconds")
    time.sleep(1)
    wait_time += 1

else:
    print("Timeout: Page did not load within 5 seconds.")