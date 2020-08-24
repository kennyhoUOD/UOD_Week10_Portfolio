
'''

    Author:          Kenny Ho
    ICT 4370:        Python Programming
    Date Written:    August 19, 2020
    Description:     Week 10: Portfolio Programming Assignment:
                        Improving the Stock problem with Additional Functionality

'''

from Ho_Kenny_Portfolio_Programing_Assignment_class import  Purchases, MainApplication
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, messagebox
import os

def main():
    """
        The main method that will execute when file is run.
    """
    def input():
        """
            Request csv file from the user.
        """
        input_path = tk.filedialog.askopenfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__)))
            
        input_entry.delete(1, tk.END)  # Remove current text in entry
        input_entry.insert(0, input_path)  # Insert the 'path'

    def output():
        """
            Choose save as file location
        """
        path = tk.filedialog.asksaveasfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__)),
            defaultextension=".csv", 
            filetypes = (("csv files","*.csv"),("all files","*.*")))

        output_entry.delete(1, tk.END)  # Remove current text in entry
        output_entry.insert(0, path)  # Insert the 'path'

    def begin():
        """
            Run Calculation Program.
            Calculate Earnings and Yearly percent
            Save file to output location
        """
        data_file = input_entry.get()
        output_directory = output_entry.get()        

        if data_file == "":
            messagebox.showerror("Error", "Missing data file")
        elif output_directory == "":
            messagebox.showerror("Error", "Missing save path")
        else:
            MainApplication.run(data_file, output_directory)
            messagebox.showinfo("Processing Complete", "Command Processed Completly")

    ### Prepare Tkinker       
    master = tk.Tk()
    master.title("Stock Portfolio")    
    top_frame = tk.Frame(master)
    bottom_frame = tk.Frame(master)
    line = tk.Frame(master, height=1, width=500, bg="grey80", relief='groove')

    ### Set Widget details
    program_info = tk.Label(top_frame, text=
                    """Perform earnings and yearly percent calculations \n
                    Please browse for a .csv data file that contains the following columns: \n                   
                    (SYMBOL, NO_SHARES, PURCHASE_PRICE, CURRENT_VALUE, PURCHASE_DATE)""")

    input_path = tk.Label(top_frame, text="Input File Path:")
    input_entry = tk.Entry(top_frame, text="", width=40)
    browse1 = tk.Button(top_frame, text="Browse", command=input)

    output_path = tk.Label(bottom_frame, text="Output File Path:")
    output_entry = tk.Entry(bottom_frame, text="", width=40)
    browse2 = tk.Button(bottom_frame, text="Browse", command=output)

    begin_button = tk.Button(bottom_frame, text='Begin!', command= begin)
    exit_button = tk.Button(bottom_frame, text="Exit", command=master.destroy)

    ### Display Widgets on the program
    top_frame.pack(side=tk.TOP)
    line.pack(pady=10)
    bottom_frame.pack(side=tk.BOTTOM)

    program_info.pack(pady=5)
    input_path.pack(pady=5)
    input_entry.pack(pady=5)
    browse1.pack(pady=5)

    output_path.pack(pady=5)
    output_entry.pack(pady=5)
    browse2.pack(pady=5)

    begin_button.pack(pady=20, fill=tk.X)
    exit_button.pack(pady=20, fill=tk.X)    

    master.mainloop()

if __name__ == "__main__":
    main()
