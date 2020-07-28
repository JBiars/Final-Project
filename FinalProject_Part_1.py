
# Designate the Domains and Score types

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

# Building Dictionaries
x = 1

# Language 

language_tests = {}

domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response1 = int(input("Enter: "))
print(response1)
print()

if (response1 > 1):
    print("ERROR!")
    response1 = int(input("Enter: "))
    print(response1)
    print()    
    
while (response1 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()

    language_tests[test] = scoretype

    response1 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response1 > 1):
        print("ERROR!")
        response1 = int(input("Enter: "))
        print(response1)
        print()  
     
print()
print(domain)
print(language_tests)
print()
print()

x += 1


# Spatial

spatial_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response2 = int(input("Enter: "))
print(response2)
print()

if (response2 > 1):
    print("ERROR!")
    response2 = int(input("Enter: "))
    print(response2)
    print()
    
while (response2 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()
    
    spatial_tests[test] = scoretype

    response2 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response2 > 1):
        print("ERROR!")
        response2 = int(input("Enter: "))
        print(response2)
        print()
     
print()
print(domain)
print(spatial_tests)
print()
print()

x += 1

# Motor 

motor_tests = {}

domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response3 = int(input("Enter: "))
print(response3)
print()

if (response3 > 1):
    print("ERROR!")
    response3 = int(input("Enter: "))
    print(response3)
    print()
    
while (response3 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(scoretype)
    print()

    motor_tests[test] = scoretype
    print(score_types[scoretype])
    print()    

    response3 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response3 > 1):
        print("ERROR!")
        response3 = int(input("Enter: "))
        print(response3)
        print()
     
print()
print(domain)
print(motor_tests)
print()
print()

x += 1


# Attention

attention_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response4 = int(input("Enter: "))
print(response4)
print()

if (response4 > 1):
    print("ERROR!")
    response4 = int(input("Enter: "))
    print(response4)
    print()
    
while (response4 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()

    spatial_tests[test] = scoretype

    response4 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response4 > 1):
        print("ERROR!")
        response4 = int(input("Enter: "))
        print(response4)
        print()
     
print()
print(domain)
print(attention_tests)
print()
print()

x += 1

# Executive Function

executive_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response5 = int(input("Enter: "))
print(response5)
print()

if (response5 > 1):
    print("ERROR!")
    response5 = int(input("Enter: "))
    print(response5)
    print()
    
while (response5 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()


    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))

    executive_tests[test] = scoretype
    print(score_types[scoretype])
    print()

    response5 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response5 > 1):
        print("ERROR!")
        response5 = int(input("Enter: "))
        print(response5)
        print()
     
print()
print(domain)
print(executive_tests)
print()
print()

# Allow for more tests to be added

print("Do you need to add any additional tests?")
edits = int(input("Press 1 for yes. Press 0 for no."))
print(edits)
print()

if (edits > 1):
    print("ERROR!")
    edits = int(input("Enter: "))
    print(edits)
    print()

while (edits == 1):
    print("Find the number associated with the domain you wish to edit.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    
    print(domains)
    print()
    edit_domain = int(input("Enter Domain: "))

    if (edit_domain == 1):
        domain = domains[1]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response1 = int(input("Enter: "))
        print(response1)
        print()

        if (response1 > 1):
            print("ERROR!")
            response1 = int(input("Enter: "))
            print(response1)
            print()
    
        while (response1 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()

            language_tests[test] = scoretype

            response1 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response5 > 1):
                print("ERROR!")
                response5 = int(input("Enter: "))
                print(response5)
                print()
     
        print()
        print(domain)
        print(language_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 2):
        domain = domains[2]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response2 = int(input("Enter: "))
        print(response2)
        print()

        if (response2 > 1):
            print("ERROR!")
            response2 = int(input("Enter: "))
            print(response2)
            print()
    
        while (response2 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()
    
            spatial_tests[test] = scoretype

            response2 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response2 > 1):
                print("ERROR!")
                response2 = int(input("Enter: "))
                print(response2)
                print()
     
        print()
        print(domain)
        print(spatial_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 3):
        domain = domains[3]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response3 = int(input("Enter: "))
        print(response3)
        print()

        if (response3 > 1):
            print("ERROR!")
            response3 = int(input("Enter: "))
            print(response3)
            print()
    
        while (response3 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(scoretype)
            print()

            motor_tests[test] = scoretype
            print(score_types[scoretype])
            print()    

            response3 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response3 > 1):
                print("ERROR!")
                response3 = int(input("Enter: "))
                print(response3)
                print()
     
        print()
        print(domain)
        print(motor_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 4):
        domain = domains[4]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response4 = int(input("Enter: "))
        print(response4)
        print()

        if (response4 > 1):
            print("ERROR!")
            response4 = int(input("Enter: "))
            print(response4)
            print()
    
        while (response4 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()

            spatial_tests[test] = scoretype

            response4 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response4 > 1):
                print("ERROR!")
                response4 = int(input("Enter: "))
                print(response4)
                print()
     
        print()
        print(domain)
        print(attention_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 5):    
        domain = domains[5]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response5 = int(input("Enter: "))
        print(response5)
        print()

        if (response5 > 1):
            print("ERROR!")
            response5 = int(input("Enter: "))
            print(response5)
            print()
    
        while (response5 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()


            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))

            executive_tests[test] = scoretype
            print(score_types[scoretype])
            print()

            response5 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response5 > 1):
                print("ERROR!")
                response5 = int(input("Enter: "))
                print(response5)
                print()
     
        print()
        print(domain)
        print(executive_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    else:
        print("ERROR!")
        print()
        print("Find the number associated with the domain you wish to edit.")
        print("You will enter the NUMBER below. Not the name.")
        print()
    
        print(domains)
        print()
        edit_domain = int(input("Enter Domain: "))

print("Test Entry Complete.")

# Make new dict
d = {
    1: language_tests,
    2: spatial_tests,
    3: motor_tests,
    4: attention_tests,
    5: executive_tests
}
print(d)

# save dict in pickle format as test_lists.p
import pickle

filename = "test_lists.p"

outfile = open(filename, "wb")

pickle.dump(d, outfile)

outfile.close()
    

        