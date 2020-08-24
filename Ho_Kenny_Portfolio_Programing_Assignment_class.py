
'''

    Author:          Kenny Ho
    ICT 4370:        Python Programming
    Date Written:    August 19, 2020
    Description:     Week 10: Portfolio Programming Assignment:
                        Improving the Stock problem with Additional Functionality

'''

import tkinter as tk
import pandas as pd
import sys
import os
from tkinter import Tk, Label, Button, Entry, filedialog
from datetime import date, datetime      

class Purchases:
    """
        Set Purchase info with stock symbol, number of shares, 
            purchase price, current price, purchase date
    """
    def __init__(self, symbol, no_shares, p_price, c_price, p_date):
        self.symbol = symbol
        self.no_shares = no_shares
        self.p_price = p_price
        self.c_price = c_price
        self.p_date = p_date
 
    def earnings(self):
        """
            Calculate gain/loss (Earnings)
            Equation: (current price - purchase price ) x number of shares
        """
        earnings = round((self.c_price - self.p_price ) * self.no_shares, 2)
        return earnings
    
    def yearly_percent(self):
        """
            Calculate Percent Earnings
                Equation: (current price - purchace price)/purchase price x 100
            Calculate Yearly Percent
                Equation: (gain/loss percentage) / ((curent date- purchase date)/365)
        """
        today = datetime.now().replace(minute=0, hour=0, second=0, microsecond=0)
        day_diff = (today-self.p_date)
        year_diff = day_diff.dt.days.astype('int16')/365

        percent_earnings = ((self.c_price - self.p_price) / self.p_price) * 100
        yearly_percent = round((percent_earnings / year_diff), 2)
        return yearly_percent

class MainApplication:
    
    def __init__(self, stock_file, output_file_path):
        self.stock_file = stock_file
        self.output_file_path = output_file_path

    def run(data_file, output_file_path):
        try:
            """
                #1: Open CSV file into pandas, parse date for "purchase_date"
                #2: Remove unnamed columns
                #3: Add CSV data based on column index into stock_bond_class
                #4: Add New column "EARNINGS" with calculations from stock_bond_class
                #5: Add New column "YEARLY_PERCENT" with calculations from stock_bond_class
                #6: Save Changes to CSV file
                #7: ### Uncomment to view data on commandline
                #8: Confimration Process completed.
                Error checking enabled:
                    1.  Check for Missing files
                    2.  Check for input errors. (String instead of Interger)
                    3.  Any errors, Report problem.
            """

            stock_df = pd.read_csv(data_file, sep=",", parse_dates=[4])                 #1
            stock_df = stock_df.loc[:, ~stock_df.columns.str.contains('^Unnamed')]      #2

            stock_add = Purchases(                                                      #3
            symbol=stock_df.loc[:,"SYMBOL"],
            no_shares= stock_df.loc[:,"NO_SHARES"],
            p_price= stock_df.loc[:,"PURCHASE_PRICE"],
            c_price= stock_df.loc[:,"CURRENT_VALUE"],
            p_date= stock_df.loc[:,"PURCHASE_DATE"]
            )

            stock_df["EARNINGS"] = stock_add.earnings()                                 #4
            stock_df["YEARLY_PERCENT"] = stock_add.yearly_percent()                     #5
            stock_df.to_csv(output_file_path, index=False)                              #6

            print(stock_df)                                                             #7
            print("\n", data_file, "have been processed. \n"                            #8
                "Please view:", output_file_path, "for the results \n") 
        except FileNotFoundError:
            print(data_file, "File was not found...")
            raise
        except TypeError :
            print("Input error in csv file. Please check if string and integer are correct")
            raise
        except Exception as e:
            print("Something went wrong with the CSV file. Please check your data.")
            raise
