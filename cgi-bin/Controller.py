#!/usr/bin/python

import cgi, cgitb
cgitb.enable()  # for troubleshooting

import os
import sys
import base64

#the cgi library gets vars from html
data = cgi.FieldStorage()
print("Status: 200")
print("Content-Type: text/html;charset=utf-8\n")

def getPronunciation(c):
    if (c == "Ⲁ"):
        return "a"
    elif (c == "Ⲉ"):
        return "e"
    elif (c == "Ⲍ"):
        return "z"
    elif (c == "Ⲏ"):
        return "ee"
    elif (c == "Ⲑ"):
        return "th"
    elif (c == "Ⲕ"):
        return "k"
    elif (c == "Ⲗ"):
        return "l"
    elif (c == "Ⲙ"):
        return "m"
    elif (c == "Ⲛ"):
        return "n"
    elif (c == "Ⲝ"):
        return "x"
    elif (c == "Ⲟ"):
        return "o"
    elif (c == "Ⲡ"):
        return "p"
    elif (c == "Ⲣ"):
        return "r"
    elif (c == "Ⲧ"):
        return "t"
    elif (c == "Ⲫ"):
        return "f"
    elif (c == "Ⲯ"):
        return "ps" 
    elif (c == "Ⲱ"):
        return "o"
    elif (c == "Ϣ"):
        return "sh"
    elif (c == "Ϥ"):
        return "f"
    elif (c == "Ϧ"):
        return "kh"
    elif (c == "Ϩ"):
        return "h"
    elif (c == "Ϭ"):
        return "ch"
    elif (c == "Ϯ"):
        return "tee"
    elif (c == "Ⲇ"):
        return "d"
    elif (c == "Ⲓ"):
        return "i"
    elif (c == "Ⲥ"):
        return "c"
    return c;   

def getPronunciationSpecial(c, cNext,cPrev):
    if (c == "Ⲃ"):
        if (cNext == "Ⲁ" or cNext == "Ⲉ" or cNext == "Ⲏ" or cNext == "Ⲓ" or cNext == "Ⲟ"or cNext == "Ⲩ"or cNext == "Ⲱ"):
            return "v"
        else:
            return "b"
    elif (c == "Ⲅ"):
        if (cNext == "Ⲉ" or cNext == "Ⲓ" or cNext == "Ⲏ"or cNext == "Ⲩ"):
            return "g"
        if (cNext == "Ⲅ"or cNext == "Ⲕ"or cNext == "Ⲝ"or cNext == "Ⲭ"):
            return "ng"
        else:
            return "gh"
    elif (c == "Ⲩ"):
        if (cPrev == "Ⲁ" or cPrev == "Ⲉ"):
            return "v"
        if (cPrev == "Ⲟ"):
            return "u"
        else:
            return "e"
    elif (c == "Ⲭ"):
        if (cNext == "Ⲉ" or cNext == "Ⲓ" or cNext == "Ⲏ" or cNext == "Ⲩ"):
            return "sh"
        else:
            return "kh"
    elif (c == "Ϫ"):
        if (cNext == "Ⲉ" or cNext == "Ⲓ" or cNext == "Ⲏ" or cNext == "Ⲩ"):
            return "j"
        else:
            return "g"
    elif (c == "̀"):
        if (cNext == "Ⲁ" or cNext == "Ⲉ" or cNext == "Ⲏ" or cNext == "Ⲓ" or cNext == "Ⲟ"or cNext == "Ⲩ"or cNext == "Ⲱ"):
            return ""
        else:
            return "e"
    return c

def hasRules(c):
    if (c == "Ⲃ"):
        return 1
    elif (c == "Ⲅ"):
        return 1
    elif (c == "Ⲩ"):
        return 1
    elif (c == "Ⲭ"):
        return 1
    elif (c == "Ϫ"):
        return 1
    elif (c == "̀"):
        return 1
    return 0

def convert_ocr_to_text(output):
    cmd = "tesseract imageToSave.png " + output + " -l cop"
    os.system(cmd)

img_data_string = data["param"].value.replace("data:image/png;base64,", "")
img_data = base64.b64decode(img_data_string)
fh = open("imageToSave.png", "wb")
fh.write(img_data)
fh.close()

convert_ocr_to_text("out")
f = open("out.txt", encoding="utf8")
tempBuffer = f.read()

buffer = tempBuffer.upper()
transliterate = ""
for i in range(len(buffer)):
    if hasRules(buffer[i]):
        before = "" if (i == 0) else buffer[i-1]
        after = "" if (i == len(buffer) - 1) else buffer[i+1]
        transliterate = transliterate + getPronunciationSpecial(buffer[i],after,before)
    else:
        transliterate = transliterate + getPronunciation(buffer[i]) 
        
print(transliterate)
