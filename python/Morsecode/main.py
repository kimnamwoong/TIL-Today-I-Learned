def get_morse_code():
    morse_code = {'A':'・－',
              'B':'－・・・',
              'C':'－・－・',
              'D':'－・・',
              'E':'・',
              'F':'・・－・',
              'G':'－－・',
              'H':'・・・・',
              'I':'・・',
              'J':'・－－－',
              'K':'－・－',
              'L':'・－・・',
              'M':'－－',
              'N':'－・',
              'O':'－－－',
              'P':'・－－・',
              'Q':'－－・－',
              'R':'・－・',
              'S':'・・・',
              'T':'－',
              'U':'・・－',
              'V':'・・・－',
              'W':'・－－',
              'X':'－・・－',
              'Y':'－・－－',
              'Z':'－－・・'}
    return morse_code


def clean_sentence(sentence):
    temp = sentence
    full_stop = [',','.','!','?']
    for stop in full_stop:
        temp = temp.replace(stop,'')

    return temp.replace(" ","")


def convert_lowercase(sentence):
    res = ""
    for char in sentence:
        if char.islower():
            char = char.upper()
        res += char

    return res


print('Hello This is Morse Code Program')
while True:
    user_input = input('Enter your sentences (H - help ,E - Exit)')
    morse_code = get_morse_code()
    if user_input.upper() == 'H':
        print(morse_code)
    elif user_input.upper() == 'E':
        break
    else:
        cleaned_sentence = clean_sentence(user_input)
        convert_sentence = convert_lowercase(cleaned_sentence)
        print(convert_sentence)
        for char in convert_sentence:
            print(morse_code[char])


