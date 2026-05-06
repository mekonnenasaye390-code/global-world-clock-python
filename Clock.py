import tkinter as tk
from datetime import datetime
import pytz

root = tk.Tk()
root.title("World Clock work by Mekonnen")
root.geometry("620x600")
root.resizable(False, False)
root.configure(bg="#0f111a")

title = tk.Label(
    root,
    text="🌍 WORLD CLOCK",
    font=("Arial", 20, "bold"),
    bg="#0f111a",
    fg="#00ffcc"
)
title.pack(pady=10)


cities = {
    "Ethiopia (Addis Ababa)": "Africa/Addis_Ababa",
    "USA (New York)": "America/New_York",
    "UK (London)": "Europe/London",
    "UAE (Dubai)": "Asia/Dubai",
    "India (Delhi)": "Asia/Kolkata"
}

labels = {}

for city in cities:
    frame = tk.Frame(root, bg="#0f111a")
    frame.pack(fill="x", pady=5)

    lbl = tk.Label(
        frame,
        text=city,
        font=("Arial", 12, "bold"),
        bg="#0f111a",
        fg="white",
        width=25,
        anchor="w"
    )
    lbl.pack(side="left", padx=10)

    time_lbl = tk.Label(
        frame,
        text="",
        font=("Arial", 12),
        bg="#0f111a",
        fg="#00ffcc"
    )
    time_lbl.pack(side="right", padx=10)

    labels[city] = time_lbl

def update_time():
    for city, tz in cities.items():
        timezone = pytz.timezone(tz)
        time_now = datetime.now(timezone).strftime("%H:%M:%S")

        labels[city].config(text=time_now)

    root.after(1000, update_time)

update_time()

root.mainloop()