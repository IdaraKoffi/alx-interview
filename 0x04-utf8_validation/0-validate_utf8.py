#!/usr/bin/python3
"""UTF-8 Validation Function"""


def validUTF8(data):
    """Check if a list of integers represents a valid UTF-8 encoding."""
    n_bytes = 0

    for num in data:
        # Keep only the last 8 bits of each integer
        byte = num & 0xFF

        if n_bytes == 0:
            # Check how many 1s at the start of the byte
            if byte >> 7 == 0:
                continue  # 1-byte character
            elif byte >> 5 == 0b110:
                n_bytes = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                n_bytes = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                n_bytes = 3  # 4-byte character
            else:
                return False
        else:
            # Check if it is a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
