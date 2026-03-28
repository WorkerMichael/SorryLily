import tkinter as tk

class SorryLily:
    def __init__(self, root):
        self.root = root
        self.root.title("The Sorry Lily")
        self.root.geometry("400x500")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightthickness=0)
        self.canvas.pack()
        
        self.status_label = tk.Label(root, text="Click a petal...", font=("Helvetica", 14))
        self.status_label.pack(pady=20)

        self.draw_lily()

        # Reset Button
        self.reset_btn = tk.Button(root, text="Regrow Lily", command=self.draw_lily)
        self.reset_btn.pack()

    def draw_lily(self):
        self.canvas.delete("all")
        cx, cy = 200, 200
        
        # Stem
        self.canvas.create_line(cx, cy, cx, 400, fill="#2d5a27", width=6)
        
        # Petal Positions (x1, y1, x2, y2)
        petal_coords = [
            (180, 100, 220, 200), # Top
            (220, 130, 310, 210), # Top Right
            (230, 210, 310, 290), # Bottom Right
            (180, 230, 220, 330), # Bottom
            (90, 210, 170, 290),  # Bottom Left
            (90, 130, 180, 210),  # Top Left
        ]
        
        for coord in petal_coords:
            petal = self.canvas.create_oval(coord, fill="#ffcce7", outline="#ff80bf", width=2)
            # Bind click event
            self.canvas.tag_bind(petal, '<Button-1>', lambda e, p=petal: self.apologize(p))
            
        # Center of the Lily
        self.canvas.create_oval(185, 185, 215, 215, fill="#ffd700", outline="#ccac00")

    def apologize(self, petal_id):
        self.canvas.delete(petal_id)
        print("Sorry") # Console output
        self.status_label.config(text="Sorry", fg="#d90429")
        
        # Fade the "Sorry" text back to neutral after 800ms
        self.root.after(800, lambda: self.status_label.config(text="...", fg="gray"))

if __name__ == "__main__":
    root = tk.Tk()
    app = SorryLily(root)
    root.mainloop()
