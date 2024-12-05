from PIL import Image

def encrypt_image(image_path, key):
    """Encrypts an image by swapping pixel values based on a key.

    Args:
        image_path: Path to the image to be encrypted.
        key: A numeric key to control the swapping pattern.

    Returns:
        The encrypted image.
    """

    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            new_x = (x + key) % width
            new_y = (y + key) % height
            pixels[x, y], pixels[new_x, new_y] = pixels[new_x, new_y], pixels[x, y]

    return img

def decrypt_image(encrypted_image, key):
    """Decrypts an encrypted image using the same key and swapping pattern.

    Args:
        encrypted_image: The encrypted image.
        key: The same numeric key used for encryption.

    Returns:
        The decrypted image.
    """

    return encrypt_image(encrypted_image, -key)

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption key: "))

    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save("encrypted_image.jpg")
    print("Image encrypted successfully!")

    decrypted_image = decrypt_image("encrypted_image.jpg", key)
    decrypted_image.save("decrypted_image.jpg")
    print("Image decrypted successfully!")