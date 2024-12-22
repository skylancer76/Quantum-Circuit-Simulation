import tkinter as tk
from tkinter import Canvas, Frame, Label

class QuantumCircuitSimulator:

    def __init__(self, master):
        self.master = master 
        self.master.title("Quantum Circuit Simulator")

        self.frame = Frame(self.master)
        self.frame.pack()

        self.canvas = Canvas(self.frame, width = 600, height = 400, bg = 'black')
        self.canvas.pack(side = tk.TOP)

        self.label = Label(self.frame, text = "Drag and drop gates onto the circuit.")
        self.label.pack()

        # List of gates 
        self.gates = ["Hadamard", "Pauli-X", "Pauli-Y", "Pauli-Z", "CNOT", "Phase"]

        for gate in self.gates:
            button = tk.Button(self.frame, text=gate, command=lambda g=gate: self.add_gate(g))
            button.pack(side=tk.LEFT)

        # Enable drag for buttons to canvas 
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)


    def add_gate(self, gate):
        x = 50  # Initial x position
        y = len(self.gates) * 20 + 20 
        self.canvas.create_rectangle(x, y, x + 100, y + 30, fill="lightblue", tags=gate)
        self.canvas.create_text(x + 50, y + 15, text=gate)


    def on_click(self, event):
        # Check if a gate is clicked
        item = self.canvas.find_closest(event.x, event.y)
        if item:
            print(f"Clicked on: {self.canvas.gettags(item)[0]}")


    def on_drag(self, event):
        # Move the gate with mouse movement
        item = self.canvas.find_closest(event.x, event.y)
        if item:
            x = event.x - 50  # Centering the rectangle
            y = event.y - 15  # Centering the rectangle
            self.canvas.coords(item, x, y, x + 100, y + 30)
            self.canvas.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumCircuitSimulator(root)
    root.mainloop()