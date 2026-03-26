import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Feature extraction
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        1 if '@' in url else 0,
        1 if "https" in url else 0,
        1 if any(word in url for word in ["login", "verify", "secure", "account", "update"]) else 0
    ]

# Improved dataset
data = [
    ["https://google.com", 1],
    ["https://facebook.com", 1],
    ["https://amazon.in", 1],
    ["https://github.com", 1],
    ["https://openai.com", 1],
    ["https://linkedin.com", 1],
    ["https://microsoft.com", 1],
    ["https://apple.com", 1],

    ["http://login-facebook.com", 0],
    ["http://verify-paypal.com", 0],
    ["http://free-money@scam.com", 0],
    ["http://bank-secure-login.com", 0],
    ["http://update-account-now.net", 0],
    ["http://win-prize-click-here.com", 0],
    ["http://secure-login-amazon.com", 0],
    ["http://verify-your-bank-details.com", 0],
    ["http://click-to-claim-reward.com", 0],
    ["http://urgent-account-update.com", 0]
]

# Prepare data
X = [extract_features(url) for url, label in data]
y = [label for url, label in data]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Prediction function
def check_url():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Enter a URL")
        return

    features = [extract_features(url)]
    result = model.predict(features)[0]

    if result == 1:
        output_label.config(text="SAFE ✅", fg="green")
    else:
        output_label.config(text="PHISHING ❌", fg="red")

# UI
root = tk.Tk()
root.title("Advanced Phishing URL Detector")
root.geometry("420x260")

tk.Label(root, text="Enter URL:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=45)
entry.pack()

tk.Button(root, text="Check URL", command=check_url).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack()

root.mainloop()