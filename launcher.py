import tkinter as tk
from tkinter import scrolledtext, font as tkfont
import subprocess
import os

PROJECTS_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECTS = [
    ("fruit-stand.py",      "Fruit Stand Game",        "Pick a random fruit from a basket — keep going until you find one you like!"),
    ("plane.py",            "Plane Classes",            "Learn about classes and objects using aeroplanes."),
    ("speak.py",            "Text to Speech",           "Type anything and make your computer say it out loud!"),
    ("turtle-01.py",        "Turtle Flower (Example)",  "Draw flower patterns using functions and turtle graphics."),
    ("turtle-00.py",        "Turtle Flower",            "Another turtle flower — try changing the numbers to see what happens!"),
]

BG        = "#1e1e2e"
PANEL     = "#181825"
TEXT      = "#cdd6f4"
ACCENT    = "#89b4fa"
GREEN     = "#a6e3a1"
SUBTEXT   = "#6c7086"


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Pets - Project Launcher")
        self.geometry("960x620")
        self.configure(bg=BG)
        self.resizable(True, True)
        self._build_ui()
        self._select(0)

    def _build_ui(self):
        # ── Left panel: project list ──────────────────────────────────────────
        left = tk.Frame(self, bg=PANEL, width=240)
        left.pack(side=tk.LEFT, fill=tk.Y)
        left.pack_propagate(False)

        tk.Label(
            left, text="Projects",
            bg=PANEL, fg=ACCENT,
            font=("Helvetica", 13, "bold"),
            pady=12
        ).pack()

        tk.Frame(left, bg=SUBTEXT, height=1).pack(fill=tk.X, padx=12)

        self.listbox = tk.Listbox(
            left,
            bg=PANEL, fg=TEXT,
            selectbackground=ACCENT, selectforeground=PANEL,
            font=("Helvetica", 11),
            bd=0, highlightthickness=0,
            activestyle="none",
            cursor="hand2",
        )
        for _, name, _ in PROJECTS:
            self.listbox.insert(tk.END, f"  {name}")

        self.listbox.pack(fill=tk.BOTH, expand=True, padx=4, pady=8)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        # ── Right panel ───────────────────────────────────────────────────────
        right = tk.Frame(self, bg=BG)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Project name heading
        self.title_label = tk.Label(
            right, text="",
            bg=BG, fg=ACCENT,
            font=("Helvetica", 14, "bold"),
            anchor="w", padx=14, pady=8,
        )
        self.title_label.pack(fill=tk.X)

        # Description
        self.desc_label = tk.Label(
            right, text="",
            bg=BG, fg=GREEN,
            font=("Helvetica", 11),
            anchor="w", padx=14, wraplength=680, justify="left",
        )
        self.desc_label.pack(fill=tk.X)

        tk.Frame(right, bg=SUBTEXT, height=1).pack(fill=tk.X, padx=14, pady=6)

        # Code viewer
        code_font = tkfont.Font(family="Courier", size=12)
        self.code_view = scrolledtext.ScrolledText(
            right,
            bg=PANEL, fg=TEXT,
            font=code_font,
            bd=0, relief=tk.FLAT,
            insertbackground="white",
            state=tk.DISABLED,
            padx=12, pady=10,
        )
        self.code_view.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 6))

        # Run button
        btn_frame = tk.Frame(right, bg=BG)
        btn_frame.pack(fill=tk.X, padx=14, pady=(0, 14))

        run_btn = tk.Button(
            btn_frame,
            text="  Run Project",
            command=self._run,
            bg=ACCENT, fg=PANEL,
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            padx=24, pady=8,
            cursor="hand2",
            activebackground="#74c7ec",
            activeforeground=PANEL,
        )
        run_btn.pack(side=tk.LEFT)

        self.status_label = tk.Label(
            btn_frame, text="",
            bg=BG, fg=SUBTEXT,
            font=("Helvetica", 10),
        )
        self.status_label.pack(side=tk.LEFT, padx=14)

    def _select(self, index):
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(index)
        self.current = index

        filename, name, desc = PROJECTS[index]
        self.title_label.config(text=name)
        self.desc_label.config(text=desc)
        self.status_label.config(text="")

        path = os.path.join(PROJECTS_DIR, filename)
        with open(path) as f:
            code = f.read()

        self.code_view.config(state=tk.NORMAL)
        self.code_view.delete("1.0", tk.END)
        self.code_view.insert(tk.END, code)
        self.code_view.config(state=tk.DISABLED)

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if sel:
            self._select(sel[0])

    def _run(self):
        filename, name, _ = PROJECTS[self.current]
        path = os.path.join(PROJECTS_DIR, filename)

        # Open the script in a new Terminal window (macOS)
        apple_script = f'tell application "Terminal" to do script "python3 \\"{path}\\""'
        subprocess.Popen(["osascript", "-e", apple_script])

        self.status_label.config(text=f'Launched "{name}" in Terminal')


if __name__ == "__main__":
    app = Launcher()
    app.mainloop()
