print("Hello World")
#creates/delcares lists-->dynamic can append, remove, update
#python reads lt to rt for index count
counties=["Arapahoe", "Denver", "Jefferson"]
print(counties)
#Append:  and new items to end of list
#ex counties.append("end of list addition")
#Index:  Return numerical location-->
#ex print(countines. index("Arapahoe")) = returns 0
print(counties.index("Arapahoe"))
print(counties[1]) #output value in index position 2
#if index is known-->can use index to change 1
#ex mylist[1]= El Paso
counties[1]="El Paso" 
print(counties)
#change back 
counties[1]="Denver"
print(counties)
#length-->used for looping through an exact amount
print(len(counties))#prints 3 for number included in list not index number
#insert-->used to place value at certain index
#counties.insert(1,"El Paso") (position, "object")
counties.insert(1,"El Paso") #inserts 2nd city unlike append which adds to end
print(counties)
#remove-->from any index postion 
counties.remove("El Paso") #removes most Lt if duplicate
print(counties)
#pop Method
#ex last_value = counties.pop(0)--pops out value at the 0 index
#then assigns right away if need be by assigning to last-value
#slice--> only view items from a certian index to element
# print(counties[0:2])-->brackets start and size value (start at 0 and give 2 items)
# positives start from L, can go from the back using neg-->-1 gives very last value = Jefferson
# create an empty dictionaly
counties_dict = {
                    "Arapahoe": "422829",
                    "Denver": "463353",
                    "Jefferson": "432438"
}
print(counties_dict)# returns key and values
print(len(counties_dict))# returns 3
print(counties_dict.items())# (view object) returns "key:values"
print(counties_dict.keys())# returns keys only
print(counties_dict.values())# returns values only
print(counties_dict.get("Denver"))# returns specific value
#Lists of dictionaries-->same keys associated with different values
#syntax[{key1:value, key2:value2}, {key1:value3, key2:value4}]
# creates empty list
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

#if statements

#1.) creates if statement and provides the condition.
#(==)--> comparison operator, or Boolian operator that means "equal to"
if counties[1] == 'Denver':
    print(counties[1]) #prints Denver if 2nd item in counties list index[1] = Denver

#  If-Else AKA:  dual-alternative decision statement
#   indent very important...make sure if and else are aligned, and underlying statements are consistenly indented
# used when needing an outcome for both true and false conditions
#Ex
#2.) Script that matches flowcharts--> see temperature file

#  Nested If-else--> see Grade

#emodule

#1.) Declare the "my_votes" variable equal to an input funtion-->prompts user to type amount such as 200
#-->how many votes did you get?
#2.) Wrap the input function with the in() method. When using input fx, data type of the user input defaults to a string
#the int() method converts the user input value to an integer--necessary to perform the calc for % of votes
#if we want the user to enter a floating-point decimal number, then we use FLOAT() method
#-->Total votes in the election
#3.) Calculate the % of votes by dividing the users' votes by the total votes, then multiply by 100 using multip. operater (*)
#-->Calculate the % of votes you received
# #4.)  Create a print statement that tells the % of votes. Convert percentage_votes from int to string data type using str(),-->nec in order to print the % of votes in the sentence
# original code my_votes = int(input("How many votes did you get in the election?"))
    #total_votes = int(input("What is the total votes in the election? "))
    #percentage_votes = (my_votes / total_votes) * 100
    #print("I received " + str(percentage_votes)+ "% of the total votes.")
# then changed to f-strings

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the elcection?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# no need to to conver % votes-->more concise. F-string performs calc and formates value as a string
# Membership operators

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
        #1 output-->El Paso is not the list of counties

#  Logical Operators--> allow connection of multiple comparison expressions to create a compound expression
# and, or, not

# combining membership and logical operations to test certain conditions

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
        #2 output-->Arapahoe or Elso is not in the list of counties

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
        #3 Output-->Arapaoe or El Paso is in the list of counties
        #checks if either statement is true

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
    #4 output

    # 2 types of loops: 
        #1.) Condition-controlled loop "DO WHILE" uses T/F condtion to control the number of repeats
            # If true--> perform task
            # statement repeats as long as condidtion is true
        #2.) Count-contrlled loop "DO FOR" repeats for specific number 

#Ex:  Iterate through list of counties
    #Delcare county variable and assign equal to 1st item in lst of counties
        #for strings-->must get length of list as intger for range() function
for i in range(len(counties)):
        #prints 1st item, then 2nd, ...until no more200
    print(counties[i])
#i indicartes index or vales 0,1, &, 2 in the length, of counties list--> i often used for simplicity
#insde range() function--> get length of list of counties --> integer 3
# iterates through list where the variiable i is = to 0 for 1st index
#0 is passed into the print(counties[i]) where i=0 and "Arapahoe" is printed
# processed is continued until all three items, or counties , int the list are printed to the screen

#tuple
# to get output--> 
#Arapahoe
#Denver
#Jefferson
#for i in range (lens(counties_tuple)):
#   print(counties_tuple{i})
# or
# for county in counties_tuple:
#   pring(county)

#iterate through dictionary

#get only keys form dictionary using a for loop

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
#Output= Arapahoe, denver, jefferson

# Keys method to iterate over a diction to get the keys, add the keys() method to the end of the counties, 
# using keys method it doesn't matter what variable name we use in the for loop. 
for county in counties_dict.keys():
    print(county)

# Get the values of a Dictionary

for voters in counties_dict.values():
    print(voters)

# or use this format to get the key
# dictionary_name [key]--> include county in print statemment for for loop
for county in counties_dict:
    print(counties_dict[county])# 

    #get method

for county in counties_dict:
    print(counties_dict.get(county))

#get key value pairs of a dictionary using items()
for key, value in counties_dict.items():
    print(key, value)
#or
for county, voters in counties_dict.items():
    print(county, voters)

#printing each county and registered voter from the counties
#using f-string-->more concise
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#iterate through a list of dictionaries using for loop
#get each dictionary in voting_data-->use the standard format for iterating
#using voting_data list created earlier
for county_dict in voting_data:
    print(county_dict)

#use range() function to iterate over the list
# ex iterating over the list of dictionaries and printing the counties in voting_data

#nested loops
#retrieve only the values form each dictionary in the list of dictionaires
#1.) use for loop to retrieve each dictionary
for county_dict in voting_data:
    #2nd loop.) use the values() method on the variable county_dict to ref the data in 2nd for loop to get each value
    for value in county_dict.values():
        print(value)

# prints only county name for each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#F-strings: Formatted string literals--used in place of concatenation
#edited code above

# multiline f-strings
# creates message to tell a candidate how many votes they won, total number and % of votes received 

candidate_votes = int(input("How many votes did the cadidate get in the election"))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The Total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#formatting f-stirng f'{value:{width}.{precision}}'
## Width specifies # of characters used to dispay the value
## Precsion indicates the # of decimao places to format the value
### ex interest in 2 decimal places= .2f (f means floating decimal)
####can separate thoughsands separator with comma:  f'{value:{width},.{precision}}'
