import pandas as pd


# Used Pandas to retrieve data from table in html rather than BeautifulSoup
# First table of Orbital crewed spaceship
df1 = (pd.read_html('https://en.wikipedia.org/wiki/Comparison_of_crewed_space_vehicles'))[0]
df1.head()

# Gets first row as a list to use as new header
header_1 = df1.iloc[0]
header_1

# Reset df to drop first row with header names
df1 = df1[1:]
df1.head()

df1.rename(columns=header_1, inplace=True)
df1.head()

# Add orbital type that separates table subjects
df1['Orbit'] = "Orbital"

# Second table of Sub-orbital crewed spaceship
df2 = (pd.read_html('https://en.wikipedia.org/wiki/Comparison_of_crewed_space_vehicles'))[0]
df2.head()

df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
df2.head()

df2['Orbit'] = "Sub-Orbital"

# See which columns can be joined on
list(df1.columns)

# See which columns can be joined on
list(df2.columns)

df3 = df1.merge(df2,how='outer')
df3

# Extract only US ships
# for each in ship_df:
#     if each.Origin = 'USA':
#         each
ship_df = df3[df3.Origin == 'USA']
ship_df.head()

def test_db1():
    # Rename Launchsytem, Crewsize, Powersystem, Payloadto/from ISS (kg), Firstspaceflight*, Lastspaceflight, Flights* fields
    ship_df = ship_df.rename(columns={"Launchsystem":"Launch System", "Crewsize":"Crew Size", "Powersystem":"Power System", "Payloadto/from ISS (kg)":"Payload to/from ISS (kg)", "Firstspaceflight*":"First Space Flight","Lastspaceflight":"Last Space Flight", "Flights*":"Flights"})
    ship_df

# Reset index
test = ship_df.reset_index(drop=True)
test

# Remove square bracketed notes from dataset
# for row in df3:
#     for each in row:
        
# tester = "1961 (1960)"
# tester.replace("[*]", "",regex=True)
# tester
# Remove parentheses notes/dates implying unmanned notes
# test = ship_df.replace("(*)", "")
# test