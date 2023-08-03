import tkinter as tk
import smtplib
from tkinter import messagebox

def send_email():
    sender_email = email_entry.get()
    password = password_entry.get()
    receiver_email = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)

            email_content = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_content)

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("Mail Application")

# Email Entry
email_label = tk.Label(root, text="Your Email:")
email_label.grid(row=0, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

# Password Entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# To Entry
to_label = tk.Label(root, text="To:")
to_label.grid(row=2, column=0)
to_entry = tk.Entry(root)
to_entry.grid(row=2, column=1)

# Subject Entry
subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1)

# Message Entry
message_label = tk.Label(root, text="Message:")
message_label.grid(row=4, column=0)
message_text = tk.Text(root, height=5, width=30)
message_text.grid(row=4, column=1)

# Send Button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1)

# Run the application
root.mainloop()
