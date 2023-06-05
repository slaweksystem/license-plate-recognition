import numpy as np
import gradio as gr
from Detector import Detector

detector = Detector()

demo = gr.Interface(
    detector.detect, 
    gr.Image(), 
    [
        "image", 
        gr.Textbox(lines=4, label="License plates", placeholder="License plates")
    ],
    css= ".gradio-container {background-color: grey}"
    )

demo.launch()



