import sys

# Allows printing numbers larger than 4300 digits
sys.set_int_max_str_digits(0)

# 10**5 is large but won't crash your RAM immediately
limit = 10**5 

try:
    for i in range(1, limit):
        # Using f-string or str() here works because of set_int_max_str_digits(0)
        print(i)
except KeyboardInterrupt:
    print("Stopped.")
