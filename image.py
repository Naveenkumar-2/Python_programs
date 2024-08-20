from PIL import Image
import numpy as np

def xor_encrypt_decrypt(image_path, key):
    # Open image and convert to numpy array
    image = Image.open(image_path)
    image_array = np.array(image)

    # Convert key to a numpy array with the same shape as the image
    key_array = np.array(key, dtype=np.uint8)
    key_array = np.resize(key_array, image_array.shape)

    # XOR operation for encryption/decryption
    encrypted_decrypted_array = np.bitwise_xor(image_array, key_array)

    # Convert numpy array back to image
    result_image = Image.fromarray(encrypted_decrypted_array)
    return result_image

# Example key (must be of the same size as the image)
# You might need to adjust key length or generate it appropriately
def generate_key(image_path):
    image = Image.open(image_path)
    key = np.random.randint(0, 256, size=image.size[::-1] + (3,), dtype=np.uint8)
    return key

# Path to your image file
image_path = 'example.jpg'

# Generate key and encrypt the image
key = generate_key(image_path)
encrypted_image = xor_encrypt_decrypt(image_path, key)
encrypted_image.save('encrypted_image.png')

# Decrypt the image
decrypted_image = xor_encrypt_decrypt('encrypted_image.png', key)
decrypted_image.save('decrypted_image.png')
