import ollama

SYSTEM_PROMPT = """
You are an AI/ML assistant for a robotics engineering student.
Give clear, accurate, concise answers.
Explain technical concepts with simple examples when useful.
"""

def ask_ollama(prompt):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response["message"]["content"]

prompts = [
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is a neural network?",
    "What is computer vision?",
    "What is robotics?",
]

if __name__ == "__main__":
    output_file = "notebooks/W7D4/W7D4_output.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        for i, prompt in enumerate(prompts, start=1):
            output = f"\n--- Prompt {i} ---\n"
            output += f"Question: {prompt}\n"

            answer = ask_ollama(prompt)

            output += "Answer:\n"
            output += answer + "\n"

            print(output)
            file.write(output)

    print(f"\nOutput saved to: {output_file}")
