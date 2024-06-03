from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import pickle
from .utils import read_pdf, preprocess_text

# Load the models
model_path = os.path.join('static', 'vectorizer.pkl')
with open(model_path, 'rb') as file:
    vectorizer = pickle.load(file)

model_path = os.path.join('static', 'kmeans_model.pkl')
with open(model_path, 'rb') as file:
    kmeans = pickle.load(file)

def index(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()

        # Guardar el archivo con el nombre original
        filename = fs.save(pdf_file.name, pdf_file)
        file_url = fs.url(filename)
        file_path = fs.path(filename)
        file_name = os.path.basename(filename)

        # Procesar el archivo PDF y evaluar con el modelo
        evaluation_result = process_and_evaluate_pdf(file_path)

        return render(request, 'index.html', {
            'file_url': file_url,
            'file_name': file_name,
            'evaluation_result': evaluation_result
        })
    return render(request, 'index.html')

def process_and_evaluate_pdf(file_path):
    # Leer y preprocesar el documento PDF
    text = read_pdf(file_path)
    preprocessed_text = preprocess_text(text)

    # Convertir el documento de prueba en una representación TF-IDF
    vector = vectorizer.transform([preprocessed_text]).toarray()

    # Asignar el documento de prueba a un cluster usando el modelo entrenado
    cluster = kmeans.predict(vector)[0]
    return cluster
