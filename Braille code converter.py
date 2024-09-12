import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port
time.sleep(2)  # Wait for the connection to establish

# Define the binary representations for each letter
braileMap = {
    'A': '100000', 'B': '110000', 'C': '100100', 'D': '100110', 'E': '100010',
    'F': '110100', 'G': '110110', 'H': '110010', 'I': '010100', 'J': '010110',
    'K': '101000', 'L': '111000', 'M': '101100', 'N': '101110', 'O': '101010',
    'P': '111100', 'Q': '111110', 'R': '111010', 'S': '011100', 'T': '011110',
    'U': '111001', 'W': '010111', 'X': '101101', 'Y': '101111', 'Z': '101011'
}

# Define the Braille patterns for 0-9
braille_numbers = [
    '100110',  # 0 (⠚)
    '100000',  # 1 (⠁)
    '110000',  # 2 (⠃)
    '100100',  # 3 (⠉)
    '100110',  # 4 (⠙)
    '100010',  # 5 (⠑)
    '110100',  # 6 (⠋)
    '110110',  # 7 (⠛)
    '110010',  # 8 (⠓)
    '100100'   # 9 (⠊)
]

def display_number(number):
    # Display number sign first (⠼)
    number_sign = '001111'  # ⠼
    ser.write(number_sign.encode())  # Send number sign pattern
    time.sleep(0.5)  # Short delay to distinguish the number sign

    # Display the actual number in Braille
    braille_pattern = braille_numbers[number]
    ser.write(braille_pattern.encode())  # Send the Braille pattern
    print(f"Sent number {number}: {braille_pattern}")

def send_letter(letter):
    if letter in braileMap:
        binary_code = braileMap[letter]
        ser.write(binary_code.encode())
        print(f"Sent {letter}: {binary_code}")
    else:
        print("Invalid letter")

# Example usage: Display the number 3
display_number(3)

# Example usage: Send a letter 'A'
send_letter('B')
