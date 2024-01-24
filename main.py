import time
import pyocr
import pyocr.builders
from PIL import Image, ImageGrab
from googletrans import Translator
import pyperclip
import pyautogui

time.sleep(3)
while True:
    # Define the coordinates for the top-left and bottom-right corners
    x1, y1, x2, y2 = (300, 489, 1112, 553)  # Adjust these coordinates as per your requirement

    # Capture the screenshot with high resolution using ImageGrab
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot.png")  # Save the screenshot as an image

    # Open the screenshot
    #screenshot.show()

    # Initialize the OCR tool using Tesseract (or another OCR engine if desired)
    # Make sure to specify the correct OCR tool and language

    tools = pyocr.get_available_tools()
    if len(tools) > 0:
        tool = tools[0]  # Use the first available OCR tool
        lang = 'eng' # Set the language (e.g., 'eng' for English)

        # Perform OCR on the screenshot image
        extracted_text = tool.image_to_string(
            Image.open("screenshot.png"),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )

    print(extracted_text)
    translator = Translator()
    text = translator.translate(extracted_text, src='es', dest='en')
    time.sleep(0.5)
    print(text.text)
    if 'ty' in text.text:
        if '-' not in text.text:
            if ' ' in text.text:
                text.text = text.text.replace(" ", "-")
                if ' ' in text.text:
                    text.text = text.text.replace(" ", "")

    if ' ' in text.text:
        text.text = text.text.replace(" ","")

    if text.text == 'hundred':
        text.text = '100'
        
    pyperclip.copy(text.text)
    pyautogui.hotkey('command', 'v')
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')

    #else:
        #print("No OCR tools available.")
