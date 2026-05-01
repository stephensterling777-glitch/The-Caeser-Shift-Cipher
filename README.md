# The Caeser Cipher Shift

The Caeser Cipher Shift is one of the oldest cryptographic methods in human history. Given an alphabet, which is a group of letters that can be represented by integers, we then take on of those integers and call it a key. This key is then applied to each letter in our message by shifting it down that number of places in the alphabet group. For example, suppose 

$$\mathbb{A} = {a,b,c,...,x,y,z}$$

That is, all the lower case letters in the English alphabet. Then, the equivalent modulus group is

$$\mathbb{Z}_{26} = {0,1,2...,23,24,25}$$

If our message is 'abc' and our key 1, then we take each letter and shift it down by 1. Since our message is equivalent to '012', we take each of those numbers and add 1, making it '123.' The equivalent letter sequence after our encryption is 'bcd.' 'hello' likewise would become 'ifmmp.'

What if we want to decrypt the message? If we know the key is 1, then we simply have to find the inverse of 1 and apply it to our encrypted message. In the case of \mathbb{Z}_26, this is technically 25. Note that -1 does not exist as an integer in our group. However, if we add 25 to 1 in \mathbb{Z}_26, then we get 0 (not 26). So, if we have 'jqyfa' with key 2, then we take each letter and add 24 to get 'howdy.' Of course, it is much more practical to go backwards 2 then to go forward 24, but for the sake of mathematical rigor, we will continue to work under the correct modulus.

## How the program works:
1. The user is asked to input a message, either encrypted or decrypted.
2. The user is asked to input a key, which is then converted to an integer and operated under a modulo of the length of the alphabet group.
3. There are two functions that are nearly identical. One takes the message and encrypts by adding the key, while the other takes the message and decrypts it by subtracting the key.

### Notes:
1. In this program, the key does not have to be limited to the modulus group since there are modulo operators throughout the code preventing any out of bound errors.
2. Although the functions could be combined into one, the author has chosen for now to keep them separate so that he may experiment with the code a little bit more.

## How to run:
Requires Python 3. Download and run: 
	python caeser_shift.py
