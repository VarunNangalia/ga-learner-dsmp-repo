# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
plt.bar(loan_status.index,loan_status)
plt.show()




#Code starts here


# --------------
#Code starts here
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

property_and_loan = property_and_loan=data.groupby(['Property_Area','Loan_Status']).size()
property_and_loan = property_and_loan.unstack()

property_and_loan.plot(kind='bar',stacked=False, figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation =45)
plt.show()


# --------------
#Code starts here
education_and_loan = education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=False, figsize=(15,10))
plt.xlabel("Education")
plt.ylabel("Loan Status")
plt.xticks(rotation =45)
plt.show()



# --------------
#Code starts here
graduate = pd.DataFrame(data[data['Education'] == 'Graduate'])
not_graduate = pd.DataFrame(data[data['Education'] == 'Not Graduate'])

graduate.plot(kind = 'density',label = 'Graduate')
not_graduate.plot(kind = 'density',label = 'Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_2.set(title='Coapplicant Income')


#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_3.set(title='Total Income')


#Code ends here


