import os

import gradio as gr

print(gr.__version__)


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def Elegir_paseo(paseo):
    
    return f"Elegiste: {paseo}"

with gr.Blocks() as demo:
    gr.Markdown("Paseos por la Ciudad")

    
    name = gr.Textbox(label="Nombre")
    intensity = gr.Slider(minimum=0, maximum=10, step=1, label="Euforia de saludo")
    btn_greet = gr.Button("Como es un saludo Euforico")
    output = gr.Textbox(label="Saludo Euforico")
    btn_greet.click(fn=greet, inputs=[name, intensity], outputs=output)
    paseo = gr.Radio(choices=["Circo", "Cine", "Teatro"], value="Cine", label="Tipo de Paseo")
    botonPaseo = gr.Button("Eleccion de paseo")
    resultado = gr.Textbox(label="Elegí")
    botonPaseo.click(fn=Elegir_paseo, inputs=[paseo], outputs=resultado)
    

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000)),
        share=True
    )