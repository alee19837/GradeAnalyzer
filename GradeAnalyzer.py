#Adam Lee
#24FEB2020
#Grade Analyzer

#Variables/Constants
#Inputname and test scores and wether or not to drop the lowest test score.
sName = input("Name of person who's grade is being calculated: ")
iScore1 = int(input("Test 1: "))
iScore2 = int(input("Test 2: "))
iScore3 = int(input("Test 3: "))
iScore4 = int(input("Test 4: "))

if iScore1 < 0 or iScore2 < 0 or iScore3 < 0 or iScore4 < 0:
    exit(print("Test score must be greater than 0."))
    
sDrop = input("Do you wish to drop the lowest test score?: ")

#Calculations
#Decision/Logical Structures to determine and calculate average and letter grade.
if sDrop == "N" or sDrop == "No" or sDrop == "n" or sDrop == "no":
    fAverage = (iScore1 + iScore2 + iScore3 + iScore4)/4

elif sDrop == "Y" or sDrop == "Yes" or sDrop == "y" or sDrop == "yes":
    if iScore1 < iScore2 and iScore1 < iScore3 and iScore1 < iScore4:
        fAverage = (iScore2 + iScore3 + iScore4)/3
    elif iScore2 < iScore1 and iScore2 < iScore3 and iScore2 < iScore4:
        fAverage = (iScore1 + iScore3 + iScore4)/3
    elif iScore3 < iScore1 and iScore3 < iScore2 and iScore3 < iScore4:
        fAverage = (iScore1 + iScore2 + iScore4)/3
    else: fAverage = (iScore1 + iScore2 + iScore3)/3
else: exit(print("Please choose Yes or No."))

if fAverage >= 97:
    sGrade = "A+"
elif fAverage >= 94:
    sGrade = "A"
elif fAverage >= 90:
    sGrade = "A-"
elif fAverage >= 87:
    sGrade = "B+"
elif fAverage >= 84:
    sGrade = "B"
elif fAverage >= 80:
    sGrade = "B-"
elif fAverage >= 77:
    sGrade = "C+"
elif fAverage >= 74:
    sGrade = "C"
elif fAverage >= 70:
    sGrade = "C-"
elif fAverage >= 67:
    sGrade = "D+"
elif fAverage >= 64:
    sGrade = "D"
elif fAverage >= 60:
    sGrade = "D-"
else:
    sGrade = "F"

#Output to screen to show name, average and letter grade 
print("Hello", sName + ",", "Your test average is: ", format(fAverage,".1f"))
print("Your letter grade for the class is: ", sGrade)
