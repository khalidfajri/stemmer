import re

TEXT = """Kami belajar tanpa lelah.
Kami& tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa#muda.
Itu karena kami ingin kelak istri dan anak kami bahagia."""

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 -]', ' ', text, flags = re.IGNORECASE|re.MULTILINE) # fungsinya mengubah selain karakter tsb menjadi spasi
    text = re.sub(r'( +)', ' ', text, flags = re.IGNORECASE|re.MULTILINE) # fungsinya jika ada lebih dari 1 spasi, maka dijadikan satu
    tokens = text.split(" ")
    return tokens

print(tokenize(TEXT))

# tokenizer = menjadikan kalimat menjadi per kata (contohnya digunakan pada search,pada keywords)