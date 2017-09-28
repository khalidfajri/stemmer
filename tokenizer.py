TEXT = """Kami belajar tanpa lelah.
Kami tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa muda.
Itu karena kami ingin kelak istri dan anak kami bahagia."""

def tokenize(text):
    text = text.lower()
    tokens = text.split(" ")
    return tokens

print(tokenize(TEXT))

# tokenizer = menjadikan kalimat menjadi per kata (contohnya digunakan pada search,pada keywords)