import gradio as gr
from crewai import Crew
from tasks import research_task, old_research_task, analysis_task

# Mapping of tasks
task_map = {
    "USA Retail Property Investment Report": (research_task, analysis_task),
    "Germany Investment Cities (Old Task)": (old_research_task,),
    "Summarize Property Info": (analysis_task,)
}

def run_tasks(task_option):
    selected_tasks = task_map[task_option]
    try:
        agents = list(set(task.agent for task in selected_tasks))  # Unique agents
        crew = Crew(
            agents=agents,
            tasks=selected_tasks,
            verbose=True,
        )
        result = crew.kickoff()

        output_text = f"✅ Task completed successfully!\n\n📝 Agent Output:\n{result}"


        # Collect optional file outputs
        file_outputs = []
        for task in selected_tasks:
            if hasattr(task, "output_file") and task.output_file:
                try:
                    with open(task.output_file, "r", encoding="utf-8") as file:
                        content = file.read()
                    file_outputs.append(f"Output from {task.output_file}:\n{content}")
                except FileNotFoundError:
                    file_outputs.append(f"File {task.output_file} not found.")
        file_output_text = "\n\n".join(file_outputs) if file_outputs else ""

        return output_text, file_output_text
    except Exception as e:
        return f"❌ An error occurred: {e}", ""

# Gradio UI components
with gr.Blocks() as demo:
    gr.Markdown(
        "<h1 style='text-align:center; color:#4A6EE0;'>🏢 Retail Property Investment AI Assistant</h1>"
        "<p style='text-align:center; font-size:18px;'>Use AI agents to generate property investment insights, analysis reports, and recommendations.</p>"
        "<hr style='border-top: 2px solid #4A6EE0;' />"
    )

    task_option = gr.Radio(
        label="📋 Select a task to run:",
        choices=list(task_map.keys()),
        value="USA Retail Property Investment Report"
    )

    run_button = gr.Button("🚀 Run Task(s)")

    output_result = gr.Textbox(label="📝 Agent Output", lines=20, interactive=False)
    output_files = gr.Textbox(label="📁 Optional File Outputs", lines=10, interactive=False)

    run_button.click(fn=run_tasks, inputs=task_option, outputs=[output_result, output_files])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8501)


