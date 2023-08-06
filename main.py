import tkinter as tk
from openaitest import generate_response

class ChatbotWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Persona Chatbot")

        # Create a text box to display chat messages
        self.chat_text = tk.Text(self.root, state=tk.DISABLED)
        self.chat_text.pack(fill=tk.BOTH, expand=True)

        # Create an entry field for user input
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X)
        self.entry.bind("<Return>", self.handle_input)

        # Display an introduction message
        self.intro_message = "Welcome to the AI Persona Chatbot! Ask me anything."
        self.display_message("AI: " + self.intro_message)

        # Initialize context for conversation memory
        self.context = {}

        # Initialize custom context handlers
        self.context_handlers = {
            "favorite_color": self.handle_favorite_color,
            "current_project": self.handle_current_project,
            # We could add more context handlers here according to the needs of the project
        }

    def handle_input(self, event):
        user_input = self.entry.get()
        self.display_message("You: " + user_input)

        # Generate a response using AI and the current conversation context
        response = self.generate_response(user_input)
        self.display_message("AI: " + response)
        self.entry.delete(0, tk.END)

    def display_message(self, message):
        # Enable text box, insert message, disable text box, and scroll to end
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, message + "\n")
        self.chat_text.config(state=tk.DISABLED)
        self.chat_text.see(tk.END)

    def generate_response(self, user_input):
        # Check if a custom context handler can provide a response
        if self.context:
            for key, handler in self.context_handlers.items():
                if key in self.context:
                    response = handler(user_input)
                    if response:
                        return response

        # Default behavior: use AI response with context-aware prompt
        prompt = self.get_prompt(user_input)
        response = generate_response(prompt)
        self.update_context(user_input, response)
        return response

    def get_prompt(self, user_input):
        # Construct a prompt based on the current conversation context
        prompt = user_input

        if self.context:
            context_prompt = "Context: "
            for key, value in self.context.items():
                context_prompt += f"{key}: {value}, "
            prompt = context_prompt + prompt

        return prompt

    def update_context(self, user_input, ai_response):
        # Update context based on user input and AI response
        # Example: Store a topic mentioned in the conversation
        if "topic" in ai_response.lower():
            self.context["current_topic"] = "Artificial Intelligence"

    def handle_favorite_color(self, user_input):
        # Handle queries about the favorite color
        if "favorite color" in user_input.lower():
            return "My favorite color is blue! What's yours?"

    def handle_current_project(self, user_input):
        # Handle queries about the current project
        if "working on" in user_input.lower():
            return "I'm currently working on enhancing my conversation skills!"

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    chatbot_window = ChatbotWindow(root)
    root.mainloop()