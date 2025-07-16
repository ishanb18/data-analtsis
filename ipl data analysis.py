
#ipl data analysis program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_file='matchanalysis.csv'

def introduction():
    print("\n\n\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:WELCOME TO MY PROGRAM :-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    print("\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:(IPL DATA ANALYSIS):-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    msg = '''
        Cricket is one of the most popular game in INDIA. 
	The Indian Premier League (IPL) is a professional Twenty20 cricket league. 
        It is the most-attended cricket league
        In this project we will analyse the dataset of IPL matches played during (2008-2019) 
	using Python Pandas and matplotlib python module for visualization of this dataset. \n\n\n\n'''

    print(msg, end='')
    wait = input('\t\t\t\t\tPress Enter to continue.....')


def made_by():
    msg = ''' 
            IPL Data Analysis made by       : Ishan Bansal & Utkarsh Jain
            Roll No                         : 13 & 52
            School Name                     : St. Anselm's Pink City School
            session                         : 2021-22
                        
            \n\n\n
        '''


    print(msg, end='')

    wait = input('\t\t\t\tPress Enter to continue.....')


def clear():
    for x in range(5):
               print()

def read_csv_file():

    ipl=pd.read_csv(csv_file,sep=",",header=0)
    ipl.drop(ipl.columns[ipl.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    print(ipl)
        
def data_analysis_menu():
    while True:
        ipl=pd.read_csv(csv_file,sep=",",header=0)
        df=pd.DataFrame(ipl)
        clear()
        print("\n\n\t\t\t\t\t\t\t________DATA ANALYSIS MENU________\t\t\t\t\t\t\t\n\n")
        print(" CHOICES ")
        print("1. WHOLE DATAFRAME\n")

        print('2. DISPLAY COLUMNS\n')
        
        print('3. DISPLAY TOP ROWS\n')
        
        print('4. DISPLAY BOTTOM ROWS\n')
        
        print('5. DISPLAY SPECIFIC COLUMN\n')
        
        print('6. ADD A NEW RECORD\n')
        
        print('7. ADD A NEW COLUMN\n')
        
        print('8. DELETE A COLUMN\n')
        
        print('9. DELETE A RECORD\n')
        
        print("10. TOTAL MATCHES IN A SEASON\n")
        
        print("11. WINNER OF THE SEASON\n")
        
        print("12. BEST PLAYER OF THE MATCH\n")

        print("13. MATCH WIN BY MAXIMUM RUNS\n")
        
        print("14. MATCHES WIN BY MINIMUM RUN IN THE SEASON\n")

        print("15. MATCH WIN BY MAXIMUM WICKETS\n")
        
        print("16. MATCHES WIN BY MINIMUM WICKET IN THE SEASON\n")
        
        print("17. NO. OF MATCHES WON BY EACH TEAM IN THE SEASON\n")
        
        print("18. NO. OF TIMES EACH TEAM WON THE TOSS\n")
        
        print("19. DATA SUMMARY\n")
        
        print("20. EXIT(To Main menu)\n")
        
        n=int(input("Enter Choice(1-20): "))
        if n==1:
            print("\n\nWHOLE DATAFRAME \n:")
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df)

            wait = input('\nPress Enter to continue.....')

        elif n == 2:
            print(df.columns)
            wait = input('\n\n\n Press any key to continuee.....')

        if n == 3:
            n = int(input('Enter Total rows you want to show :'))
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df.head(n))
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif n == 4:
            n = int(input('Enter Total rows you want to show :'))
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df.tail(n))
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif n == 5:
            print(df.columns)
            col_name = input('Enter Column Name that You want to print : ')
            print(df[col_name])
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif n == 6:
            a = input('Enter Match ID :')
            b = input('Enter IPL season :')
            c = input('Enter City Name :')
            d = input('Enter Match date :')
            e = input('Enter Team 1 Name  :')
            f = input('Enter Team 2 Name :')
            g = input('Enter Toss Winner :')
            h = input('Enter Toss Decision :')
            i = input('Enter Result (Normal /tie/ DL ) :')
            j = input('Enter Duckwoth Lewis Method applied (0 for No, 1 for Yes ) :) :')
            k = input('Enter Winner Team :')
            l = input('Enter Win By runs :')
            m = input('Enter Win By Wickets :')
            n = input('Enter Man of the Match Player :')
            o = input('Enter venue : ')
            data = {'id': a, 'season': b, 'city': c,'date': d, 'team1': e, 'team2': f, 'toss_winner': g,'toss_decision':h,'result':i,'dl_applied':j,'winner':k,'win_by_runs':l,'win_by_wickets':m,'player_of_match':n,'venue':o}
            df = df.append(data, ignore_index=True)
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df)
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif n == 7:
            col_name = input('Enter new column name :')
            col_value = input('Enter default column value :')
            df[col_name] = col_value
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df)
            wait = input('\n\n\n Press any key to continuee.....')

        elif n == 8:
            col_name = input('Enter column Name to delete :')
            del df[col_name]
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df)
            wait = input('\n\n\n Press any key to continuee.....')

        elif n == 9:
            index_no = int(input('Enter the Index Number that You want to delete :'))
            df = df.drop(df.index[index_no])
            df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
            print(df)
            wait = input('\n\n\n Press any key to continuee.....')
            
        elif n==10:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                matches=dfseason.count()
                print("Total number of matches in",b,"is\n",matches['season'])
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
            
        elif n==11:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("Winner of",b,"is\n",dfseason['winner'].mode())

            else:
                print("Enter year as given")


            wait = input('\n\nPress Enter to continue.....')
                
        elif n==12:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("Best player of",b,"is :\n",dfseason['player_of_match'].mode())

            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')

        elif n==13:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
                print(dfseason.loc[dfseason[dfseason['win_by_runs'].ge(1)].win_by_runs.idxmax()])
            else:
                print("Enter year as given")



            wait = input('\n\nPress Enter to continue.....')
                
        elif n==14:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
                print(dfseason.loc[dfseason[dfseason['win_by_runs'].ge(1)].win_by_runs.idxmin()])
            else:
                print("Enter year as given")



            wait = input('\n\nPress Enter to continue.....')

        elif n== 15:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
                print(dfseason.loc[dfseason[dfseason['win_by_wickets'].ge(1)].win_by_wickets.idxmax()])

            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
            
        elif n==16:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
                print(dfseason.loc[dfseason[dfseason['win_by_wickets'].ge(1)].win_by_wickets.idxmin()])
                              
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
                
        elif n==17:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
                print("No. Of Matches Win by each team in",b,"are\n",dfseason['winner'].value_counts())
                              
            else:
                print("Enter year as given")

            wait = input('\n\nPress Enter to continue.....')
                    
                
        elif n==18:
            b=int(input("Enter Year you want to see(2008 - 2019):"))
            if b == 2008 or b == 2009 or b == 2010 or b == 2011 or b == 2012 or b == 2013 or b == 2014 or b == 2015 or b == 2016 or b == 2017 or b == 2018 or b == 2019:
                dfseason = df[df['season'] == b]
                print("No. Of toss Win by each team in",b,"\n",dfseason['toss_winner'].value_counts())

                wait = input('\n\nPress Enter to continue.....')
                
                   
            else:
                print("Enter year as given")

                wait = input('\n\nPress Enter to continue.....')

                 
        elif n==19:
            print(df.describe())

            wait = input('Press Enter to continue.....')
                
        elif n==20:
            break
        else:
            print("INVALID CHOICE")
                
                
def graph():
    clear()
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\t\t\t\tGRAPH MENU ')
        print('_'*80)
        print('\n1. Season wise Matches - Line Graph')
        print('\n2. Season wise Matches - Bar Graph')
        print('\n3. Season wise Matches - Horizontal Bar Graph')
        print('\n4. Most Successful Team - Bar Graph')
        print('\n5. Match played by each Team - Line Graph')
        print('\n6. Match played by each Team - Bar Graph')
        print('\n7. No. of matches per venue - Line Graph')
        print('\n8. No. of matches per venue - Bar Graph')
        print('\n9. No. of matches per venue - Bar Horizontal Graph')
        print('\n10. No. of toss win by each team - Line Graph')
        print('\n11. No. of toss win by each team - Bar Graph')
        print('\n12. No. of toss win by each team - Bar Horizontal Graph')
        print('\n13. No. of times which Toss decision is taken - Bar Graph')
        print('\n14. Match result - PIE CHART')
        print('\n15. no. of player became player of the match- HISTOGRAM')
        print('\n16.  Exit (Move to Main Menu)\n')
        ch = int(input('Enter Your Choice(1-16):'))

        if ch == 1:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        elif ch == 2:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            
        elif ch == 3:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()
           

        elif ch == 4:
            g = df.groupby('winner')
            x = df['winner'].unique()
            y = g['winner'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('winner')
            plt.ylabel('Matches')
            plt.title('Most Successful Team')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()


        elif ch ==5:
            x = df['team1'].value_counts()
            y = df['team2'].value_counts()
            plt.title('Match playes by each team')
            plt.xlabel('teams')
            plt.ylabel('Matches')
            (x+y).plot(kind='line')
            plt.show()

        elif ch ==6:
            x = df['team1'].value_counts()
            y = df['team2'].value_counts()
            plt.title('Match playes by each team')
            plt.ylabel('teams')
            plt.xlabel('Matches')
            (x+y).plot(kind='barh')
            plt.show()

        elif ch == 7:
            g = df.groupby('venue')
            x = df['venue'].unique()
            y = g['venue'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('venue')
            plt.ylabel('Matches')
            plt.title('No. of matches per venue')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        elif ch == 8:
            g = df.groupby('venue')
            x = df['venue'].unique()
            y = g['venue'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('venue')
            plt.ylabel('Matches')
            plt.title('No. of matches per venue')
            plt.grid(True)
            plt.bar(x, y)
            plt.show()

        elif ch == 9:
            g = df.groupby('venue')
            x = df['venue'].unique()
            y = g['venue'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('matches')
            plt.ylabel('venue')
            plt.title('No. of matches per venue')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()

        elif ch == 10:
            g = df.groupby('toss_winner')
            x = df['toss_winner'].unique()
            y = g['toss_winner'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('toss_winner')
            plt.ylabel('Matches')
            plt.title('No. of Toss Win by each team')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        elif ch == 11:
            g = df.groupby('toss_winner')
            x = df['toss_winner'].unique()
            y = g['toss_winner'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('toss_winner')
            plt.ylabel('Matches')
            plt.title('No. of Toss Win by each team')
            plt.grid(True)
            plt.bar(x, y)
            plt.show()

        elif ch == 12:
            g = df.groupby('toss_winner')
            x = df['toss_winner'].unique()
            y = g['toss_winner'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('Matches')
            plt.ylabel('toss_winner')
            plt.title('No. of Toss Win by each team')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()

        elif ch == 13:
            g = df.groupby('toss_decision')
            x = df['toss_decision'].unique()
            y = g['toss_decision'].count()
            plt.xticks(rotation='vertical')
            plt.xlabel('Toss decision')
            plt.ylabel('matches')
            plt.title('No. of times which toss decision is taken')
            plt.grid(True)
            plt.bar(x, y)
            plt.show()

        elif ch == 14:
            g = df.groupby('result')
            x = df['result'].unique()
            y = g['result'].count()
            exp=[0.4,0.4,0.6]
            c=['blue','red','green']
            s=pd.Series(y,index=['normal','tie','no result'])
            plt.title('Match Result')
            plt.grid(True)
            s.plot(kind = 'pie',y=y,explode = exp,autopct='%.2f',colors=c)
            plt.show()



        elif ch == 15:
            g = df.groupby('player_of_match')
            x = df['player_of_match'].unique()
            y = g['player_of_match'].count()
            s=pd.Series(y)
            plt.title('no. of player became player of the match')
            plt.xlabel('No. of player')
            plt.grid(True)
            s.plot(kind = 'hist')
            plt.show()

            
        elif ch ==16:
            break
        else:
            print("Enter Valid choice")

            wait=input("\n\nPress Enter to Continue......")
    
def main_menu():
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
