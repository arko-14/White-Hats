import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('COM9', 9600)  # Replace 'COM3' with your Arduino port
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
braille_numbers = {
    '0':'100110',  # 0 (⠚)
    '1':'100000',  # 1 (⠁)
    '2':'110000',  # 2 (⠃)
    '3':'100100',  # 3 (⠉)
    '4':'100110',  # 4 (⠙)
    '5':'100010',  # 5 (⠑)
    '6':'110100',  # 6 (⠋)
    '7':'110110',  # 7 (⠛)
    '8':'110010',  # 8 (⠓)
    '9':'100100'   # 9 (⠊)
}


#to decide whether the character coming is letter or number

if braileMap:
    def send_letter(letter):
        if  letter in braileMap:
            binary_code = braileMap[letter]
            ser.write(binary_code.encode())
            print(f"Sent {letter}: {binary_code}")

        else:
            print("Invalid letter")    
        
#time.sleep(0.5)


    def send_number(numbers):
        if numbers in braille_numbers:
            number_sign = '001111'  
            ser.write(number_sign.encode())  # Send number sign pattern
            print(number_sign)
            time.sleep(1)
            binary_number = braille_numbers[numbers]
            ser.write(binary_number.encode())
            print(f"Sent { numbers }:{ binary_number }")

        
        else:
            print("Invalid number")





B = input('input letter or integer = ')
if B.isalpha():
    send_letter(B)
else:
    time.sleep(0.5)
    send_number(B)

#send_letter(B)
#time.sleep(0.5)
#send_number('0')



   







