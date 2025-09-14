FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


def caesarShift(message, shift):
    result = ""
    for char in message.upper():
        if char.isalpha():
            charCode = ord(char)
            newCharCode = charCode + shift

            if newCharCode > LAST_CHAR_CODE:
                newCharCode -= CHAR_RANGE

            if newCharCode < FIRST_CHAR_CODE:
                newCharCode += CHAR_RANGE

            newChar = chr(newCharCode)
            result += newChar
        else:
            result += char

    print(result)


userMessage = input("Message to encrypt: ")
userShift = int(input("Shift: "))

caesarShift(userMessage, userShift)
