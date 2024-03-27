# Random

This is a random number generated using the quantum rng from Australia National University: https://qrng.anu.edu.au/contact/api-documentation/ to generate random numbers from a to b inclusive.

We turn the numbers received by QRNG into bits, then only use the amount of bits we need to generate a uniform distribution of numbers from a to b inclusive using rejection sampling.

For example, if you want to generate a random number from 0 to 4, the highest number 4 is represented as 100 in binary. But if each binary digit is uniformly distributed, it is possible to get the digits 111, which is 7 and outside of the range 0 to 4. Therefore we just regenerate all the binary digits again until we have a number within range.

QRNG API only allows 1 call per minute, so we make a request for 1024 hex codes (0-255 in decimal), and convert it into binary by doing % 2, and store it as a file. Only when we run out of bits in our file do we make another API call to QRNG.

This also means this random number generator I made only supports numbers up to 2^1024-1 but that's a number between googol and googolplex so you should be fine.
