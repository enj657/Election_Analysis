# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC. ")
# else:
#     print("Open the windows. ")

# #What is the score
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A. ')
# else:
#     if score >= 80:
#         print('Your grade is a B. ')
#     else:
#         if score >= 70:
#             print('Your grade is a C. ')
#         else:
#             if score >= 60:
#                 print('Your grade is a D. ')
#             else:
#                 print('Your grade is an F. ')

# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade
# if score >= 90:
#     print('Your grade is an A. ')
# elif score >= 80:
#     print('Your grade is a B. ')
# elif score >= 70:
#     print('Your grade is a C. ')
# elif score >= 60:
#     print('Your grade is a D. ')
# else:
#     print('Your grade is an F. ')

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties. ")
else:
    print("El Paso is not in the list of counties. ")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties. ")
else:
    print("Arapahoe or El Paso in not in the list of counties. ")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties. ")
else:
    print("Arapahoe and El Paso are not in the list of counties. ")


if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties. ")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties. ")


x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")



for county in counties:
    print(county)

for i in range(len(counties)):
        print(counties[i])

print("For loop and dictionaries")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    #print(county + " county has" + str(voters) + " registered voters. ")
    print(f"{county} county has {voters} registered voters. ")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


print("Next part")

for county_dict in voting_data:
    print(county_dict['registered_voters'])


candiate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candiate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candiate_votes / total_votes * 100:.2f}% of the total votes. ")
print(message_to_candidate)