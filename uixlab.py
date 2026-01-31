import tkinter as tk
from tkinter import ttk

DARK_BG = "#f7fcf6"
LIGHT_BG = "#b31515"
ACCENT = "#19b4b4"
TEXT_DARK = "white"
TEXT_LIGHT = "black"

current_theme = "dark"

# ---------------- MAIN APP ----------------
root = tk.Tk()
root.title("UIXLab")
root.geometry("800x500")
root.config(bg=DARK_BG)

sidebar = tk.Frame(root, width=200, bg="black")
sidebar.pack(side="left", fill="y")

content = tk.Frame(root, bg=DARK_BG)
content.pack(side="right", fill="both", expand=True)

# ---------------- HELPERS ----------------
def clear_content():
    for w in content.winfo_children():
        w.destroy()

def apply_theme():
    bg = DARK_BG if current_theme == "dark" else LIGHT_BG
    fg = TEXT_DARK if current_theme == "dark" else TEXT_LIGHT
    root.config(bg=bg)
    content.config(bg=bg)

    for w in content.winfo_children():
        try:
            w.config(bg=bg, fg=fg)
        except:
            pass

# ---------------- BUTTONS DEMO ----------------
def buttons_demo():
    clear_content()
    apply_theme()

    tk.Label(
        content,
        text="Buttons Showcase",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    tk.Button(content, text="Primary", bg=ACCENT, fg="black", width=15).pack(pady=5)
    tk.Button(content, text="Secondary", bg="gray", fg="white", width=15).pack(pady=5)
    tk.Button(content, text="Danger", bg="red", fg="white", width=15).pack(pady=5)

# ---------------- TOGGLE SWITCH ----------------
def toggle_demo():
    clear_content()
    apply_theme()

    state = tk.BooleanVar()

    def update():
        status.config(text="ON" if state.get() else "OFF")

    tk.Label(content, text="Toggle Switch", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Checkbutton(
        content,
        text="Enable Feature",
        variable=state,
        command=update
    ).pack(pady=10)

    status = tk.Label(content, text="OFF", font=("Arial", 14))
    status.pack()

# ---------------- SLIDER DEMO ----------------
def slider_demo():
    clear_content()
    apply_theme()

    tk.Label(content, text="Slider Component", font=("Arial", 18, "bold")).pack(pady=10)

    value_label = tk.Label(content, text="Value: 50", font=("Arial", 14))
    value_label.pack(pady=5)

    def update(val):
        value_label.config(text=f"Value: {val}")

    tk.Scale(
        content,
        from_=0,
        to=100,
        orient="horizontal",
        command=update
    ).pack(pady=10)

# ---------------- PROGRESS BAR ----------------
def progress_demo():
    clear_content()
    apply_theme()

    tk.Label(content, text="Progress Bar", font=("Arial", 18, "bold")).pack(pady=10)

    bar = ttk.Progressbar(content, length=300)
    bar.pack(pady=10)

    def start():
        bar["value"] = 0
        for i in range(101):
            bar["value"] = i
            root.update()
            root.after(15)

    tk.Button(content, text="Start", command=start, bg=ACCENT, fg="black").pack()

# ---------------- THEME SWITCH ----------------
def theme_demo():
    global current_theme
    clear_content()

    tk.Label(content, text="Theme Switcher", font=("Arial", 18, "bold")).pack(pady=10)

    def toggle_theme():
        global current_theme
        current_theme = "light" if current_theme == "dark" else "dark"
        apply_theme()

    tk.Button(
        content,
        text="Toggle Dark / Light",
        command=toggle_theme,
        bg=ACCENT,
        fg="black",
        width=20
    ).pack(pady=20)

    apply_theme()

# ---------------- SIDEBAR ----------------
def side_btn(text, cmd):
    return tk.Button(
        sidebar,
        text=text,
        command=cmd,
        bg="black",
        fg=ACCENT,
        width=20,
        pady=10,
        font=("Arial", 10, "bold")
    )

tk.Label(
    sidebar,
    text="UIXLab",
    fg=ACCENT,
    bg="black",
    font=("Arial", 18, "bold")
).pack(pady=20)

side_btn("Buttons", buttons_demo).pack(pady=5)
side_btn("Toggle Switch", toggle_demo).pack(pady=5)
side_btn("Slider", slider_demo).pack(pady=5)
side_btn("Progress Bar", progress_demo).pack(pady=5)
side_btn("Theme Switcher", theme_demo).pack(pady=5)

buttons_demo()
root.mainloop()