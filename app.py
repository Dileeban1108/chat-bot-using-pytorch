import tkinter as tk
from tkinter import scrolledtext
from chat import get_response, bot_name

# === COLORS AND FONTS ===
BG_COLOR = "#1e1e1e"      # Deep dark background
USER_COLOR = "#343541"    # Slightly lighter for user messages
BOT_COLOR = "#444654"     # Slightly darker for bot messages
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#10a37f"  # ChatGPT green
FONT = ("Helvetica", 12)
FONT_BOLD = ("Helvetica", 12, "bold")


class ChatApplication:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ChatGPT Style Bot - Dilu")
        self.window.configure(bg=BG_COLOR)
        self.window.geometry("600x700")

        # === CHAT DISPLAY AREA ===
        self.chat_area = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT,
            insertbackground=TEXT_COLOR,
            padx=15,
            pady=15,
            borderwidth=0,
            relief="flat"
        )
        self.chat_area.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

        # === ENTRY AREA ===
        self.entry_frame = tk.Frame(self.window, bg=BG_COLOR)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=(5, 10))

        self.msg_entry = tk.Entry(
            self.entry_frame,
            bg="#40414f",
            fg=TEXT_COLOR,
            font=FONT,
            insertbackground=TEXT_COLOR,
            relief="flat"
        )
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 10))
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        self.msg_entry.focus()

        self.send_button = tk.Button(
            self.entry_frame,
            text="➤",
            bg=ACCENT_COLOR,
            fg="white",
            font=FONT_BOLD,
            relief="flat",
            activebackground="#15c590",
            activeforeground="white",
            command=lambda: self._on_enter_pressed(None)
        )
        self.send_button.pack(side=tk.RIGHT, ipadx=10, ipady=5)

        # Add welcome text
        self._insert_message(f"Hello! I’m {bot_name}. How can I help you today?", bot_name)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get().strip()
        if msg:
            self._insert_message(msg, "You")
            self.msg_entry.delete(0, tk.END)

    def _insert_message(self, msg, sender):
        self.chat_area.configure(state=tk.NORMAL)

        if sender == "You":
            # USER MESSAGE
            self.chat_area.insert(tk.END, f"You: {msg}\n", "user")
            response = get_response(msg)
            self.chat_area.insert(tk.END, f"{bot_name}: {response}\n\n", "bot")
        else:
            # INITIAL BOT MESSAGE
            self.chat_area.insert(tk.END, f"{sender}: {msg}\n\n", "bot")

        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

        # Apply tags for style
        self.chat_area.tag_config("user", foreground="#10a37f", spacing1=5, lmargin1=10)
        self.chat_area.tag_config("bot", foreground="#ffffff", spacing1=10, lmargin1=10, rmargin=10)


if __name__ == "__main__":
    app = ChatApplication()
    app.window.mainloop()
