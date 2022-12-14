# -*- coding: utf-8 -*-
"""assignment09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FuYk0uIoOJ8TmTlvvel78qa7jhPb97z8

# SF Salaries Exercise
"""

#            ____  _____  ______ _      _____            _    _ __  __          _   _            _    _ __  __ ______ _____             ____  _____  ______ _      _____          _____ __  __
#      /\   |  _ \|  __ \|  ____| |    |  __ \     /\   | |  | |  \/  |   /\   | \ | |     /\   | |  | |  \/  |  ____|  __ \      /\   |  _ \|  __ \|  ____| |    |  __ \   /\   |_   _|  \/  |
#     /  \  | |_) | |  | | |__  | |    | |__) |   /  \  | |__| | \  / |  /  \  |  \| |    /  \  | |__| | \  / | |__  | |  | |    /  \  | |_) | |  | | |__  | |    | |  | | /  \    | | | \  / |
#    / /\ \ |  _ <| |  | |  __| | |    |  _  /   / /\ \ |  __  | |\/| | / /\ \ | . ` |   / /\ \ |  __  | |\/| |  __| | |  | |   / /\ \ |  _ <| |  | |  __| | |    | |  | |/ /\ \   | | | |\/| |
#   / ____ \| |_) | |__| | |____| |____| | \ \  / ____ \| |  | | |  | |/ ____ \| |\  |  / ____ \| |  | | |  | | |____| |__| |  / ____ \| |_) | |__| | |____| |____| |__| / ____ \ _| |_| |  | |
#  /_/    \_\____/|_____/|______|______|_|  \_\/_/    \_\_|  |_|_|  |_/_/    \_\_| \_| /_/    \_\_|  |_|_|  |_|______|_____/  /_/    \_\____/|_____/|______|______|_____/_/    \_\_____|_|  |_|

import pandas as pd

"""** Import pandas as pd.**"""

sal =pd.DataFrame(pd.read_csv('Salaries.csv'))
sal

"""** Read Salaries.csv as a dataframe called sal.**"""

sal.head()

"""** Check the head of the DataFrame. **"""



"""** Use the .info() method to find out how many entries there are.**"""



sal.info()

"""**What is the average BasePay ?**"""

sal['BasePay'].mean()



"""** What is the highest amount of OvertimePay in the dataset ? **"""

sal['OvertimePay'].max()

"""** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **"""

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']



"""** How much does JOSEPH DRISCOLL make (including benefits)? **"""

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']



"""** What is the name of highest paid person (including benefits)?**"""

# sal0 = sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
name= str(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName'])
name0=''
for i in range(len(name)):
  if name[i].isdigit() == False and name[i] != ' ' :
    name0=name0 + name[i]
print('Name: ',name0)



"""** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**"""

nameLow = str(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName'])
name1 = ''
for i in range(len(nameLow)):
  if nameLow[i].isdigit() == False and nameLow[i] != ' ' :
    name1=name1 + nameLow[i]
print('Name: ',name1)
print('It\'s negative?')



"""** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **"""

sal.groupby('Year').mean()['BasePay']



"""** How many unique job titles are there? **"""

salUn = sal['JobTitle'].unique()
print(len(salUn))



"""** What are the top 5 most common jobs? **"""

sal['JobTitle'].value_counts().head(5)



"""** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **"""

sal2013 = sal[sal['Year']==2013]['JobTitle'].value_counts()==1
print(sal2013.sum())



"""** How many people have the word Chief in their job title? (This is pretty tricky) **"""

sal['JobTitle'].apply(lambda str:('Chief' in str)).sum()



"""** Bonus: Is there a correlation between length of the Job Title string and Salary? **"""

print(len(sal['JobTitle']))
print(sal['TotalPayBenefits'].sum())
JobTitle = len(sal['JobTitle'])
TotalPayBenefits = sal['TotalPayBenefits'].sum()
data = {'title_len':[JobTitle/JobTitle , JobTitle/TotalPayBenefits],
        'TotalPayBenefits': [TotalPayBenefits/JobTitle,TotalPayBenefits/TotalPayBenefits]}
df = pd.DataFrame(data,index = ['title_len',' TotalPayBenefits'])
df

sal["title_len"] = sal["JobTitle"].apply(len) 
df = sal[["title_len" , "TotalPayBenefits"]] 
df
df.corr()



"""# Great Job!"""