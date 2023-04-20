import argparse
import random
from typing import Dict
from encryptor import NatoAlphabet
from nato_alphabets import nato_alphabet_custom, nato_alphabet_standard
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages using the NATO alphabet.')
    parser.add_argument('message', nargs='?', help='The message to be encrypted or decrypted. If not provided, input will be read from the input file.')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the message.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the message.')
    parser.add_argument('-c', '--custom', action='store_true', help='Use the custom NATO alphabet.')
    parser.add_argument('-i', '--input_file', help='The input file to read the message from.')
    parser.add_argument('-o', '--output_file', help='The output file to write the encrypted or decrypted message to.')
    parser.add_argument('-r', '--random', action='store_true', help='Use a random NATO alphabet.')
    parser.add_argument('-t', '--try_reverse', action='store_true', help='Attempt to decrypt messages using reverse lookup.')
    parser.add_argument('-p', '--image_path', help='The path to the image file.')
    parser.add_argument('-s', '--image_size', nargs=2, type=int, help='The size of the image in pixels.')
    args = parser.parse_args()

    if args.custom:
        nato_alphabet = nato_alphabet_custom
    else:
        nato_alphabet = nato_alphabet_standard

    if args.random:
        nato_alphabet = random.sample(nato_alphabet_standard, len(nato_alphabet_standard))

    if args.message:
        message = args.message
    elif args.input_file:
        with open(args.input_file, 'r') as f:
            message = f.read()
    elif args.image_path and args.image_size:
        na = NatoAlphabet(nato_alphabet)
        if args.encrypt:
            pixel_chars = na.encrypt_image(args.image_path)
            image_data = na._convert_phonetic_equivalents_to_bytes(pixel_chars, args.image_size)
            image = Image.frombytes(mode='RGB', size=args.image_size, data=image_data)
            if args.output_file:
                image.save(args.output_file)
                print(f"Encrypted image written to {args.output_file}.")
            else:
                image.show()
        elif args.decrypt:
            na.decrypt_image(args.image_path, args.image_size)
    else:
        print("Please specify either a message, an input file, or an image file and its size.")
        return

    if args.encrypt and not (args.image_path and args.image_size):
        try:
            na = NatoAlphabet(nato_alphabet)
            encrypted_message = na.encrypt_message(message) 
            if args.output_file:
                with open(args.output_file, 'w') as f:
                    f.write(encrypted_message)
                print(f"Encrypted message written to {args.output_file}.")
            else:
                print("Encrypted message:", encrypted_message)
        except ValueError:
            print("Error: Invalid input. Please enter a valid message to encrypt.")
        except Exception as e:
            print(f"Error occurred during encryption: {e}")
    elif args.decrypt and not (args.image_path and args.image_size):
        try:
            na = NatoAlphabet(nato_alphabet)
            decrypted_message = na.decrypt_message(message)
            if args.try_reverse:
                decrypted_message = na.decrypt_message(message, reverse=True)
            if args.output_file:
                with open(args.output_file, 'w') as f:
                    f.write(decrypted_message)
                print(f"Decrypted message written to {args.output_file}.")
            else:
                print("Decrypted message:", decrypted_message)
        except ValueError:
            print("Error: Invalid input. Please enter a valid message to decrypt.")
        except Exception as e:
            print(f"Error occurred during decryption: {e}")
    else:
        print("Please specify either -e/--encrypt or -d/--decrypt.")

if __name__ == '__main__':
    main()





