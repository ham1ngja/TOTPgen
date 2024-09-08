import time

import pyotp

# Generate a random secret
secret = pyotp.random_base32()

# Generate a time-based OTP from the secret
totp = pyotp.totp(secret)

# Output secret for backup purposes
print("secret> ", secret)

# Ouput the current totp
print("totp> ", totp.now())

# Calculate and output how many seconds are left until the TOTP changes
time_remaining = 30 - (time.time() % 30)
print(f"time remaining> {int(time_remaining)} seconds")

# Enter the TOTP, for verification purposes
code = input("verification> ")

# Verify the code
print(totp.verify(code))
