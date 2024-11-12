def simple_hash(message):
    """Very simplified hash function demonstrating basic concepts"""
    # Convert message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode()

    # Initialize simple hash values
    h1 = 0x6a09e667
    h2 = 0xbb67ae85

    # Basic padding: add a '1' bit and zeros
    padded = message + b'\x80' + b'\x00' * (64 - len(message) - 1)

    # Process message in chunks of 8 bytes
    for i in range(0, len(padded), 8):
        chunk = padded[i:i+8]
        
        # Convert chunk to integer
        value = int.from_bytes(chunk, byteorder='big')

        # Simple mixing operations
        h1 = (h1 + value) & 0xFFFFFFFF
        h2 = (h2 ^ h1) & 0xFFFFFFFF
        
        # Simple rotation
        h1 = ((h1 << 13) | (h1 >> 19)) & 0xFFFFFFFF
        h2 = ((h2 << 7) | (h2 >> 25)) & 0xFFFFFFFF

    # Combine hash values
    final_hash = (h1 << 32) | h2
    return hex(final_hash)

# Example usage
if __name__ == "__main__":
    message = "Hello, World!"
    result = simple_hash(message)
    print(f"Simple hash of '{message}': {result}")