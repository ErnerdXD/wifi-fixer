import base64
import ctypes
import re
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import ttk

ICON_B64 = "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"

BG = "#16181d"
CARD = "#1f2229"
CARD_HOVER = "#282c35"
ACCENT = "#0a84ff"
ACCENT_HOVER = "#3a9bff"
TEXT = "#e8eaed"
MUTED = "#8b919c"
GREEN = "#34c759"
RED = "#ff5f57"
LOG_BG = "#101216"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


if not is_admin():
    params = "" if getattr(sys, "frozen", False) else f'"{sys.argv[0]}"'
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True,
                       creationflags=0x08000000)  # no console window
    return (r.stdout + r.stderr).strip()


# ---------- UI helpers (thread-safe via root.after) ----------
def log(msg, color=TEXT):
    def _do():
        box.configure(state="normal")
        box.insert(tk.END, msg + "\n", color)
        box.see(tk.END)
        box.configure(state="disabled")
    root.after(0, _do)


def set_status(text, color=MUTED):
    root.after(0, lambda: status.configure(text=text, fg=color))


def busy(on):
    def _do():
        for b in buttons:
            b.enabled = not on
            b.refresh()
        if on:
            bar.pack(fill="x", padx=24, pady=(0, 10), before=box_frame)
            bar.start(12)
        else:
            bar.stop()
            bar.pack_forget()
    root.after(0, _do)


# ---------- actions ----------
def fix_wifi():
    busy(True)
    set_status("Fixing Wi-Fi...", ACCENT)
    log("▶ Fix Wi-Fi", ACCENT)
    log("Rescanning hardware...", MUTED)
    log(run("pnputil /scan-devices") or "OK")
    log("Checking WLAN service...", MUTED)
    out = run("sc.exe queryex WlanSvc")
    m = re.search(r"PID\s*:\s*(\d+)", out)
    pid = m.group(1) if m else "0"
    if pid != "0":
        log(f"Killing stuck service (PID {pid})...", MUTED)
        log(run(f"taskkill /f /pid {pid}"))
    log("Starting WlanSvc...", MUTED)
    log(run("net start WlanSvc"))
    log("Enabling Wi-Fi adapter...", MUTED)
    log(run('powershell -Command "Get-NetAdapter | Where-Object {$_.Name -like \'*Wi-Fi*\'} | '
            'Enable-NetAdapter -Confirm:$false"') or "OK")
    log("Restarting Explorer (taskbar will flash)...", MUTED)
    run("taskkill /f /im explorer.exe")
    subprocess.Popen("explorer.exe", creationflags=0x08000000)
    log("✔ Done. Check your Wi-Fi button.", GREEN)
    log("If it's still missing, the Wi-Fi driver needs reinstalling.\n", MUTED)
    set_status("Done", GREEN)
    busy(False)


def reset_network():
    busy(True)
    set_status("Resetting network...", ACCENT)
    log("▶ Reset Network", ACCENT)
    steps = [
        ("Resetting Winsock...", "netsh winsock reset"),
        ("Resetting IP stack...", "netsh int ip reset"),
        ("Releasing IP...", "ipconfig /release"),
        ("Renewing IP...", "ipconfig /renew"),
        ("Flushing DNS...", "ipconfig /flushdns"),
    ]
    for label, cmd in steps:
        log(label, MUTED)
        log(run(cmd))
    log("✔ Done. Restart your PC if internet still doesn't work.\n", GREEN)
    set_status("Done", GREEN)
    busy(False)


# ---------- widgets ----------
class Tooltip:
    def __init__(self, widget, text):
        self.widget, self.text, self.tip = widget, text, None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, _=None):
        x = self.widget.winfo_rootx() - 250
        y = self.widget.winfo_rooty() + 30
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_attributes("-topmost", True)
        self.tip.wm_geometry(f"+{max(x, 5)}+{y}")
        tk.Label(self.tip, text=self.text, justify="left", bg="#2b2f38", fg=TEXT,
                 relief="flat", bd=0, font=("Segoe UI", 9), padx=12, pady=10).pack()

    def hide(self, _=None):
        if self.tip:
            self.tip.destroy()
            self.tip = None


class FlatButton(tk.Label):
    def __init__(self, parent, text, subtitle, command):
        super().__init__(parent, text=f"{text}\n{subtitle}", font=("Segoe UI", 11, "bold"),
                         bg=ACCENT, fg="white", justify="center", cursor="hand2", pady=10)
        self.command, self.enabled = command, True
        self.bind("<Enter>", lambda e: self._set(ACCENT_HOVER))
        self.bind("<Leave>", lambda e: self._set(ACCENT))
        self.bind("<Button-1>", self._click)

    def _set(self, color):
        if self.enabled:
            self.configure(bg=color)

    def _click(self, _):
        if self.enabled:
            threading.Thread(target=self.command, daemon=True).start()

    def refresh(self):
        self.configure(bg=ACCENT if self.enabled else "#3a3f4b",
                       fg="white" if self.enabled else MUTED,
                       cursor="hand2" if self.enabled else "arrow")


root = tk.Tk()
root.title("Wi-Fi Fixer")
root.geometry("460x560")
root.minsize(420, 500)
root.configure(bg=BG)
try:
    root.iconphoto(True, tk.PhotoImage(data=base64.b64decode(ICON_B64)))
except Exception:
    pass

style = ttk.Style()
style.theme_use("clam")
style.configure("Blue.Horizontal.TProgressbar", troughcolor=CARD, background=ACCENT,
                bordercolor=CARD, lightcolor=ACCENT, darkcolor=ACCENT, thickness=4)

# header
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=24, pady=(22, 4))
logo = tk.PhotoImage(data=base64.b64decode(ICON_B64))
logo_lbl = tk.Label(header, image=logo, bg=BG)
logo_lbl.image = logo
logo_lbl.pack(side="left")
titles = tk.Frame(header, bg=BG)
titles.pack(side="left", padx=12)
tk.Label(titles, text="Wi-Fi Fixer", font=("Segoe UI", 18, "bold"), bg=BG, fg=TEXT).pack(anchor="w")
tk.Label(titles, text="Quick repair for Wi-Fi problems", font=("Segoe UI", 9), bg=BG, fg=MUTED).pack(anchor="w")

buttons = []


def add_card(text, subtitle, func, info):
    card = tk.Frame(root, bg=CARD)
    card.pack(fill="x", padx=24, pady=(14, 0))
    inner = tk.Frame(card, bg=CARD)
    inner.pack(fill="x", padx=12, pady=12)
    b = FlatButton(inner, text, subtitle, func)
    b.pack(side="left", fill="x", expand=True)
    icon = tk.Label(inner, text="ⓘ", font=("Segoe UI", 17), bg=CARD, fg=MUTED, cursor="question_arrow")
    icon.pack(side="left", padx=(12, 2))
    icon.bind("<Enter>", lambda e: icon.configure(fg=ACCENT), add="+")
    icon.bind("<Leave>", lambda e: icon.configure(fg=MUTED), add="+")
    Tooltip(icon, info)
    buttons.append(b)


add_card("Fix Wi-Fi", "Greyed out or missing Wi-Fi button", fix_wifi,
         "Use when the Wi-Fi button is greyed out,\n"
         "missing, or the Wi-Fi list won't open.\n\n"
         "•  Rescans hardware to re-detect the adapter\n"
         "•  Force-kills the stuck WLAN service\n"
         "•  Starts it again\n"
         "•  Re-enables the Wi-Fi adapter\n"
         "•  Restarts Explorer (taskbar flashes)")

add_card("Reset Network", "Connected but no internet", reset_network,
         "Use when Wi-Fi is connected but there is\n"
         "no internet, or Fix Wi-Fi didn't help.\n\n"
         "•  Resets Winsock and the IP stack\n"
         "•  Releases and renews your IP address\n"
         "•  Flushes the DNS cache\n\n"
         "You will lose connection for a few seconds.\n"
         "A PC restart may be needed to fully apply.")

# status + log
status = tk.Label(root, text="Ready", font=("Segoe UI", 10, "bold"), bg=BG, fg=MUTED, anchor="w")
status.pack(fill="x", padx=24, pady=(18, 6))

bar = ttk.Progressbar(root, mode="indeterminate", style="Blue.Horizontal.TProgressbar")

box_frame = tk.Frame(root, bg=LOG_BG)
box_frame.pack(fill="both", expand=True, padx=24, pady=(0, 22))
box = tk.Text(box_frame, bg=LOG_BG, fg=TEXT, font=("Consolas", 9), bd=0, relief="flat",
              padx=10, pady=8, state="disabled", wrap="word", height=8)
sb = tk.Scrollbar(box_frame, command=box.yview)
box.configure(yscrollcommand=sb.set)
sb.pack(side="right", fill="y")
box.pack(side="left", fill="both", expand=True)
for name, col in ((TEXT, TEXT), (MUTED, MUTED), (GREEN, GREEN), (ACCENT, ACCENT), (RED, RED)):
    box.tag_configure(name, foreground=col)

root.mainloop()
