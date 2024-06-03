import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def read_pdf(file_path):
    # Abrir el archivo PDF
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        # Extraer texto de cada página
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def preprocess_text(text):
    # Eliminar caracteres especiales y números
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', ' ', text)
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Eliminar stop words
    stop_words = set(stopwords.words('spanish'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    # Lemmatización
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)

