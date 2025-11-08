

# Response time in millsec to sec

response_time_ms = [1200,1500,1800]

def resp_time_sec(x):
    return x/1000

resp_time_sec = list(map(resp_time_sec,response_time_ms))
print(resp_time_sec)