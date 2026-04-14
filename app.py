import gradio as gr
from crew import run_crew, clear_memory

# ── Helpers ────────────────────────────────────────────────────────────────
def chat(message, history):
    """Called by Gradio on each user message."""
    if not message.strip():
        return history, history

    response = run_crew(message)

    history.append((message, response))
    return history, history


def reset(history):
    clear_memory()
    return [], []


# ── UI Layout ──────────────────────────────────────────────────────────────
with gr.Blocks(
    title="AI Startup Idea Generator",
    theme=gr.themes.Soft(primary_hue="indigo"),
) as demo:

    gr.Markdown(
        """
        # AI Startup Idea Generator
        **Powered by CrewAI multi-agent collaboration**
        
        Enter any domain or interest (e.g. *"healthcare"*, *"fintech for Gen Z"*, *"sustainable agriculture"*).  
        Agents will collaborate to generate ideas → research markets → build strategy → create a pitch.
        
        > **Memory enabled** — try follow-ups like *"now make it low-cost"* or *"focus on India market"*.
        """
    )

    chatbot = gr.Chatbot(
        label="Agent Output",
        height=520,
        bubble_full_width=False,
    )

    state = gr.State([])

    with gr.Row():
        msg = gr.Textbox(
            placeholder="e.g. AI tools for small restaurants...",
            label="Your startup domain / idea",
            scale=5,
            lines=1,
        )
        submit_btn = gr.Button("Generate ", variant="primary", scale=1)

    with gr.Row():
        clear_btn = gr.Button("🗑 Clear memory & chat", variant="secondary")

    gr.Examples(
        examples=[
            ["AI-powered tools for small restaurants"],
            ["EdTech startup for rural India using vernacular languages"],
            ["Mental health support app for college students"],
            ["Sustainable fashion using AI and circular economy"],
        ],
        inputs=msg,
        label="Try an example",
    )

    # Events
    submit_btn.click(chat, inputs=[msg, state], outputs=[chatbot, state])
    msg.submit(chat, inputs=[msg, state], outputs=[chatbot, state])
    clear_btn.click(reset, inputs=[state], outputs=[chatbot, state])

if __name__ == "__main__":
    demo.launch(share=True)   # share=True gives a public URL for demo video