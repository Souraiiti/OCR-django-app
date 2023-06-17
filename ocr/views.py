import base64

import numpy as np
import pytesseract
from django.contrib import messages
from django.shortcuts import render
from PIL import Image

# you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = (
    r'/usr/bin/tesseract'  # Path to tesseract.exej
)


def homepage(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            # input image
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")
        # lang = request.POST["language"]
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang = "eng")
        # return text to html
        return render(request, "home.html", {"ocr": text, "image": image_base64})
    #
    return render(request, "home.html")
