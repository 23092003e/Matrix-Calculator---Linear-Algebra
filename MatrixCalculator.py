from tkinter import *
from tkinter import messagebox
import numpy as np 
import time 

# GUI Layout
root = Tk()                                                                         
root.geometry("500x500") 
root.iconbitmap("matrix.ico")
root.title("Matrix Calculator")
root.configure(bg = "#6a7491")

tops = Frame(root, width = 500, height = 50, bg = "#474E64")   
tops.pack(side = TOP)                                           

f1 = Frame(root, width = 500, height = 100, bg = "#474E64")   
f1.pack(side = TOP, pady = (16, 0))                            

f2 = Frame(root, width = 500, height = 100, bg = "#474E64")     
f2.pack(side = TOP, pady = (32, 0))                            

f3 = Frame(root, width = 500, height = 100, bg = "#474E64")     
f3.pack(side = TOP, pady = (32, 0))                

f4 = Frame(root, width = 500, height = 100, bg = "#474E64")     
f4.pack(side = TOP, pady = (32, 0))  

def Generate():
    # Handling Exceptions
    try:
        generate["state"] = DISABLED; 
        save["state"] = NORMAL    
        destroy["state"] = NORMAL

        # Declaring global variables and getting the values ​​of M and N
        global M; global N; global rows1   
        M = int(eRA.get())                 
        N = int(eCA.get())            

        # Create a matrix A title and arrange its position  
        titleA = Label(f3, font = ("arial", "9", "bold"), text = "Matrix A", bg = "#474E64", fg = "#FFFFFF")  
        titleA.grid(row = 0, column = 0, columnspan = N)                                                      

        # Create entries for matrix A according to user input.
        rows1 = []                                                  
        for i in range(M):                                          
            cols1 = []                                              
            for j in range(N):                                      
                entry = Entry(f3, width= 5, justify = "center")     
                entry.grid(row = i+1, column = j)                   
                cols1.append(entry)                                 
            rows1.append(cols1)                                     

        # Declaring global variables and getting the values ​​of P and Q
        global P; global Q; global rows2  
        P = int(eRB.get())                 
        Q = int(eCB.get())            

        # If statement
        if (P > 0) and (Q > 0):
            # Create a matrix B title and arrange its position                                                                           
            titleB = Label(f3, font = ("arial", "9", "bold"), text = "Matrix B", bg = "#474E64", fg = "#FFFFFF")  
            titleB.grid(row = 0, column = N, columnspan = Q, padx = (50, 0))                                       

            # Create entries for matrix B according to user input.
            rows2 = []                                              
            for i in range(P):                                      
                cols2 = []                                          
                for j in range(Q):                                  
                    if (j == 0):                                    
                        pad = (50, 0)                               
                    else:                                          
                        pad = (0, 0)                               
                    entry = Entry(f3, width = 5, justify = "center")    
                    entry.grid(row = i+1, column = j+N, padx = pad)     
                    cols2.append(entry)                                
                rows2.append(cols2)                                     

        # Declaring a global variable and getting the value of K
        global K
        K = int(eNK.get())

    # Handling Exceptions
    except:                 
        # Change the state value of a button                                     
        generate["state"] = NORMAL; 
        save["state"] = DISABLED   
        destroy["state"] = DISABLED

        # Displays message box if error occurs
        messagebox.showinfo(title = "Information", message = "Please fill in the data correctly!!!")

def Destroy():
    # Change the state value of a button
    delete["state"] = DISABLED; add["state"] = DISABLED
    subtract["state"] = DISABLED; multiply["state"] = DISABLED
    determinant["state"] = DISABLED; save["state"] = DISABLED
    destroy["state"] = DISABLED; scalar["state"] = DISABLED
    generate["state"] = NORMAL

    # Deleting value from entry widget (row and column) on f1
    for widget in f1.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, "end")

    # Fills rows and columns with default values ​​of 0.
    eRA.insert(0, 0); eCA.insert(0, 0); eRB.insert(0, 0); eCB.insert(0, 0); eNK.insert(0, 0)

    # Delete all widgets on f3
    for widget in f3.winfo_children():
        widget.destroy()

    # Delete all widgets on f4
    for widget in f4.winfo_children():
        widget.destroy()
def Save():
# Handling Exceptions
    try:
        # Change the state value of a button
        save["state"] = DISABLED; 
        delete["state"] = NORMAL

        # If-elif-else statement 
        if (P > 0) and (Q > 0):                                            
            add["state"] = NORMAL; 
            subtract["state"] = NORMAL
            multiply["state"] = NORMAL; 
            determinant["state"] = DISABLED
            scalar["state"] = DISABLED
        elif (K > 0):                                                       
            scalar["state"] = NORMAL
            determinant["state"] = DISABLED
        else:                                                               
            determinant["state"] = NORMAL

        # Declaring global variables( A(Matrix A), B(Matrix B) )
        global A; global B

        # Create a list with the name entriesA --> matrix A
        entriesA = []

        # Takes the value from the entry column, then adds it to the entries listA
        for row in rows1:                           
            for col in row:                         
                entriesA.append(int(col.get()))
        
        # Convert list entriesA to numpy array reshape(M, N) --> A
        A = np.array(entriesA).reshape(M, N)

        # If statement
        if (P > 0) and (Q > 0):

            # Create a list with the name entriesB --> matrix B
            entriesB = []           

            # Takes the value from the entry column, then adds it to the entries listB
            for row in rows2:                           
                for col in row:                         
                    entriesB.append(int(col.get()))     
            
            # Convert list entriesB to numpy array reshape(P, Q) --> B
            B = np.array(entriesB).reshape(P, Q)
    
    # Handling Exceptions
    except:                                               
        # Change the state value of a button    
        save["state"] = NORMAL; 
        delete["state"] = DISABLED
        add["state"] = DISABLED; 
        subtract["state"] = DISABLED
        multiply["state"] = DISABLED; 
        determinant["state"] = DISABLED
        scalar["state"] = DISABLED
        
        # Displays message box if error occurs
        messagebox.showinfo(title = "Information", message = "Matrix entries are still empty!!!")

def Delete():
    # Change the state value of a button 
    delete["state"] = DISABLED; 
    add["state"] = DISABLED         
    subtract["state"] = DISABLED; 
    multiply["state"] = DISABLED
    determinant["state"] = DISABLED; 
    save["state"] = NORMAL

    # Deleting value from entry widget on f3
    for widget in f3.winfo_children():      
        if isinstance(widget, Entry):
            widget.delete(0, "end")         
    
    # Delete all widgets on f4
    for widget in f4.winfo_children():      
        widget.destroy()


#Addition Operation   
def Add():
    try:
        C = A + B
    except:
        messagebox.showinfo(title = "Conditions", message = "The order of both matrices must be the same")
    for widget in f4.winfo_children(): 
        widget.destroy()

    titleC = Label(f4, font = ("arial", "9","bold"), text = "A + B", bg = "#474E64", fg = "#FFFFFF")
    titleC.grid(row = 0, column = 0, columnspan=len(C[0]))

    for i in range(len(C)):                                     
        for j in range(len(C[0])):                              
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                   
            entry.insert(0, C[i, j])   

#Subtraction Operation
def Subtract():
    try:
        C = A - B
    except:
        messagebox.showinfo(title="Conditions", message="The order of both matrices must be the same")

    for widget in f4.winfo_children():
        widget.destroy()

    titleC = Label(f4, font = ("arial","9","bold"), text = "A - B", bg = "#474E64", fg="#FFFFFF")
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))

    for i in range(len(C)):
        for j in range(len(C[0])):
            entry = Entry(f4, width=5, justify="center")
            entry.grid(row = i+1, column= j)
            entry.insert(0,C[i,j])

# Mutiplication Operation
def Multiply():
    try:
        C = np.dot(A,B)
    except:
        messagebox.showinfo(title = "Conditions", message = "The number of columns of Matrix A is the same as the number of rows of Matrix A or the Order of both matrices must be the same")

    for widget in f4.winfo_children():
        widget.destroy()

    titleC = Label(f4, font = ("arial", "9","bold"), text = "A x B", bg = "#474E64", fg = "#FFFFFF")
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))

    for i in range(len(C)):                                     
        for j in range(len(C[0])):                             
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                  
            entry.insert(0, C[i, j]) 

#Determinat
def Determinant():
    try:
        D = round(np.linalg.det(A))
    except:
        messagebox.showinfo(title="Conditions", message = "The number of rows and columns must be the same")
    
    for entry in f4.winfo_children():
        entry.destroy()

    titleD = Label(f4, font = ("arial", "9", "bold"), text = "det(A)", bg = "#474E64", fg = "#FFFFFF"); titleD.grid(row = 0, column = 0)   
    entryD = Entry(f4, width= 5, justify = "center"); entryD.grid(row = 0, column = 1)
    entryD.insert(0, D)
#Scalar
def Scalar():
    C = A * K
    for widget in f4.winfo_children():
        widget.destroy()    

    titleC = Label(f4, font = ("arial", "9", "bold"), text = "A x K", bg = "#474E64", fg = "#FFFFFF")  
    titleC.grid(row = 0, column = 0, columnspan = len(C[0]))

    for i in range(len(C)):                                     
        for j in range(len(C[0])):                              
            entry = Entry(f4, width= 5, justify = "center")     
            entry.grid(row = i+1, column = j)                   
            entry.insert(0, C[i, j])


localtime = time.asctime(time.localtime(time.time()))   

title = Label(tops, font = ("arial", "12", "bold"), text = "Matrix Operations Demo", bg = "#dde0eb", fg = "#FFFFFF")
title.grid(row = 0, column = 0, pady = (8, 0)) 
date = Label(tops, text = localtime, bg = "#474E64", fg = "#FFFFFF")
date.grid(row = 1, column = 0, pady = (0, 8)) 

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
generate = Button(f1, text = "Generate", command = Generate, width = 8, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF")
generate.grid(row = 1, column = 6, padx = (40, 0))

# Button save
destroy = Button(f1, text = "Destroy", command = Destroy, width = 8, relief = GROOVE, bg = "#FF5264", fg = "#FFFFFF", state = DISABLED)
destroy.grid(row = 2, column = 6, padx = (40, 0), pady = (4, 0))

eRA.insert(0, 0); eCA.insert(0, 0); eRB.insert(0, 0); eCB.insert(0, 0); eNK.insert(0, 0)

#Button save --> Save
save = Button(f2, text = "Save", width = 12, height = 1, command = Save, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
save.grid(row = 0, column = 0)

#Button delete --> Delete
delete = Button(f2, text = "Delete", width = 12, command = Delete, relief = GROOVE, bg = "#FF5264", fg = "#FFFFFF", state = DISABLED)
delete.grid(row = 1, column = 0, pady = (4, 0), columnspan = 2)

# Button add --> Addition
add = Button(f2, text = "Addition", width = 12, command = Add, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
add.grid(row = 0, column = 1, padx = (10, 0))

# Button subtract --> Subtraction
subtract = Button(f2, text = "Subtraction", width = 12, command = Subtract, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
subtract.grid(row = 1, column = 1, padx = (10, 0), pady = (4, 0), columnspan = 2)

# Button multiply -> Multiplication
multiply = Button(f2, text = "Multiply", width = 12, command = Multiply, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
multiply.grid(row = 0, column = 2, padx = (10, 0))

# Button determinant --> Determinant
determinant = Button(f2, text = "Determinant", width = 12, command = Determinant, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
determinant.grid(row = 1, column = 2, padx = (10, 0), pady = (4, 0), columnspan = 2)

# Button scalar --> Scalar multiplication
scalar = Button(f2, text = "Scalar multiplication", width = 12, command = Scalar, relief = GROOVE, bg = "#3C4559", fg = "#FFFFFF", state = DISABLED)
scalar.grid(row = 0, column = 3, padx = (10, 0))


root.mainloop()
