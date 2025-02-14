import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window
root = tk.Tk()
root.title("!ntelli_Search!")
root.geometry("420x580")  # Adjusted height for extra buttons
root.configure(bg="#121212")  # Dark theme


# Function to handle all searches
def search(platform):
    query = entry.get().strip()
    if not query:
        return  # Prevent empty searches

    urls = {
        "YouTube": f"https://www.youtube.com/results?search_query={query}",
        "Google": f"https://www.google.com/search?q={query}",
        "Instagram": f"https://www.instagram.com/{query.replace('@', '')}",
        "Twitter": f"https://twitter.com/search?q={query}&src=typed_query",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={query}",
        "ChatGPT": f"https://chat.openai.com/?q={query}",
        "Gemini": f"https://gemini.google.com/app?q={query}"
    }

    webbrowser.open(urls[platform])


# Title Label - Bigger and Bolder
Label(root, text="!ntelli_Search!", font=("Arial", 22, "bold"), fg="white", bg="#121212").pack(pady=15)

# Capsule-shaped search bar
entry_frame = tk.Frame(root, bg="#333", bd=0, relief="solid")
entry_frame.pack(pady=10, padx=20)

entry = Entry(entry_frame, width=38, font=("Arial", 13), bg="#333", fg="white", insertbackground="white",
              relief="flat", highlightthickness=0)
entry.pack(ipady=10, padx=15, pady=5)

# Making the search bar fully capsule-shaped
entry_frame.configure(width=350, height=45)
entry_frame.config(highlightbackground="white", highlightcolor="white")
entry_frame.pack_propagate(False)

# Apply rounded corners using a canvas
canvas = tk.Canvas(entry_frame, width=350, height=45, bg="#121212", bd=0, highlightthickness=0)
canvas.pack()
canvas.create_oval(0, 0, 45, 45, fill="#333", outline="#333")  # Left curve
canvas.create_oval(305, 0, 350, 45, fill="#333", outline="#333")  # Right curve
canvas.create_rectangle(22, 0, 328, 45, fill="#333", outline="#333")  # Center rectangle

entry_frame.lift(entry)  # Lift the entry above the canvas

# Button style (fully rounded with hover effects)
btn_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#1E88E5", "fg": "white",
    "activebackground": "#1565C0", "activeforeground": "white",
    "bd": 0, "relief": "flat", "highlightthickness": 0,
    "width": 20, "height": 2
}


def on_enter(e):
    e.widget.config(bg="#1565C0")


def on_leave(e):
    e.widget.config(bg="#1E88E5")


# Function to create fully rounded buttons
def create_rounded_button(text, command):
    btn = Button(root, text=text, command=command, **btn_style)
    btn.pack(pady=6, padx=20, ipadx=10, ipady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    # Making the button fully rounded
    btn.config(borderwidth=0, highlightthickness=0)
    btn.configure(width=20, height=2)
    return btn


# Create rounded buttons
platforms = ["YouTube", "Google", "Instagram", "Twitter", "LinkedIn", "ChatGPT", "Gemini"]
for platform in platforms:
    create_rounded_button(f"Search on {platform}", lambda p=platform: search(p))

# Run the GUI event loop
root.mainloop()
