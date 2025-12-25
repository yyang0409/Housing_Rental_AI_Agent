import gradio as gr
from ui.contract_ui import build_contract_ui
from ui.qa_ui import build_qa_ui
from agents.rental_agent import RentalAgent
from agents.official_template import OFFICIAL_TEMPLATE

def build_ui():
    agent = RentalAgent(OFFICIAL_TEMPLATE)

    with gr.Blocks() as demo:
        gr.Markdown("# 🏠 租賃 AI Agent")

        with gr.Tabs():
            with gr.Tab("📄 合約分析"):
                build_contract_ui(agent)

            with gr.Tab("💬 法律問答"):
                build_qa_ui(agent)

    return demo
