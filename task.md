# Explanation

## Step-by-Step

1. On line one the user is asked for the bottom hole pressure and converted to a float (decimal since comparison operations cannot be done on string and numbers)

2. Line 3 checks for the safe zone threshold, same for the elif.

3. The else does not check for anything since if it's not in either the safe, or warning zones it will definitely be in the critical zone

4. The last line prints the message
