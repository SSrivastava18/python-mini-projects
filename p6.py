import tkinter as tk

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Voting System")
        self.master.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label_id = tk.Label(self.master, text="Enter Voter ID:")
        self.label_id.pack()
        
        self.entry_id = tk.Entry(self.master)
        self.entry_id.pack()
        
        self.label_name = tk.Label(self.master, text="Enter Your Name:")
        self.label_name.pack()
        
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack()
        
        self.button_cast_vote = tk.Button(self.master, text="Cast Vote", command=self.cast_vote)
        self.button_cast_vote.pack()
    
    def cast_vote(self):
        voter_id = self.entry_id.get()
        voter_name = self.entry_name.get()
        
        
        self.show_voting_options()
    
    def show_voting_options(self):
        self.master.destroy()  
        
        
        voting_options_window = tk.Tk()
        voting_options_window.title("Voting Options")
        voting_options_window.geometry("400x300")
        
        
        parties = ["BJP party", "Congress party"]
        
        
        self.selected_party = tk.StringVar()
        for party in parties:
            tk.Radiobutton(voting_options_window, text=party, variable=self.selected_party, value=party).pack()
        
        
        button_submit_vote = tk.Button(voting_options_window, text="Submit Vote", command=self.submit_vote)
        button_submit_vote.pack()
        
        voting_options_window.mainloop()
    
    def submit_vote(self):
        selected_party = self.selected_party.get()
        
        
        
        
        print("Vote submitted for:", selected_party)
        print("Thank you for voting!")
        exit()  

def main():
    root = tk.Tk()
    app = VotingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()







