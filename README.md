# NATO Phonetic Alphabet Encryptor
## Overview
The "NATO Phonetic Alphabet Encryptor" program provides functionalities to encrypt and decrypt messages using the NATO phonetic alphabet. It also allows users to encrypt and decrypt images using the same encryption algorithm.

## Files
The program consists of the following files:

- encryptor.py: contains the implementation of the NatoAlphabet class, which provides the encryption and decryption functionalities for both messages and images.
- nato_alphabets.py: contains the definitions of two NATO phonetic alphabet dictionaries: nato_alphabet_standard and nato_alphabet_custom.
- nato_main.py: contains the main function that utilizes the functionalities provided by the NatoAlphabet class to encrypt or decrypt messages.
## Usage
The program can be used through the command line. The following arguments can be used:

message: the message to be encrypted or decrypted. If not provided, input will be read from the input file.
- -e, --encrypt: encrypt the message.
- -d, --decrypt: decrypt the message.
- -c, --custom: use the custom NATO alphabet.
- -i, --input_file: the input file to read the message from.
- -o, --output_file: the output file to write the encrypted or decrypted message to.
- -r, --random: use a random NATO alphabet.
- -t, --try_reverse: attempt to decrypt the message using both the standard and custom NATO alphabets.
## Encryption Algorithm
The encryption algorithm uses the NATO phonetic alphabet to replace each character in the message with its corresponding NATO word. Spaces are preserved. For example, the message "HELLO WORLD" would be encrypted as "Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta".

For image encryption, the algorithm converts each pixel in the image to its corresponding NATO word based on its RGB value. The resulting string of NATO words is used as the encrypted message.

## Decryption Algorithm
The decryption algorithm reverses the encryption process. Each NATO word in the encrypted message is replaced with its corresponding character in the standard or custom NATO alphabet. Spaces are preserved. For example, the encrypted message "Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta" would be decrypted as "HELLO WORLD".

For image decryption, the algorithm converts each NATO word in the encrypted message back to its corresponding RGB value. The resulting pixel values are used to reconstruct the original image.

## Dependencies
The program requires the following dependencies:

Pillow: a fork of the Python Imaging Library (PIL), which is used to handle image inputs and outputs.
## Examples
Encrypt the message "HELLO WORLD" using the standard NATO alphabet:
```python
python nato_main.py "HELLO WORLD" -e
```
Decrypt the message "Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta" using the custom NATO alphabet and write the output to a file:
```python
python nato_main.py "Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta" -d -c -o decrypted.txt
```
Encrypt an image file named input.png using a random NATO alphabet and save the resulting encrypted message to a file named encrypted.txt:
```python
python nato_main.py -e -r -i input.png -o encrypted.txt
```
Decrypt an image file named encrypted.png using both the standard and custom NATO alphabets and display the resulting images:
```python
python nato_main.py -d -t -i encrypted.png
```