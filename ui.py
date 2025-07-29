import gradio as gr
from dotenv import load_dotenv
from mychatbot import ai_chatbot  # Import the ai_chatbot function from mychat
import json
import os

with open(os.path.join(os.path.dirname(__file__), 'branding.json')) as f:

    brand_info=json.load(f)['brand']
with gr.Blocks(title=brand_info["organizationName"]) as demo:
    gr.HTML(f'''<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="{brand_info['logo']['title']}" alt="{brand_info['organizationName']}" />
            </div>''')
    gr.ChatInterface(
        fn=ai_chatbot,
        title=brand_info["organizationName"],
        description=brand_info["slogan"],
        type="messages",
        examples=["What is AI?", 
                  "How does machine learning work?", 
                  "Can you explain neural networks?",
                  "What is natural language processing?",
                  "How do I get started with AI?"],
    )

if __name__ == "__main__":
    demo.launch()