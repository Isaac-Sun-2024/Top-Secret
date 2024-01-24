import time
import pyocr
import pyocr.builders
from PIL import Image, ImageGrab
from googletrans import Translator
import pyperclip
import pyautogui
from unidecode import unidecode


# spanish_to_english = {
#     'cero': 'zero',
#     'uno': 'one',
#     'dos': 'two',
#     'tres': 'three',
#     'cuatro': 'four',
#     'cinco': 'five',
#     'seis': 'six',
#     'siete': 'seven',
#     'ocho': 'eight',
#     'nueve': 'nine',
#     'diez': 'ten',
#     'once': 'eleven',
#     'doce': 'twelve',
#     'trece': 'thirteen',
#     'catorce': 'fourteen',
#     'quince': 'fifteen',
#     'dieciseis': 'sixteen',
#     'diecisiete': 'seventeen',
#     'dieciocho': 'eighteen',
#     'diecinueve': 'nineteen',
#     'veinte': 'twenty',
#     'veintiuno': 'twenty-one',
#     'veintidos': 'twenty-two',
#     'veintitres': 'twenty-three',
#     'veinticuatro': 'twenty-four',
#     'veinticinco': 'twenty-five',
#     'veintiseis': 'twenty-six',
#     'veintisiete': 'twenty-seven',
#     'veintiocho': 'twenty-eight',
#     'veintinueve': 'twenty-nine',
#     'treinta': 'thirty',
#     'treinta y uno': 'thirty-one',
#     'treinta y dos': 'thirty-two',
#     'treinta y tres': 'thirty-three',
#     'treinta y cuatro': 'thirty-four',
#     'treinta y cinco': 'thirty-five',
#     'treinta y seis': 'thirty-six',
#     'treinta y siete': 'thirty-seven',
#     'treinta y ocho': 'thirty-eight',
#     'treinta y nueve': 'thirty-nine',
#     'cuarenta': 'forty',
#     'cuarenta y uno': 'forty-one',
#     'cuarenta y dos': 'forty-two',
#     'cuarenta y tres': 'forty-three',
#     'cuarenta y cuatro': 'forty-four',
#     'cuarenta y cinco': 'forty-five',
#     'cuarenta y seis': 'forty-six',
#     'cuarenta y siete': 'forty-seven',
#     'cuarenta y ocho': 'forty-eight',
#     'cuarenta y nueve': 'forty-nine',
#     'cincuenta': 'fifty',
#     'cincuenta y uno': 'fifty-one',
#     'cincuenta y dos': 'fifty-two',
#     'cincuenta y tres': 'fifty-three',
#     'cincuenta y cuatro': 'fifty-four',
#     'cincuenta y cinco': 'fifty-five',
#     'cincuenta y seis': 'fifty-six',
#     'cincuenta y siete': 'fifty-seven',
#     'cincuenta y ocho': 'fifty-eight',
#     'cincuenta y nueve': 'fifty-nine',
#     'sesenta': 'sixty',
#     'sesenta y uno': 'sixty-one',
#     'sesenta y dos': 'sixty-two',
#     'sesenta y tres': 'sixty-three',
#     'sesenta y cuatro': 'sixty-four',
#     'sesenta y cinco': 'sixty-five',
#     'sesenta y seis': 'sixty-six',
#     'sesenta y siete': 'sixty-seven',
#     'sesenta y ocho': 'sixty-eight',
#     'sesenta y nueve': 'sixty-nine',
#     'setenta': 'seventy',
#     'setenta y uno': 'seventy-one',
#     'setenta y dos': 'seventy-two',
#     'setenta y tres': 'seventy-three',
#     'setenta y cuatro': 'seventy-four',
#     'setenta y cinco': 'seventy-five',
#     'setenta y seis': 'seventy-six',
#     'setenta y siete': 'seventy-seven',
#     'setenta y ocho': 'seventy-eight',
#     'setenta y nueve': 'seventy-nine',
#     'ochenta': 'eighty',
#     'ochenta y uno': 'eighty-one',
#     'ochenta y dos': 'eighty-two',
#     'ochenta y tres': 'eighty-three',
#     'ochenta y cuatro': 'eighty-four',
#     'ochenta y cinco': 'eighty-five',
#     'ochenta y seis': 'eighty-six',
#     'ochenta y siete': 'eighty-seven',
#     'ochenta y ocho': 'eighty-eight',
#     'ochenta y nueve': 'eighty-nine',
#     'noventa': 'ninety',
#     'noventa y uno': 'ninety-one',
#     'noventa y dos': 'ninety-two',
#     'noventa y tres': 'ninety-three',
#     'noventa y cuatro': 'ninety-four',
#     'noventa y cinco': 'ninety-five',
#     'noventa y seis': 'ninety-six',
#     'noventa y siete': 'ninety-seven',
#     'noventa y ocho': 'ninety-eight',
#     'noventa y nueve': 'ninety-nine',
#     'cien': 'one hundred'
# }

# new = {
#     'ayer': 'yesterday',
#     'hoy': 'today',
#     'domingo, el domingo': 'sunday',
#     'hace calor': 'it is hot',
#     'hace frio': 'it is cold',
#     'hace sol': 'it is sunny',
#     'hace viento': 'it is windy',
#     'llueve': 'it is raining',
#     'lueve': 'it is raining',
#     'nieva': 'it is snowing',
#     'hoy es': 'today is',
#     'lunes, el lunes': 'monday',
#     'martes, el martes': 'tuesday',
#     'miercoles, el miercoles': 'wednesday',
#     'jueves, el jueves': 'thursday',
#     'viernes, el viernes': 'friday',
#     'sabado, el sabado': 'saturday',
#     'manana': 'tomorrow',
#     'hace buen tiempo': 'it is good weather',
#     'hace mal tiempo': "it's bad weather",
#
# }

new = {
    'delante de': 'in front of',
    'detras de': 'behind',
    'a la derecha de': 'to the right of',
    'encima de': 'on',
    'a la derecha del armario': 'to the right of the wardrobe',
    'a la izquierda de': 'to the left of',
    'al lado de': 'beside',
    'al lado de la cama': 'beside the bed',
    'debajo de': 'under',
    'en las paredes': 'on the walls',
    'entre': 'between',
}

def remove_repeated_letters(input_string):
    result = []  # A list to store the characters of the new string

    i = 0
    while i < len(input_string):
        result.append(input_string[i])  # Add the current character to the result
        while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            i += 1  # Skip repeated characters
        i += 1  # Move to the next character

    return ''.join(result)  # Convert the list back to a string

def remove_stress_marks(input_string):
    return unidecode(input_string)

time.sleep(0.5)
while True:
    # Define the coordinates for the top-left and bottom-right corners
    x1, y1, x2, y2 = (300, 489, 1112, 553)  # Adjust these coordinates as per your requirement

    # Capture the screenshot with high resolution using ImageGrab
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot.png")  # Save the screenshot as an image

    # Open the screenshot
    # screenshot.show()

    # Initialize the OCR tool using Tesseract (or another OCR engine if desired)
    # Make sure to specify the correct OCR tool and language

    tools = pyocr.get_available_tools()
    if len(tools) > 0:
        tool = tools[0]  # Use the first available OCR tool
        lang = 'eng'  # Set the language (e.g., 'eng' for English)

        # Perform OCR on the screenshot image
        extracted_text = tool.image_to_string(
            Image.open("screenshot.png"),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )

    print(extracted_text)

    # Example usage:
    input_string = extracted_text
    result_string = remove_stress_marks(input_string)
    extracted_text = result_string  # Output will be 'veintitres'

    # Example usage:
    input_string = extracted_text
    result_string = remove_repeated_letters(input_string)

    extracted_text = result_string

    text = new[extracted_text]



    if text != 'v':
        pyperclip.copy(text)
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey('enter')
        print(text)
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        time.sleep(0.2)

    else:
        pass


    # else:
    # print("No OCR tools available.")
