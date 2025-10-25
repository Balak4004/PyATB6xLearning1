
#You want to check whether a web page loads within 3 seconds (performance test condition).

#load_time = 4.2
#⚠️ Page load too slow: 4.2 seconds

load_time = float(input("enter page load time : ").strip())

if load_time <=0:
    print(" enter valid load time")
else:
    if load_time >=1 and load_time <=3:
        print(f"page load is fast : {load_time} seconds")
    else:
        print(f"page load is slow : {load_time} seconds")