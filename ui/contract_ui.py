import gradio as gr
from services.pdf_service import PDFService

def build_contract_ui(agent):
    with gr.Blocks() as contract_ui:
        gr.Markdown("## 📄 租賃合約 PDF 分析")

        pdf = gr.File(type="filepath", label="上傳租賃合約 PDF")
        output = gr.Textbox(lines=20)

        gr.Button("分析合約").click(
            lambda f: agent.analyze_contract(PDFService.extract_text(f)),
            inputs=pdf,
            outputs=output
        )

    return contract_ui
