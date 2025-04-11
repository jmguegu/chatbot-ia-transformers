
from transformers import pipeline

def cargar_modelo(nombre_modelo="distilgpt2"):
    """
    Carga un modelo preentrenado de Hugging Face para generación de texto.
    """
    generador = pipeline("text-generation", model=nombre_modelo)
    return generador

def responder(generador, entrada_usuario):
    """
    Usa el modelo para generar una respuesta a partir del texto ingresado.
    """
    salida = generador(entrada_usuario, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return salida
