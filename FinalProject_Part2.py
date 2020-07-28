# Open test_list.p with dictionary of dictionaries (d)

import pickle

filename = "test_lists.p"

in_file = open(filename, "rb")

d_from_file = pickle.load(in_file)

in_file.close()


# Designate domains and score types again

domains = {
    1: "Language",
    2: "Spatial",
    3: "Motor",
    4: "Attention",
    5: "Executive Function"
}

score_types = {
    1: "Standard Score",
    2: "Scaled Score",
    3: "T-Score",
    4: "Z-Score"
}

# Split d_from_file into individual dictionaries again

language = d_from_file[1]
spatial = d_from_file[2]
motor = d_from_file[3]
attention = d_from_file[4]
executive = d_from_file[5]

# Divide dictionaries into 2 lists: list of tests and list of scoretype number codes

language_t = list(language.keys())
language_s = list(language.values())

spatial_t = list(spatial.keys())
spatial_s = list(spatial.values())

motor_t = list(motor.keys())
motor_s = list(motor.values())

attention_t = list(attention.keys())
attention_s = list(attention.values())

executive_t = list(executive.keys())
executive_s = list(executive.values())

# Enter the scores and store it in a list with the score type code. 
# Has to be a list, not a dictionary, because the same pairing may occur multiple times

print("Language")

x = 0
language_scores = []

while x < len(language_s):
    print(language_t[x])
    
    t = language_s[x]
    
    print(score_types[t])
    print()

    s = input("Enter Patient's Score: ")
    s = float(s)
    
    language_scores.append(s)

    x = x + 1

print(language_scores)
print()

print("Spatial")

x = 0

spatial_scores = []

while x < len(spatial_s):
    print(spatial_t[x])
    
    t = spatial_s[x]
    
    print(score_types[t])
    print()

    s = input("Enter Patient's Score: ")
    s = float(s)
    
    spatial_scores.append(s)

    x = x + 1
    
print(spatial_scores)
print()

print("Motor")

x = 0

motor_scores = []

while x < len(motor_s):
    print(motor_t[x])
    
    t = motor_s[x]
    
    print(score_types[t])
    print()

    s = input("Enter Patient's Score: ")
    s = float(s)
    
    motor_scores.append(s)

    x = x + 1
    
print(motor_scores)
print()

print("Attention")

x = 0

attention_scores = []

while x < len(attention_s):
    print(attention_t[x])
    
    t = attention_s[x]
   
    print(score_types[t])
    print()

    s = input("Enter Patient's Score: ")
    s = float(s)

    attention_scores.append(s)

    x = x + 1
    
print(attention_scores)
print()
    
print("Executive")

x = 0

executive_scores = []

while x < len(executive_s):
    print(executive_t[x])
    
    t = executive_s[x]
    
    print(score_types[t])
    print()

    s = input("Enter Patient's Score: ")
    s = float(s)
   
    executive_scores.append(s)

    x = x + 1
    
print(executive_scores)
print()


# Convert all entered scores into a Scaled Score
# For loop based on the list of entered scores for the domain
# Which calculation is performed depends on the list of score type number codes for the domain

print("Language Conversions to Scaled Score")


language_c = []

count = 0


for y in language_scores:
    y = float(y)
    if language_s[count] == 1:
        step = (y-100)/15
        c = (step*3) + 10
    elif language_s[count] == 2:
        c = y
    elif language_s[count] == 3:
        step = (y-50)/10
        c = (step*3) + 10
    elif language_s[count] == 4:
        c = (y*3) + 10

    language_c.append(c)

    count = count + 1
  

print(language_c)
print()

print("Spatial Conversions to Scaled Score")


spatial_c = []

count = 0


for y in spatial_scores:
    y = float(y)
    if spatial_s[count] == 1:
        step = (y-100)/15
        c = (step*3) + 10
    elif spatial_s[count] == 2:
        c = y
    elif spatial_s[count] == 3:
        step = (y-50)/10
        c = (step*3) + 10
    elif spatial_s[count] == 4:
        c = (y*3) + 10

    spatial_c.append(c)

    count = count + 1
  

print(spatial_c)
print()

print("Motor Conversions to Scaled Score")


motor_c = []

count = 0


for y in motor_scores:
    y = float(y)
    if motor_s[count] == 1:
        step = (y-100)/15
        c = (step*3) + 10
    elif motor_s[count] == 2:
        c = y
    elif motor_s[count] == 3:
        step = (y-50)/10
        c = (step*3) + 10
    elif motor_s[count] == 4:
        c = (y*3) + 10

    motor_c.append(c)

    count = count + 1
  

print(motor_c)
print()

print("Attention Conversions to Scaled Score")


attention_c = []

count = 0


for y in attention_scores:
    y = float(y)
    if attention_s[count] == 1:
        step = (y-100)/15
        c = (step*3) + 10
    elif attention_s[count] == 2:
        c = y
    elif attention_s[count] == 3:
        step = (y-50)/10
        c = (step*3) + 10
    elif attention_s[count] == 4:
        c = (y*3) + 10

    attention_c.append(c)

    count = count + 1
  

print(attention_c)
print()

print("Executive Function Conversions to Scaled Score")


executive_c = []

count = 0


for y in executive_scores:
    y = float(y)
    if executive_s[count] == 1:
        step = (y-100)/15
        c = (step*3) + 10
    elif executive_s[count] == 2:
        c = y
    elif executive_s[count] == 3:
        step = (y-50)/10
        c = (step*3) + 10
    elif executive_s[count] == 4:
        c = (y*3) + 10

    executive_c.append(c)

    count = count + 1
  

print(executive_c)
print()

# Create an excel workbook of the results 

import xlsxwriter

workbook = xlsxwriter.Workbook("ScoreConversions.xlsx")
worksheet1 = workbook.add_worksheet("Language")
worksheet2 = workbook.add_worksheet("Spatial")
worksheet3 = workbook.add_worksheet("Motor")
worksheet4 = workbook.add_worksheet("Attention")
worksheet5 = workbook.add_worksheet("Executive Function")

#Create Domain labels with room to fill in data

worksheet1.write(0, 0, "Domain:")
worksheet1.write(0, 1, "Language")

#Create  Labels

worksheet1.write(1, 0, "Tests Administered:")
worksheet1.write(1, 1, "Score Type:")
worksheet1.write(1, 2, "Patient Score:")
worksheet1.write(1, 3, "Converted Scaled Score:")

# Start in next row
row = 2
column = 0

#Fill in data
for a in language_t:
    worksheet1.write(row, column, a)
    row = row + 1

row = 2 
column = 1 

for b in language_s:
    worksheet1.write(row, column, score_types[b])
    row = row + 1

row = 2
column = 2

for c in language_scores:
    worksheet1.write(row, column, c)
    row = row + 1

row = 2
column = 3

for d in language_c:
    worksheet1.write(row, column, d)
    row = row + 1

#Create Domain labels with room to fill in data

worksheet1.write(0, 0, "Domain:")
worksheet1.write(0, 1, "Spatial")

#Create  Labels

worksheet1.write(1, 0, "Tests Administered:")
worksheet1.write(1, 1, "Score Type:")
worksheet1.write(1, 2, "Patient Score:")
worksheet1.write(1, 3, "Converted Scaled Score:")

# Start in next row
row = 2
column = 0

#Fill in data
for a in spatial_t:
    worksheet1.write(row, column, a)
    row = row + 1

row = 2 
column = 1 

for b in spatial_s:
    worksheet1.write(row, column, score_types[b])
    row = row + 1

row = 2
column = 2

for c in spatial_scores:
    worksheet1.write(row, column, c)
    row = row + 1

row = 2
column = 3

for d in spatial_c:
    worksheet1.write(row, column, d)
    row = row + 1    


#Create Domain labels with room to fill in or calculate data

worksheet1.write(0, 0, "Domain:")
worksheet1.write(0, 1, "Motor")

#Create  Labels

worksheet1.write(1, 0, "Tests Administered:")
worksheet1.write(1, 1, "Score Type:")
worksheet1.write(1, 2, "Patient Score:")
worksheet1.write(1, 3, "Converted Scaled Score:")

# Start in next row
row = 2
column = 0

#Fill in data
for a in motor_t:
    worksheet1.write(row, column, a)
    row = row + 1

row = 2 
column = 1 

for b in motor_s:
    worksheet1.write(row, column, score_types[b])
    row = row + 1

row = 2
column = 2

for c in motor_scores:
    worksheet1.write(row, column, c)
    row = row + 1

row = 2
column = 3

for d in motor_c:
    worksheet1.write(row, column, d)
    row = row + 1


#Create Domain labels with room to fill in or calculate data

worksheet1.write(0, 0, "Domain:")
worksheet1.write(0, 1, "Attention")

#Create  Labels

worksheet1.write(1, 0, "Tests Administered:")
worksheet1.write(1, 1, "Score Type:")
worksheet1.write(1, 2, "Patient Score:")
worksheet1.write(1, 3, "Converted Scaled Score:")

# Start in next row
row = 2
column = 0

#Fill in data
for a in attention_t:
    worksheet1.write(row, column, a)
    row = row + 1

row = 2 
column = 1 

for b in attention_s:
    worksheet1.write(row, column, score_types[b])
    row = row + 1

row = 2
column = 2

for c in attention_scores:
    worksheet1.write(row, column, c)
    row = row + 1

row = 2
column = 3

for d in attention_c:
    worksheet1.write(row, column, d)
    row = row + 1


#Create Domain labels with room to fill in or calculate data

worksheet1.write(0, 0, "Domain:")
worksheet1.write(0, 1, "Executive Function")

#Create  Labels

worksheet1.write(1, 0, "Tests Administered:")
worksheet1.write(1, 1, "Score Type:")
worksheet1.write(1, 2, "Patient Score:")
worksheet1.write(1, 3, "Converted Scaled Score:")

# Start in next row
row = 2
column = 0

#Fill in data
for a in executive_t:
    worksheet1.write(row, column, a)
    row = row + 1

row = 2 
column = 1 

for b in executive_s:
    worksheet1.write(row, column, score_types[b])
    row = row + 1

row = 2
column = 2

for c in executive_scores:
    worksheet1.write(row, column, c)
    row = row + 1

row = 2
column = 3

for d in executive_c:
    worksheet1.write(row, column, d)
    row = row + 1

workbook.close()



    





        



 
    




