def simple_md5(message):
    # Initial values (4 x 32-bit registers)
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Convert message to bytes and add padding
    msg_bytes = bytearray(message.encode())
    
    # Add initial padding bit
    msg_bytes.append(0x80)
    
    # Add padding zeros
    while len(msg_bytes) % 64 != 56:
        msg_bytes.append(0)
    
    # Add message length in bits as last 8 bytes
    msg_length = (8 * len(message)) & 0xffffffffffffffff
    msg_bytes += msg_length.to_bytes(8, byteorder='little')

    # Process each 64-byte chunk
    for chunk_start in range(0, len(msg_bytes), 64):
        chunk = msg_bytes[chunk_start:chunk_start + 64]
        
        # Break chunk into 16 32-bit words
        words = [int.from_bytes(chunk[i:i + 4], byteorder='little')
                for i in range(0, 64, 4)]

        # Save original values
        AA, BB, CC, DD = A, B, C, D

        # Main loop - simplified to just one round type
        for i in range(16):
            # Simple mixing function
            F = (B & C) | (~B & D)
            
            # Update values
            temp = D
            D = C
            C = B
            B = B + ((A + F + words[i]) & 0xFFFFFFFF)
            A = temp

        # Add chunk result to running total
        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    # Convert final values to hex string
    return ''.join(format(x, '08x') for x in [A, B, C, D])

# Test the function
if __name__ == "__main__":
    test_str = "Hello, World!"
    print(f"Simplified MD5 of '{test_str}': {simple_md5(test_str)}")