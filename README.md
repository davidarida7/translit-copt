# Translit Copt

Translit Copt is an application that allows you to transliterate Coptic text. This application will be very useful for those learning how to read the Coptic language.

When you launch the application, you simply have to allow camera access, and scan the Coptic text that you would like (or alternatively upload an image you already have), and our program will transliterate it and output it for you in the "Transliterated Text" section!

## Tech

This application was developed using a [Bootstrap template frontend](https://startbootstrap.com/theme/freelancer/), Tesseract 4.0.0 for OCR of the Coptic language using Coptic trained data files (available on [Shreeshrii's Github](https://github.com/Shreeshrii/tessdata_coptic)), and a custom implemented Coptic unicode text to transliterated English characters library developed in Python at the 2022 Coptic Hackathon at Queen St. Mary & Prince Tadros Coptic Orthodox Church by Bishoy Kamel, Mark Bassily, Mark Shenouda, Ramz Azmy, and David Arida.

## Installation and Setup
To get the application up and running locally,
1. First ensure you have Python installed. If you don't or, please download and install it from [here](https://www.python.org/downloads/).
2. Download and install Tesseract on your machine by following the instructions noted in this [video](https://www.youtube.com/watch?v=2kWvk4C1pMo), with the following caveats:
    a. The Tesseract exe file location has changed. There is no longer a wiki, as the updated documents are on [this repository](https://github.com/tesseract-ocr/tessdoc), You can find the page that has the exe files directly from this link: [Install Tesseract via pre-built binary package](https://github.com/UB-Mannheim/tesseract/wiki).
    b. In order for Tesseract to work, you also need to set another environment variable, using the command below, where `<location-in-Program-Files-where-you-installed-Tesseract-OCR>` should be replaced with the actual location in Program Files where Tesseract-OCR is installed:
    ```sh
    SET TESSDATA_PREFIX=<location-in-Program-Files-where-you-installed-Tesseract-OCR>/Tesseract-OCR/tessdata
    ```
    c. You must copy the `cop.traineddata` file from [the repository linked above](https://github.com/Shreeshrii/tessdata_coptic) to the same tessdata folder from the previous step, where again `<location-in-Program-Files-where-you-installed-Tesseract-OCR>` should be replaced with the actual location in Program Files where Tesseract-OCR is installed: `<location-in-Program-Files-where-you-installed-Tesseract-OCR>/Tesseract-OCR/tessdata`.
3. You are now ready to setup the Python server, which is responsible for both the UI and the backend, using this command, which should be run in the same directory of this project that has the `index.html` file:
    ```sh
    python3 -m http.server --cgi 8000
    ```
Now the application should be up and running! All you have to do is navigate to http://localhost:8000/index.html, and you will be on the landing page of the UI and can use the application as described above!

## Live Application

A live version of the application is running at [this URL](http://20.83.188.26:8000/index.html).

Please see this zipped file with all the changes that needed to be made to the code for it to run on the server: [translit-copt-main.zip](https://github.com/davidarida7/translit-copt/files/9146254/translit-copt-main.zip).

Here is a screenshot of the application up and running on mobile for a large block of text from the Coptic Bible:

![image](https://user-images.githubusercontent.com/21349126/179889199-793cdc0b-540a-4b70-9212-570a90ec1440.png =585x1266)
