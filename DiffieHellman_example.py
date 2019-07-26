Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\micha\Documents\Python programs\GitHub Stuff\MichaelVirnig_DiffeHellman.py 

Please select from the following choices:

	1) Start as Alice

	2) Start as Bob

	3) Exit the program

Enter your choice (1 || 2 || 3): 1






























































Welcome to my Diffie Hellman Key Exchange program!

You may enter Control+C at anytime to bring up the main menu.


You have chosen to start communication as Alice.

Please enter the agreed upon prime number: 7

Based on  7 , Phi is  6

Please enter Alice's Private Key: 	11

Alice computes  11 ^-1 mod 6

The inverse mod of the private key is  5

Please enter Bob's Private key: 	17

Bob computes  17 ^-1 mod 6

The inverse mod of the private key is  5

Enter your Secret Key(k) Value: 	21

Your Secret Key must be less than the Shared Prime minus 1.

Please try again.

Bad input, try again.


Please select from the following choices:

	1) Start as Alice

	2) Start as Bob

	3) Exit the program

Enter your choice (1 || 2 || 3): 1






























































Welcome to my Diffie Hellman Key Exchange program!

You may enter Control+C at anytime to bring up the main menu.


You have chosen to start communication as Alice.

Please enter the agreed upon prime number: 7

Based on  7 , Phi is  6

Please enter Alice's Private Key: 	11

Alice computes  11 ^-1 mod 6

The inverse mod of the private key is  5

Please enter Bob's Private key: 	13

Bob computes  13 ^-1 mod 6

The inverse mod of the private key is  1

Enter your Secret Key(k) Value: 	3


Alice computes  3 ^ 11 mod 7 = 5

Alice sends  5  to Bob ---------------->


			Bob computes  5 ^ 13 mod 7 = 5

	             <---------------- Bob sends  5  to Alice


Alice computes  5 ^ 5 mod 7 = 3

Alice sends  3  to Bob ---------------->


			Bob computes  3 ^ 1 mod 7 = 3

			Bob now has the shared secret key! 3 


Please select from the following choices:

	1) Start as Alice

	2) Start as Bob

	3) Exit the program

Enter your choice (1 || 2 || 3): 2






























































Welcome to my Diffie Hellman Key Exchange program!

You may enter Control+C at anytime to bring up the main menu.


You have chosen to start communication as Bob.

Please enter the agreed upon prime number: 19

Based on  19 , Phi is  18

Please enter Bob's Private key: 	1111

Bob computes  1111 ^-1 mod 18

The inverse mod of the private key is  7

Please enter Alice's Private Key: 	23

Alice computes  23 ^-1 mod 18

The inverse mod of the private key is  11

Enter your Secret Key(k) Value: 	7


Bob computes  7 ^ 1111 mod 19 = 7

Bob sends  7  to Alice ---------------->


			Alice computes  7 ^ 23 mod 19 = 11

	             <---------------- Alice sends  11  to Bob


Bob computes  11 ^ 7 mod 19 = 11

Bob sends  11  to Alice ---------------->


			Alice computes  11 ^ 11 mod 19 = 7

			Alice now has the shared secret key! 7 


Please select from the following choices:

	1) Start as Alice

	2) Start as Bob

	3) Exit the program

Enter your choice (1 || 2 || 3): 
