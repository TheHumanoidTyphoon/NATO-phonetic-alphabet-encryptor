from typing import Dict
from PIL import Image
from io import BytesIO


class NatoAlphabet:
    def __init__(self, alphabet: Dict[str, str]):
        self.alphabet = alphabet

    def encrypt_message(self, message: str) -> str:
        encrypted_chars = []
        for char in message.upper():
            if char == " ":
                encrypted_chars.append(" ")
            elif char not in self.alphabet:
                raise ValueError("Invalid character in message.")
            else:
                encrypted_chars.append(self.alphabet[char])
        return " ".join(encrypted_chars)

    def decrypt_message(self, message: str) -> str:
        decrypted_chars = []
        for word in message.split(" "):
            if word == "":
                decrypted_chars.append("")
            elif word not in self.alphabet.values():
                raise ValueError("Invalid word in message.")
            else:
                decrypted_chars.append(list(self.alphabet.keys())[list(self.alphabet.values()).index(word)])
        return "".join(decrypted_chars)

    def _convert_image_to_phonetic_equivalents(self, image):
        pixels = list(image.getdata())
        pixel_chars = []
        for pixel in pixels:
            pixel_chars.append(self.alphabet[str(pixel)])
        return "".join(pixel_chars)

    def encrypt_image(self, image_path: str) -> str:
        with Image.open(image_path) as image:
            if image.format in ["PNG", "JPEG", "GIF"]:
                image = image.convert("RGB")
            else:
                raise ValueError("Unsupported image format.")
            pixel_chars = self._convert_image_to_phonetic_equivalents(image)
        return pixel_chars

    def decrypt_image(self, image_path: str, size: tuple) -> None:
        with Image.open(image_path) as image:
            if image.format in ["PNG", "JPEG", "GIF"]:
                image = image.convert("RGB")
            else:
                raise ValueError("Unsupported image format.")
            pixel_chars = image.read()
        pixel_values = []
        for row in pixel_chars:
            for pixel in row:
                pixel_value = list(self.alphabet.keys())[list(self.alphabet.values()).index(pixel)]
                pixel_values.append(eval(pixel_value))
        image_data = bytes(pixel_values)
        with Image.frombytes(mode='RGB', size=size, data=image_data) as image:
            image.show()







