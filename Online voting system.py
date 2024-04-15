import tkinter as tk
from tkinter import messagebox

# Voter database (for demonstration purposes)
voter_database = {
    "123456": {"name": "Saurabh Srivastava", "pin": "1234"},
    "789012": {"name": "Raushan Gupta", "pin": "5678"}
}

class VotingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Online Voting System")
        self.geometry("300x200")

        # Voter credentials
        self.voter_id = tk.StringVar()
        self.voter_name = tk.StringVar()
        self.voter_pin = tk.StringVar()

        # Voting options
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]
        self.selected_candidate = tk.StringVar()

        # Login frame
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(padx=20, pady=20)

        tk.Label(self.login_frame, text="Voter ID:").grid(row=0, column=0)
        tk.Entry(self.login_frame, textvariable=self.voter_id).grid(row=0, column=1)

        tk.Label(self.login_frame, text="PIN:").grid(row=2, column=0)
        tk.Entry(self.login_frame, textvariable=self.voter_pin, show="*").grid(row=2, column=1)

        tk.Button(self.login_frame, text="Login", command=self.verify_credentials).grid(row=3, column=0, columnspan=2, pady=10)

    def verify_credentials(self):
        voter_id = self.voter_id.get()
        voter_pin = self.voter_pin.get()

        if voter_id in voter_database and voter_database[voter_id]["pin"] == voter_pin:
            self.voter_name.set(voter_database[voter_id]["name"])
            self.login_frame.destroy()
            self.voting_frame = tk.Frame(self)
            self.voting_frame.pack(padx=20, pady=20)

            tk.Label(self.voting_frame, text="Select a candidate:").pack()

            for candidate in self.candidates:
                tk.Radiobutton(self.voting_frame, text=candidate, variable=self.selected_candidate, value=candidate).pack()

            tk.Button(self.voting_frame, text="Vote", command=self.cast_vote).pack(pady=10)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def cast_vote(self):
        selected_candidate = self.selected_candidate.get()
        if selected_candidate:
            voter_id = self.voter_id.get()
            voter_name = self.voter_name.get()
            print(f"Voter ID: {voter_id}")
            print(f"Voter Name: {voter_name}")
            print(f"Selected Candidate: {selected_candidate}")
            messagebox.showinfo("Success", "Your vote has been cast!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Please select a candidate")

if __name__ == "__main__":
    app = VotingApp()
    app.mainloop()





