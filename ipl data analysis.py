
#ipl data analysis program
import pandas as pd
import matplotlib.pyplot as plt
import time

def introduction():
    print("\n\n\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:WELCOME TO MY PROGRAM :-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    print("5\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:(IPL DATA ANALYSIS):-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    msg = '''
        Cricket is one of the most popular game in INDIA. 
	The Indian Premier League (IPL) is a professional Twenty20 cricket league. 
        It is the most-attended cricket league
        In this project we will analyse the dataset of IPL matches played during (2008-2019) 
	using Python Pandas and matplotlib python module for visualization of this dataset. \n\n\n\n'''


    for x in msg:
           print(x, end='')
           time.sleep(0.001)
    wait = input('Press Enter to continue.....')


def made_by():
    msg = ''' 
            IPL Data Analysis made by       : Ishan Bansal
            Roll No                         : 13
            School Name                     : St. Anselm's Pink City School
            session                         : 2021-22
                        
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.001)

    wait = input('Press Enter to continue.....')


def clear():
    for x in range(65):
               print()

def read_csv_file():

    print("Filepath = ","C:/PYTHON CSV/ipl.csv")
    ipl=pd.read_csv("C:/PYTHON CSV/ipl.csv",sep=",",header=0)
    print(ipl)
        
def data_analysis_menu():
    while True:
        ipl=pd.read_csv("C:/PYTHON CSV/ipl.csv",sep=",",header=0)
        df=pd.DataFrame(ipl)
        clear()
        print("\n\n\t\t\t\t\t\t\t________DATA ANALYSIS MENU________\t\t\t\t\t\t\t\n\n")
        print(" CHOICES ")
        print("1. WHOLE DATAFRAME\n")
        
        print("2. TOTAL MATCHES IN A SEASON\n")
        
        print("3. WINNER OF THE SEASON\n")
        
        print("4. BEST PLAYER OF THE MATCH\n")
        
        print("5. MATCHES WIN BY MINIMUM RUN IN THE SEASON\n")
        
        print("6. MATCHES WIN BY MINIMUM WICKET IN THE SEASON\n")
        
        print("7. NO. OF MATCHES WON BY EACH TEAM IN THE SEASON\n")
        
        print("8. NO. OF TIMES EACH TEAM WON THE TOSS\n")
        
        print("9. DATA SUMMARY\n")
        
        print("10. EXIT(To Main menu)\n")
        
        n=int(input("Enter Choice(1-9): "))
        if n==1:
            print("\n\nWHOLE DATAFRAME \n:")
            print(df)

            wait = input('\nPress Enter to continue.....')
        elif n==2:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                matches=dfseason.count()
                print("Total number of matches in",b,"is\n",matches['season'])
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
        elif n==3:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("Winner of",b,"is\n",dfseason['winner'].mode())

            else:
                print("Enter year as given")


            wait = input('\n\nPress Enter to continue.....')
                
        elif n==4:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("Best player of",b,"is :\n",dfseason['player_of_match'].mode())

            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
                
        elif n==5:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print(dfseason.loc[dfseason[dfseason['win_by_runs'].ge(1)].win_by_runs.idxmin()])
            else:
                print("Enter year as given")



            wait = input('\n\nPress Enter to continue.....')
        elif n==6:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print(dfseason.loc[dfseason[dfseason['win_by_wickets'].ge(1)].win_by_wickets.idxmin()])
                              
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
                
        elif n==7:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("No. Of Matches Win by each team in",b,"are\n",dfseason['winner'].value_counts())
                              
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
                    
                
        elif n==8:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("No. Of toss Win by each team in",b,"\n",dfseason['toss_winner'].value_counts())
                   
            else:
                print("Enter year as given")

                wait = input('\n\nPress Enter to continue.....')
                 
        elif n==9:
            print(df.describe())

            wait = input('Press Enter to continue.....')
                
        elif n==10:
            break
        else:
            print("INVALID CHOICE")
                
                
def graph():
    clear()
    print("Work in Progress (Select another choice)")
def main_menu():
    clear()
    introduction()
    made_by()
    while True:
        clear()
        print("\n\n\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:MAIN MENU:-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
        print("ALL CHOICES ")
        print()
        print('1.  Read CSV File\n')
        print('2.  Data Analysis Menu\n')
        print('3.  Graph Menu\n')
        print('4.  Exit\n')
        a = int(input('Enter your choice(1-4) :'))

        if a == 1:
            read_csv_file()
            wait = input('\n\n Press Enter to continue....')

        elif a == 2:
            data_analysis_menu()
            wait = input('\n\n Press Enter to continue....')

        elif a == 3:
            graph()
            wait = input('\n\n Press Enter to continue....')

        elif a == 4:
            print("PROGRAM CLOSED")
            break
                     
        clear()


main_menu()
