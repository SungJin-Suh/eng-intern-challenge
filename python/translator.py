import sys

char_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..'
}

def text_to_braille(text: str) -> str:
    result = ""
    is_number = False
    
    for char in text:
        if char.isdigit():
            if not is_number:
                result += ".O.OOO"
                is_number = True
            result += char_to_braille_map[char]
        else:
            if is_number:
                is_number = False
            if char.isupper():
                result += ".....O"
                char = char.lower()
            result += char_to_braille_map.get(char, "")
    
    return result


def braille_to_text(braille: str) -> str:
    braille_to_char_map = {v: k for k, v in char_to_braille_map.items()}
    
    result = ""
    i = 0
    
    while i < len(braille):
        chunk = braille[i:i + 6]
        if chunk == ".O.OOO":
            i += 6
            continue
        elif chunk == ".....O":
            i += 6 
            chunk = braille[i:i + 6]
            result += braille_to_char_map.get(chunk, "").upper()
        else:
            result += braille_to_char_map.get(chunk, "")
        i += 6
    
    return result


if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    if all(char in 'O.' for char in user_input):
        print(braille_to_text(user_input))
    else:
        print(text_to_braille(user_input))
