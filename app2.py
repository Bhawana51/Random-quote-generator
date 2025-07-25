import tkinter as tk
import random

QUOTES = [
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Code is like humor. When you have to explain it, it’s bad.", "Cory House"),
    ("Programs must be written for people to read.", "Harold Abelson"),
]

def new_quote():
    quote, author = random.choice(QUOTES)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

root = tk.Tk()
root.title("Random Quote Generator")

quote_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, justify="center")
quote_label.pack(pady=20)

author_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"))
author_label.pack()

tk.Button(root, text="New Quote", command=new_quote).pack(pady=10)

new_quote()
root.mainloop()
