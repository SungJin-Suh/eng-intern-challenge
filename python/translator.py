import sys

def text_to_braille(text: str) -> str:
    """
    Converts a given text string to its corresponding Braille representation.

    This function translates each character in the input text to its corresponding Braille pattern.
    It handles digits by prefixing them with a Braille number indicator and converts uppercase letters
    to lowercase, prefixing them with a Braille capital letter indicator.

    :param text: the input text string to be converted to Braille representation
    :precondition: text is a string containing only alphanumeric characters and punctuation
    :postcondition: the input text is converted to its Braille representation
    :return: the Braille representation of the input text

    >>> text = "Hello world"
    >>> text_to_braille(text)
    '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
    """
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
    """
    Converts a given Braille string to its corresponding text representation.

    This function translates each Braille pattern in the input string to its corresponding text character.
    It handles Braille number indicators by skipping them and converts Braille capital letter indicators
    to uppercase letters in the resulting text.

    :param braille: the input Braille string to be converted to text representation
    :precondition: braille is a string containing only O and . characters
    :postcondition: the input Braille string is converted to its text representation
    :return: the text representation of the input Braille string

    >>> braille = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.."
    >>> braille_to_text(braille)
    'Abc 234'
    """
    braille_to_char_map = {
        'O.....': ['1', 'a'], 'O.O...': ['2', 'b'], 'OO....': ['3', 'c'], 
        'OO.O..': ['4', 'd'], 'O..O..': ['5', 'e'], 'OOO...': ['6', 'f'], 
        'OOOO..': ['7', 'g'], 'O.OO..': ['8', 'h'], '.OO...': ['9', 'i'], 
        '.OOO..': ['0', 'j'], 'O...O.': 'k', 'O.O.O.': 'l', 
        'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': '>', 
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', 
        '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 
        'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
        'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ', 
        '..OO.O': '.', '..O...': ',', '..O.OO': '?', 
        '..OOO.': '!', '..OO..': ':', '..O.O.': ';', 
        '....OO': '-', '.O..O.': '/', '.OO..O': '<', 
        'O.O..O': '(', '.O.OO.': ')'
    }
    
    result = ""
    index = 0
    number_mode = False
    
    while index < len(braille):
        braille_chunk = braille[index:index + 6]
        
        if braille_chunk == ".O.OOO":
            index += 6
            number_mode = True
            continue
        elif braille_chunk == ".....O":
            index += 6
            braille_chunk = braille[index:index + 6]
            if isinstance(braille_to_char_map.get(braille_chunk, ""), list):
                result += braille_to_char_map.get(braille_chunk, "")[1].upper()
            else:
                result += braille_to_char_map.get(braille_chunk, "").upper()
            number_mode = False
        else:
            if isinstance(braille_to_char_map.get(braille_chunk, ""), list):
                if number_mode:
                    result += braille_to_char_map.get(braille_chunk, "")[0]
                else:
                    result += braille_to_char_map.get(braille_chunk, "")[1]
            else:
                result += braille_to_char_map.get(braille_chunk, "")
        
        index += 6
    
    return result

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    if all(char in 'O.' for char in user_input):
        print(braille_to_text(user_input))
    else:
        print(text_to_braille(user_input))
