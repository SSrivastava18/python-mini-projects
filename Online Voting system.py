import tkinter as tk
from tkinter import messagebox

# List of valid voter IDs
valid_voter_ids = ["123456", "789012", "345678"]

def check_voter_id():
    voter_id = voter_id_entry.get()
    voter_name = voter_name_entry.get()

    if voter_id in valid_voter_ids:
        voter_id_entry.config(state="disabled")
        voter_name_entry.config(state="disabled")
        display_voting_options(voter_id, voter_name)
    else:
        messagebox.showerror("Invalid Voter ID", "The entered Voter ID is not valid.")

def display_voting_options(voter_id, voter_name):
    voting_window = tk.Toplevel(root)
    voting_window.title("Vote Casting")

    vote_var = tk.StringVar()

    label = tk.Label(voting_window, text=f"Welcome, {voter_name} (Voter ID: {voter_id})")
    label.pack(pady=10)

    options = ["Option 1", "Option 2", "Option 3"]
    for option in options:
        radio_button = tk.Radiobutton(voting_window, text=option, variable=vote_var, value=option)
        radio_button.pack(fill="x", padx=20, pady=5)

    submit_button = tk.Button(voting_window, text="Submit Vote", command=lambda: submit_vote(voter_id, voter_name, vote_var.get()))
    submit_button.pack(pady=10)

def submit_vote(voter_id, voter_name, vote):
    if vote:
        print(f"Voter ID: {voter_id}")
        print(f"Voter Name: {voter_name}")
        print(f"Vote: {vote}")
        messagebox.showinfo("Vote Submitted", "Thank you for voting!")
        root.quit()
    else:
        messagebox.showerror("No Option Selected", "Please select a voting option.")

root = tk.Tk()
root.title("Online Voting System")
root.geometry("600x500")

voter_id_label = tk.Label(root, text="Voter ID:")
voter_id_label.pack(pady=5)

voter_id_entry = tk.Entry(root)
voter_id_entry.pack(pady=5)

voter_name_label = tk.Label(root, text="Voter Name:")
voter_name_label.pack(pady=5)

voter_name_entry = tk.Entry(root)
voter_name_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=check_voter_id)
submit_button.pack(pady=10)

root.mainloop()