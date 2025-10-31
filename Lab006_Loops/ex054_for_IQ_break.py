
# for IQ question check output using break to stop execution once condition is true

for i in range(0,10):
    if i == 5:
        print("Five")
        break
    else:
        print(i)

# i | condition | output
# 0 | 0 == 5 -> False | o/p = 0
# 1 | 1 == 5 -> False | o/p = 1
# 2 | 2 == 5 -> False | o/p = 2
# 3 | 3 == 5 -> False | o/p = 3
# 4 | 4 == 5 -> False | o/p = 4
# 5 | 5 == 5 -> False | o/p = Five