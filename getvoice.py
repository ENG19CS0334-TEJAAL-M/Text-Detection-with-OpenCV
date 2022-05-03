import pytesseract as tess
from gtts import gTTS
import os
tess.pytesseract.tesseract_cmd = r'C:\\Users\\DELL\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
img = Image.open(r'D:\DSU 1\Tej_Projects\TextDetection\img1.png')
text = tess.image_to_string(img)
print(text)
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")