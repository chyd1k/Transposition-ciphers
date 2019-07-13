# Transposition-ciphers and Vigenere cipher
This application allows you to encrypt and decrypt messages with Vigenere cipher and some transposition ciphers. It has user interface so
i hope you enjoy to use it :)

<img src="https://psv4.userapi.com/c848228/u141400706/docs/d18/f6c0e026ccbe/1.png?extra=W_abdFAA2aLpRX5SaZT4c_6iCCotADosmJm1OlWBQSuxjj5SFJ5CxQ0_SOt8DM_OQ9QVTGeAH5CvXqkbOu2K2LcDakUDIkPUGzjIgIvurkoSGgRwoQyc1ewLlJXtPTUtsyCogYbS1j3nfixTIE2h365M">

The application allows you to encrypt and decrypt text messages with using the Vigenere, Scytale, Rail Fence,
Vertical and Double transposition ciphers.

# Vigenere cipher:
In my program I used ASCII table. This solution made it possible to encrypt messages consisting not only of uppercase Latin letters, 
but also numbers and special characters. 

The result of encryption is also presented in the form of printable characters.

# Scytale cipher:
In the classical Scytale cipher as the encryption key is used the number of turns of the band, that in fact, 
is a number that indicates the dimension of the blocks on what the message is splitting.

In my program, as the encryption key, I use the number of blocks, not their dimension (rows_amount).

The number that indicates the dimension of the blocks on what the message is splitting is calculated as:

<code>columns_amount = int(len(mes) / rows_amount)</code>

 The message is then read off in columns.

# Rail fence cipher:
In the rail fence cipher, the plain text is written downwards and diagonally on successive "rails" of an imaginary fence, 
then moving up when the bottom rail is reached. 
When the top rail is reached, the message is written downwards again until the whole plaintext is written out.
The message is then read off in rows.

# Vertical transposition cipher:
Plain text is written horizontally with a fixed width, and the ciphertext is read vertically in the order specified by the user.

# Double transposition cipher:
Plain text is written horizontally with a fixed width. After this columns are changing thier places in the specified by the user order.
The same step applies to rows. The message is then read off in rows.
