import gradio as gr
from chat_utils import cargar_modelo, responder

modelo = cargar_modelo()

iface = gr.Interface(
    fn=lambda texto: responder(modelo, texto),
    inputs=gr.Textbox(lines=2, placeholder="Escribe algo..."),
    outputs="text",
    title="🤖 Chatbot con IA",
    description="Chatbot básico usando Transformers + Gradio"
)

if __name__ == "__main__":
    iface.launch()

