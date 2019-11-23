import pandas as pd
import sys


if (len(sys.argv) < 5):
	print('Incorrect number of arguments')
	print('Example Usage: [BofA Filename] [Chase Filename] [Date Start] [Date End]')
	print("(Date Format: MM/DD/YYYY)")
	exit()


bofaFilename = sys.argv[1]
chaseFilename = sys.argv[2]
dateStart = sys.argv[3]
dateEnd = sys.argv[4]

######################################
### Bank of American Transactions ####
######################################

df = pd.read_csv(filepath_or_buffer = bofaFilename)
df = df[df.Status != 'pending']
df['Source'] = 'Bank of America'
df['Category'] = ''
df = df[['Date', 'Source', 'Original Description', 'Category',
       'Amount', 'Amount']]
df = df[(df['Date'] >= dateStart) & (df['Date'] <= dateEnd)]
df = df.rename(columns={"Original Description": "Description"})


######################################
######### Chase Transactions #########
######################################

df2 = pd.read_csv(filepath_or_buffer=chaseFilename,index_col=False)
df2['Source'] = 'Chase'
df2['Category'] = ''
df2 = df2[['Posting Date', 'Source', 'Description', 'Category',
       'Amount', 'Amount']]
df2 = df2.rename(columns={"Posting Date":"Date"},errors="raise")
df2 = df2[(df2['Date'] >= dateStart) & (df2['Date'] <= dateEnd)]


#Combine results
results = pd.concat([df, df2], sort =False)

#Write to CSV
print(results.to_csv())
# results.to_csv(path_or_buf='results.csv')