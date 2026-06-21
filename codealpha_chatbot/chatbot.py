import tkinter as tk
from tkinter import scrolledtext
import random
import datetime



user_name = ""

greetings = [
    "Hello!",
    "Hi there!",
    "Welcome!",
    "Nice to meet you!"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did Python go to school? To improve its class.",
    "Debugging is like being a detective in your own crime movie."
]



def get_response(user_input):
    global user_name

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return random.choice(greetings)

    elif "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip().title()
        return f"Nice to meet you, {user_name}!"

    elif user_input == "what is my name":
        if user_name:
            return f"Your name is {user_name}"
        return "I don't know your name yet."

    elif user_input == "time":
        return datetime.datetime.now().strftime(
            "Current Time: %H:%M:%S"
        )

    elif user_input == "date":
        return datetime.datetime.now().strftime(
            "Today's Date: %d-%m-%Y"
        )

    elif user_input == "joke":
        return random.choice(jokes)

    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace(
                "calculate",
                ""
            ).strip()

            allowed = "0123456789+-*/(). "

            if all(ch in allowed for ch in expression):
                result = eval(expression)
                return f"Answer = {result}"

            return "Invalid expression."

        except:
            return "Calculation Error."

    elif user_input == "help":
        return (
            "Available Commands:\n\n"
            "• hello / hi / hey\n"
            "• my name is <your name>\n"
            "• what is my name\n"
            "• time\n"
            "• date\n"
            "• joke\n"
            "• calculate 5+10\n"
            "• clear\n"
            "• bye"
        )

    elif user_input in ["bye", "exit"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that. Type 'help'."



def send_message(event=None):

    user_message = entry.get().strip()

    if not user_message:
        return

    chat_area.insert(
        tk.END,
        f"You: {user_message}\n"
    )

    response = get_response(user_message)

    chat_area.insert(
        tk.END,
        f"Bot: {response}\n\n"
    )

    entry.delete(0, tk.END)

    chat_area.see(tk.END)

def clear_chat():

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.insert(
        tk.END,
        "Chat cleared.\n\n"
    )

def show_help():

    help_text = (
        "\n=== HELP MENU ===\n"
        "hello / hi / hey\n"
        "my name is <your name>\n"
        "what is my name\n"
        "time\n"
        "date\n"
        "joke\n"
        "calculate 5+10\n"
        "bye\n\n"
    )

    chat_area.insert(
        tk.END,
        help_text
    )



root = tk.Tk()

root.title("Smart Rule-Based Chatbot")

root.geometry("700x550")



title = tk.Label(
    root,
    text="🤖 Smart Rule-Based Chatbot",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)


chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=22,
    font=("Arial", 11)
)

chat_area.pack(
    padx=10,
    pady=10
)



chat_area.insert(
    tk.END,
    "🤖 Welcome to Smart Chatbot!\n\n"
    "Type 'help' to see available commands.\n\n"
)


input_frame = tk.Frame(root)

input_frame.pack(
    pady=5
)



entry = tk.Entry(
    input_frame,
    width=50,
    font=("Arial", 12)
)

entry.grid(
    row=0,
    column=0,
    padx=5
)

entry.bind(
    "<Return>",
    send_message
)



send_btn = tk.Button(
    input_frame,
    text="Send",
    width=10,
    command=send_message
)

send_btn.grid(
    row=0,
    column=1,
    padx=5
)

# Help Button

help_btn = tk.Button(
    input_frame,
    text="Help",
    width=10,
    command=show_help
)

help_btn.grid(
    row=0,
    column=2,
    padx=5
)



clear_btn = tk.Button(
    input_frame,
    text="Clear",
    width=10,
    command=clear_chat
)

clear_btn.grid(
    row=0,
    column=3,
    padx=5
)



root.mainloop()