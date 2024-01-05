# Image OCR Flask

This application is a web application that uploads images with Flask and recognizes Japanese text in the images with OCR.

## Requirement

- Python
  - flask
  - Pillow
  - pytesseract
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
  - [jpn.traineddata](https://github.com/tesseract-ocr/tessdata)

## Usage

1. Create the uploads directory by the following command.

```
mkdir uploads
```

2. Run the application.

```bash
python app.py
```

3. Access the application in your browser at http://127.0.0.1:5000.
4. Select an image file and press the Upload button.

## Note

- The path to Tesseract in app.py must be changed to the path installed on your PC.
- If you change the recognized language, the language configuration in app.py will also need to be replaced with the language you will use.
