import tkinter as tk
from chatbot import AskBot


# Create the AskBot object
bot = AskBot()


# Clear the conversation
def clear_chat():
    chat_display.config(state="normal")
    chat_display.delete("1.0", tk.END)

    # Add the welcome message back
    chat_display.insert(tk.END, "AskBot: ", "bot")
    chat_display.insert(
        tk.END,
        "Hello! I am AskBot. You can ask me about people, concepts, or definitions.\n\n"
    )

    chat_display.config(state="disabled")


# Process a user message
def send_message():
    user_input = input_box.get()

    # Ignore empty messages
    if not user_input.strip():
        return

    # Determine what the user is asking
    intent = bot.detect_intent(user_input)

    if intent == "greeting":
        bot_response = (
            "Hello! I am AskBot. You can ask me about people, concepts, "
            "or ask for definitions."
        )

    elif intent == "thank_you":
        bot_response = "You're welcome! Any other questions?"

    elif intent == "define":
        topic = user_input[7:].strip()
        bot_response = bot.get_wikipedia_summary(topic)

    elif intent == "who_is":
        topic = user_input[7:].strip()
        bot_response = bot.get_wikipedia_summary(topic)

    elif intent == "what_is":
        topic = user_input[8:].strip()
        bot_response = bot.get_wikipedia_summary(topic)

    elif intent == "tell_me_about":
        topic = user_input[15:].strip()
        bot_response = bot.get_wikipedia_summary(topic)

    elif intent == "exit":
        bot_response = "Goodbye! Have a great day."

        # Display the goodbye conversation
        chat_display.config(state="normal")

        chat_display.insert(tk.END, "You: ", "user")
        chat_display.insert(tk.END, user_input + "\n\n")

        chat_display.insert(tk.END, "AskBot: ", "bot")
        chat_display.insert(tk.END, bot_response + "\n\n")

        chat_display.config(state="disabled")
        chat_display.see(tk.END)

        # Close the window after one second
        window.after(2000, window.destroy)
        return

    else:
        bot_response = (
            "I'm not sure how to help with that. Try asking me to define "
            "something or ask 'who is' followed by a name."
        )

    # Display the conversation
    chat_display.config(state="normal")

    chat_display.insert(tk.END, "You: ", "user")
    chat_display.insert(tk.END, user_input + "\n\n")

    chat_display.insert(tk.END, "AskBot: ", "bot")
    chat_display.insert(tk.END, bot_response + "\n\n")

    # Scroll to the newest message
    chat_display.see(tk.END)

    chat_display.config(state="disabled")

    # Clear the input box
    input_box.delete(0, tk.END)


# Create the main window

window = tk.Tk()
window.title("AskBot")
window.geometry("700x600")
window.minsize(500, 400)

# Create the title
title_label = tk.Label(
    window,
    text="AskBot",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=(15, 2))

subtitle_label = tk.Label(
    window,
    text="Your personal Wikipedia assistant",
    font=("Arial", 11)
)
subtitle_label.pack(pady=(0, 10))

# Create the chat area
chat_frame = tk.Frame(window)
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

chat_display = tk.Text(
    chat_frame,
    height=20,
    width=70,
    state="disabled",
    font=("Arial", 12),
    wrap=tk.WORD,
    padx=10,
    pady=10
)


# Add the scrollbar
scrollbar = tk.Scrollbar(
    chat_frame,
    command=chat_display.yview
)

chat_display.config(yscrollcommand=scrollbar.set)

chat_display.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# Format user and AskBot labels
chat_display.tag_configure(
    "user",
    font=("Arial", 14, "bold")
)

chat_display.tag_configure(
    "bot",
    font=("Arial", 14, "bold")
)


# Add the welcome message
chat_display.config(state="normal")

chat_display.insert(
    tk.END,
    "AskBot: ",
    "bot"
)

chat_display.insert(
    tk.END,
    "Hello! I am AskBot. You can ask me about people, concepts, "
    "or definitions.\n\n"
)

chat_display.config(state="disabled")


# Create the input area
input_frame = tk.Frame(window)
input_frame.pack(fill=tk.X, padx=10, pady=5)

input_box = tk.Entry(
    input_frame,
    font=("Arial", 12)
)
input_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=5,
    ipady=6
)


# Create the Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5
)
send_button.pack(
    side=tk.RIGHT,
    padx=5
)


# Create the Clear Chat button
clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear_chat,
    font=("Arial", 10),
    padx=10,
    pady=3
)
clear_button.pack(pady=5)


# Allow Enter to send a message
input_box.bind(
    "<Return>",
    lambda event: send_message()
)

# Automatically focus the input box
window.after(100, input_box.focus_set)

# Start the GUI
window.mainloop()
