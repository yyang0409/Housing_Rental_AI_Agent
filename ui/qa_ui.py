import gradio as gr

CATEGORIES = [
    "契約基本與雙方身分",
    "標的物與租期約定",
    "金錢與費用相關",
    "使用限制與修繕維護",
    "租約終止與返還",
    "爭議處理與雙方義務"
]

def build_qa_ui(agent):
    with gr.Blocks() as qa_ui:
        gr.Markdown("## 💬 租屋法律問答")

        category = gr.Dropdown(
            choices=CATEGORIES,
            label="選擇主題"
        )

        question = gr.Textbox(label="你的問題")
        answer = gr.Textbox(lines=15)

        gr.Button("送出問題").click(
            agent.answer_question,
            inputs=[question, category],
            outputs=answer
        )

    return qa_ui
