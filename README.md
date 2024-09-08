# totpgen.py

TOTPgen.py randomly creates a secret, generates an OTP, and then asks you to type it back in to verify it. To avoid confusion, the program also displays how long you have left before the OTP changes again.

Below, you will find the entire source code. Scroll down past it to see a [line-by-line breakdown](#code-explanation) of the code and how it works.

```python
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
```

## Code Explanation

### Generate a Secret

```python
secret = pyotp.random_base32()
```

To generate a TOTP, we must first have a secret from which to derive it. The code above generates said secret, encoded in base32.

We use base32 because it is a compact and human-readable encoding scheme that is more resistant to errors when users manually transcribe it. It encodes binary data into a more compact text format.

```
FGVHOSDH3BGDXW47TZ65TCSQXZPIA5OD
```

Above is an example of a base32 secret generated with the program. When manually transcribing this secret for safekeeping, you may notice that it is all uppercase letters. It also excludes 1 and 0, as they can be too easily confused with lowercase L and uppercase `o`. The digits 8 and 9 are also excluded.

When manually saving a secret, even one error can cause the user to lose access if they ever have to restore the secret.

### Generate TOTP

```python
totp = pyotp.totp(secret)
```

The code above actually generates the TOTP secret.

### Output Secret

```python
print("secret> ", secret)
```

The secret must be shown at the point of generation to enable the user to back it up. This is often displayed as a QR code.

### Output TOTP

```python
print("totp> ", totp.now())
```

The code above outputs the actual TOTP code, which will have to be verified.

### Output Time Window

```python
time_remaining = 30 - (time.time() % 30)
print(f"time remaining> {int(time_remaining)} seconds")
```

When entering the TOTP, it is crucial to know how much time you have remaining in the 30-second window that TOTP usually uses.

`time.time()` gives the number of seconds since the start of the Unix epoch (January 1st, 1970). The value that is returned is a floating-point number that contains both seconds and fractions of a second.

`time.time() % 30` calculates how many seconds have passed since the start of the current 30-second interval, as `%` gives the remainder. We then subtract that from 30 in order to get the remaining number of seconds in a 30-second window.

Finally, we use `int(time_remaining)` to convert the number of seconds into an integer, as we do not need the decimal portion.

### TOTP Verification

```python
code = input("verification> ")
print(totp.verify(code))
```

Finally, the program asks for user input and checks it against the current TOTP. The returned value is a boolean, either `True` or `False`.
