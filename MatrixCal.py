# Import library for LinearAlgebra
import numpy as np 
from tkinter import *
import tkinter as tk

"""Function to handle matrix calculations."""
class MatrixCode:

    
    def Generate():
        # Handling Exceptions
        try:
            generate["state"] = tk.DISABLED; 
            save["state"] = tk.NORMAL    
            destroy["state"] = tk.NORMAL

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
            generate["state"] = tk.DISABLED; 
            save["state"] = tk.NORMAL    
            destroy["state"] = tk.NORMAL

            # Displays message box if error occurs
            messagebox.showinfo(title = "Information", message = "Please fill in the data correctly!!!")

    def Destroy():
        # Change the state value of a button
        delete["state"] = tk.DISABLED; 
        add["state"] = tk.DISABLED
        subtract["state"] = tk.DISABLED; 
        multiply["state"] = tk.DISABLED
        determinant["state"] = tk.DISABLED; 
        save["state"] = DISABLED
        destroy["state"] = tk.DISABLED; 
        scalar["state"] = tk.DISABLED
        generate["state"] = tk.NORMAL

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
            save["state"] = tk.DISABLED; 
            delete["state"] = tk.NORMAL

            # If-elif-else statement 
            if (P > 0) and (Q > 0):                                            
                add["state"] = tk.NORMAL; 
                subtract["state"] = tk.NORMAL
                multiply["state"] = tk.NORMAL; 
                determinant["state"] = tk.DISABLED
                scalar["state"] = tk.DISABLED
            elif (K > 0):                                                       
                scalar["state"] = tk.NORMAL
                determinant["state"] = tk.DISABLED
            else:                                                               
                determinant["state"] = tk.NORMAL

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
            save["state"] = tk.NORMAL; 
            delete["state"] = tk.DISABLED
            add["state"] = tk.DISABLED; 
            subtract["state"] = tk.DISABLED
            multiply["state"] = tk.DISABLED; 
            determinant["state"] = tk.DISABLED
            scalar["state"] = tk.DISABLED
            
            # Displays message box if error occurs
            messagebox.showinfo(title = "Information", message = "Matrix entries are still empty!!!")

    def Delete():
        # Change the state value of a button 
        delete["state"] = tk.DISABLED; 
        add["state"] = tk.DISABLED         
        subtract["state"] = tk.DISABLED; 
        multiply["state"] = tk.DISABLED
        determinant["state"] = tk.DISABLED; 
        save["state"] = tk.NORMAL

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

        for i in rane(len(C[0])):
            for j in range(len(C[0])):
                Entry = Entry(f4, width = 5, justify="center")
                entry.grid(row = i+1, column = j)
                entry.insert(0,C[i,j])

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

        titleC = Label(f4, font = ("arial", "g","bold"), text = "A x B", bg = "#474E64", fg = "#FFFFFF")
        titleC.grid(row = 0, column = 0, columnspan = len(C[0]))

        for i in range(len(C)):
            for j in range(len(C[0])):
                entry = Entry(f4, width=5, justify="center")
                entry.grid(row = i + 1, column = j)
                entry.insert(0, C[i,j])

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