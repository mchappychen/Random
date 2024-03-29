# Random

This is a random number generated using the quantum rng from Australia National University: https://qrng.anu.edu.au/contact/api-documentation/ to generate random numbers from a to b inclusive.

We turn the numbers received by QRNG into bits, then only use the amount of bits we need to generate a uniform distribution of numbers from a to b inclusive using rejection sampling.

For example, if you want to generate a random number from 0 to 4, the highest number 4 is represented as 100 in binary. But if each binary digit is uniformly distributed, it is possible to get the digits 111, which is 7 and outside of the range 0 to 4. Therefore we just regenerate all the binary digits again until we have a number within range to ensure the uniformity of the distribution.

QRNG API only allows 1 call per minute, so we make a request for 1024 hex codes (0-255 in decimal), and convert it into binary (each bit is still uniformly distributed), and store it as a file. Only when we run out of bits in our file do we make another API call to QRNG. Since there's 8 bits in 0-255 in decimal, we get 8x1024 = 8192 bits per API call.

This also means this random number generator I made only supports numbers up to 2^8192-1 but that's 1.3×10^2466 so you should be good.
