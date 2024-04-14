import tkinter as tk
from tkinter import messagebox


voters = {}

votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}


def register_voter():
    voter_id = voter_id_entry.get()
    voter_name = voter_name_entry.get()


    if voter_id in voters:
        messagebox.showerror("Error", "Voter ID already registered.")
        return


    voters[voter_id] = voter_name

    voter_id_entry.delete(0, tk.END)
    voter_name_entry.delete(0, tk.END)


    voting_page()

def vote(candidate):
    voter_id = voter_id_entry.get()

    if voter_id not in voters:
        messagebox.showerror("Error", "Invalid voter ID.")
        return

    votes[candidate] += 1


    voter_id_entry.delete(0, tk.END)


    messagebox.showinfo("Success", "Your vote has been recorded.")


def voting_page():
    voter_id_label.pack_forget()
    voter_name_label.pack_forget()
    voter_id_entry.pack_forget()
    voter_name_entry.pack_forget()
    register_button.pack_forget()

    voter_id_label.pack()
    voter_id_entry.pack()

    candidate_label = tk.Label(root, text="Select a candidate:")
    candidate_label.pack()

    candidate_a_button = tk.Button(root, text="Candidate A", command=lambda: vote("Candidate A"))
    candidate_a_button.pack()

    candidate_b_button = tk.Button(root, text="Candidate B", command=lambda: vote("Candidate B"))
    candidate_b_button.pack()

    candidate_c_button = tk.Button(root, text="Candidate C", command=lambda: vote("Candidate C"))
    candidate_c_button.pack()


root = tk.Tk()
root.title("Online Voting Platform")


voter_id_label = tk.Label(root, text="Enter your voter ID:")
voter_id_label.pack()
voter_id_entry = tk.Entry(root)
voter_id_entry.pack()

voter_name_label = tk.Label(root, text="Enter your name:")
voter_name_label.pack()
voter_name_entry = tk.Entry(root)
voter_name_entry.pack()


register_button = tk.Button(root, text="Register", command=register_voter)
register_button.pack()


root.mainloop()