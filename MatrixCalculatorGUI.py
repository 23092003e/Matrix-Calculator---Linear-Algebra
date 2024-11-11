import numpy as np
from tkinter import *
import time
from MatrixCal import MatrixCode

class MatrixCalculatorGUI:
    def __init__(self, root):
        self.MatrixCal = MatrixCode()
        self.root = root
        self.root.geometry("500x500")
        self.root.iconbitmap("matrix.ico")
        self.root.title("Matrix Calculator")
        self.root.configure(bg = "#6a7491")

        self.localtime = time.asctime(time.localtime(time.time()))

        self.setup_gui()

    def setup_gui(self):
        tops = Frame(root, width = 500, height = 50, bg = "#dde0eb")
        tops.pack(side = TOP)

        f1 = Frame(root, width = 500, height = 100, bg = "#dde0eb")
        f1.pack(side = TOP, pady = (16, 0))

        f2 = Frame(root, width = 500, height = 100, bg = "#dde0eb")
        f2.pack(side = TOP, pady = (32,0))

        f3 = Frame(root, width = 500, height = 100, bg = "#dde0eb")
        f3.pack(side = TOP, pady=(32,0))

        f4 = Frame(root, width = 500, height = 100, bg = "#dde0eb")
        f4.pack(side = TOP, pady= (32,0))

        title = Label(tops, font = ("arial", "12", "bold"), text = "Matrix Operations Demo", bg = "#dde0eb", fg = "#FFFFFF")
        title.grid(row = 0, column = 0, pady = (8, 0)) # Program title

        date = Label(tops, text = self.localtime, bg = "#dde0eb", fg = "#FFFFFF")
        date.grid(row = 1, column = 0, pady = (0, 8)) # Local time when opening the program
        
        #Label Matrix A
        mA = Label(f1, font = ("arial", "9", "bold"), text = "Matrix A", bg = "#dde0eb", fg = "#FFFFFF")
        mA.grid(row = 0, column = 0, columnspan = 2, pady = 4)

        #Label Matrix B
        mB = Label(f1, font = ("arial", "9", "bold"), text = "Matrix B", bg = "#dde0eb", fg = "#FFFFFF")
        mB.grid(row = 0, column = 2, columnspan = 2, padx = (40, 0), pady = 4)

        #Label scalar K
        sK = Label(f1, font = ("arial", "9", "bold"), text = "Scalar K", bg = "#dde0eb", fg = "#FFFFFF")
        sK.grid(row = 0, column = 4, columnspan = 2, padx = (40, 0), pady = 4)

        #Row labels (matrix A)
        rA = Label(f1, text = "Rows   ", bg = "#dde0eb", fg = "#FFFFFF"); rA.grid(row = 1, column = 0)
        eRA = Entry(f1, width = 5, justify = "center", relief = SUNKEN, bd = 3); eRA.grid(row = 1, column = 1)

        #Row labels (matrix B)
        rB = Label(f1, text = "Rows   ", bg = "#dde0eb", fg = "#FFFFFF"); rB.grid(row = 1, column = 2, padx = (40, 0))
        eRB = Entry(f1, width = 5, justify = "center", relief = SUNKEN, bd = 3); eRB.grid(row = 1, column = 3)

        # Value Label (Scalar K)
        nK = Label(f1, text = "Value   ", bg = "#dde0eb", fg = "#FFFFFF"); nK.grid(row = 1, column = 4, padx = (40, 0))
        eNK = Entry(f1, width = 5, justify = "center", relief = SUNKEN, bd = 3); eNK.grid(row = 1, column = 5)

        # Column Label (Matrix A)
        cA = Label(f1, text = "Columns", bg = "#dde0eb", fg = "#FFFFFF"); cA.grid(row = 2, column = 0)
        eCA = Entry(f1, width = 5, justify = "center", relief = SUNKEN, bd = 3); eCA.grid(row = 2, column = 1)

        # Column Label (Matrix B)
        cB = Label(f1, text = "Columns", bg = "#dde0eb", fg = "#FFFFFF"); cB.grid(row = 2, column = 2, padx = (40, 0))
        eCB = Entry(f1, width = 5, justify = "center", relief = SUNKEN, bd = 3); eCB.grid(row = 2, column = 3)

        # Button generate
        generate = Button(f1, text = "Generate", command = MatrixCode.Generate, width = 8, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF")
        generate.grid(row = 1, column = 6, padx = (40, 0))

        # Button save
        destroy = Button(f1, text = "Destroy", command = MatrixCode.Destroy, width = 8, relief = GROOVE, bg = "#FF5264", fg = "#FFFFFF", state = DISABLED)
        destroy.grid(row = 2, column = 6, padx = (40, 0), pady = (4, 0))

        eRA.insert(0, 0); eCA.insert(0, 0); eRB.insert(0, 0); eCB.insert(0, 0); eNK.insert(0, 0)

        #Button save --> Save
        save = Button(f2, text = "Save", width = 12, height = 1, command = MatrixCode.Save, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        save.grid(row = 0, column = 0)

        #Button delete --> Delete
        delete = Button(f2, text = "Delete", width = 12, command = MatrixCode.Delete, relief = GROOVE, bg = "#FF5264", fg = "#FFFFFF", state = DISABLED)
        delete.grid(row = 1, column = 0, pady = (4, 0), columnspan = 2)

        # Button add --> Addition
        add = Button(f2, text = "Addition", width = 12, command = MatrixCode.Add, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        add.grid(row = 0, column = 1, padx = (10, 0))

        # Button subtract --> Subtraction
        subtract = Button(f2, text = "Subtraction", width = 12, command = MatrixCode.Subtract, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        subtract.grid(row = 1, column = 1, padx = (10, 0), pady = (4, 0), columnspan = 2)

        # Button multiply -> Multiplication
        multiply = Button(f2, text = "Multiply", width = 12, command = MatrixCode.Multiply, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        multiply.grid(row = 0, column = 2, padx = (10, 0))

        # Button determinant --> Determinant
        determinant = Button(f2, text = "Determinant", width = 12, command = MatrixCode.Determinant, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        determinant.grid(row = 1, column = 2, padx = (10, 0), pady = (4, 0), columnspan = 2)

        # Button scalar --> Scalar multiplication
        scalar = Button(f2, text = "Scalar multiplication", width = 12, command = MatrixCode.Scalar, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
        scalar.grid(row = 0, column = 3, padx = (10, 0))

root = Tk()
app = MatrixCalculatorGUI(root)
root.mainloop()
