import numpy as np
import gradio as gr

def process_image(input_img):
    return input_img, "text\ntext2\ntext3"

demo = gr.Interface(
    process_image, 
    gr.Image(), 
    [
        "image", 
        gr.Textbox(lines=4, label="License plates", placeholder="License plates")
    ],
    css= ".gradio-container {background-color: grey}"


    )

demo.launch()



