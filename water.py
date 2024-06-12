import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

def menu():
    print("*********************************************************************")
    print("          Water Availability For Drinking Project  ")
    print("*********************************************************************")
    print()
    print()
    print("          Data Analysis                ")
    print("1. Reading file without index")
    print("2. Reading files with new column names")
    print()
    print()
    print("          Data Visualuzation           ")
    print("3. Line Plot")
    print("4. Bar Plot")
    print()
    print()
    print("          Data Manipulation             ")
    print("5. Reading few records")
    print("6. Read 3 records from top and 2 from bottom from file")
    print("7. Duplicate file with new name")
    print("8. Read with specific columns")
    print("9. Create csv file with data frame")
    print("10. Read csv file")
    print("11. Find maximum Availability of Drinking Water(%)  ")
    print("12. Create detailemp file with data")
    print("13. Modifying Availability of Drinking Water(%) 63.33 with NaN value")
    print()
    print()
    print("*********************************************************************")
    
menu()
def no_index():
    df=pd.read_csv("R:\Rahul\\Table.csv.csv",index_col=0)
    print("Without index")
    print(df)
def new_colname():
    df=pd.read_csv("R:\Rahul\\Table1.csv",skiprows=1,names=['States','AvailabilityofDrinkingWater(%)','Source of Drinking Water(%)- Well','Source of Drinking Water (%)- Tap','Source of Drinking Water (%)- Others'])
    print(df)
def line_plot():
    print('Line Plot')
    df=pd.read_csv("R:\\Rahul\\Table.csv.csv")
    x=df["States"]
    y=df["AvailabilityofDrinkingWater(%)"]
    plt.plot(x,y,color='red',linewidth=5)
    plt.xlabel("States")    
    plt.ylabel("AvailabilityofDrinkingWater(%)")
    plt.title("Water Availability")
    plt.show()
    
def bar_plot():
    print("bar_plot")
    df=pd.read_csv("R:\Rahul\\Table.csv.csv")
    x=df["States"]
    y=df["AvailabilityofDrinkingWater(%)"]
    plt.title("Water Availability")
    plt.bar(x,y)
    plt.show()
def read_rows():
    df=pd.read_csv("R:\Rahul\\Rahul.csv",nrows=3)
    print(df)
def top_bottom():
    df=pd.read_csv("R:\Rahul\\Rahul.csv")
    #print(df)
    print("top 3 rows")
    print(df.head(3))
    print()
    print()
    print("last 2 rows")
    print(df.tail(2))
def dup():
    print("duplicate file with new name as Rahulnew.csv")
    df=pd.read_csv("R:\Rahul\\Rahul.csv")
    df.to_csv("Rahulnew.csv")
    print(df)
def spec_col():
    df=pd.read_csv("R:\\Rahul\\Table.csv.csv",usecols=["States","AvailabilityofDrinkingWater(%)","Source of Drinking Water (%)- Well"])
    print(df)
def create_file():
    student={'New Employee':[110,111,112,113,114],'Name':['Sunil','Amit','Umar','Ajay','Ravi']}
    df1=pd.DataFrame(student)
    print(df1)
    df1.to_csv("R:\Rahul\\Rahul.csv")
def csv():
    print("Reading file water")
    df=pd.read_csv("R:\Rahul\\Table.csv.csv")
    print(df)
def maxdrinkingwater():
    df3=pd.read_csv("R:\\Rahul\\Table.csv.csv")
    print(df3)
    print("Highest Availability of Drinking Water(%)")
    print(df3['AvailabilityofDrinkingWater(%)'].max())
    
def create_detailemp():
    employee={'First name':['Rakesh','Raman','Arvind','Junaid'],'Last name':['Kumar','Jain','Gupta','Uddain'],'Father Name':['S.K.Kumar','Rajinder Jain','Ravinder Gupta','Jalauddin']}
    df2=pd.DataFrame(employee)
    print(df2)
    df2.to_csv("R:\Rahul\\Rahul.csv")
def salNaN():
    df=pd.read_csv("R:\Rahul\\Table.csv.csv",na_values=[63.33])
    print(df)

    
opt=' '
opt=int(input('Enter your choice:'))


if(opt==1):
    no_index()
elif(opt==2):
    new_colname()
elif opt==3:
    line_plot()
elif opt==4:
    bar_plot()
elif opt==5:
    read_rows()
elif opt==6:
    top_bottom()
elif opt==7:
    dup()
elif opt==8:
    spec_col()
elif opt==9:
    create_file()
elif opt==10:
    csv()
elif opt==11:
    maxdrinkingwater()
elif opt==12:
    create_detailemp()
elif opt==13:
    salNaN()
else:
    print("invalid option")
