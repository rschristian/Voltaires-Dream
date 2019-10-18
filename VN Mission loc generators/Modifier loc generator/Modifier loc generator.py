'''
MODIFIER LOC GENERATOR - by Isildur

!! slightly modified version of the mission loc generator !!

Instructions -
-- there are 2 txt files that need inputted text to function - unlocalized_names and localized_names

-- in unlocalized_names, put the unlocalized name for each modifier in code on separate lines e.g:
vn_eng_consolidate_our_rule_mission
vn_eng_fortify_england_mission

-- in localized_names, put the localized name that corresponds to unlocalized ones e.g:
Consolidated Rule
Fortified England

-- once you do this, run this program and copy contents of shell output to your yml file
'''

#modules
import io
import sys

#exits if input files don't exist
try:
    test_file = open("unlocalized_names.txt")
    test_file.close()
except IOError:
    print("Error: File unlocalized_names.txt does not exist!")
    print("Exiting program")
    sys.exit()

try:
    test_file = open("localized_names.txt")
    test_file.close()
except IOError:
    print("Error: File localized_names.txt does not exist!")
    print("Exiting program")
    sys.exit()

#open files
unloc_file = io.open("unlocalized_names.txt", encoding="utf-8")
loc_file = io.open("localized_names.txt", encoding="utf-8")

#check if files are empty
def check_if_empty(unloc_file):
    
    unloc_file.seek(0)
    first_char = unloc_file.read(1)
    if not first_char:
        print("File is empty!")
        print("Please make sure your file has some text in to convert")
        return True
    else:
        unloc_file.seek(0)
        return False
    
def check_if_empty(loc_file):
    
    loc_file.seek(0)
    first_char = loc_file.read(1)
    if not first_char:
        print("File is empty!")
        print("Please make sure your file has some text in to convert")
        return True
    else:
        loc_file.seek(0)
        return False

#output text
def output_text():

    global line_count
    line_num = 0
    while line_num < line_count:
        line_num += 1
        segment1 = unloc_file.readline()
        segment1 = segment1.replace("\n", "")
        segment2 = loc_file.readline()
        segment2 = segment2.replace("\n", "")
        print(" " + segment1 + ': ' + '"' + segment2 + '"')
        print(" " + 'desc_' + segment1 + ': ' + '""')

#for funcs above
emptycheck = check_if_empty(unloc_file)

if emptycheck == True:
    print("Exiting program")
    unloc_file.close()
    loc_file.close()
    sys.exit()
    
emptycheck2 = check_if_empty(unloc_file)

if emptycheck2 == True:
    print("Exiting program")
    unloc_file.close()
    loc_file.close()
    sys.exit()

#determine num of missions
line_count = 0
for line in unloc_file:
    line_count += 1

#reset readline pos to 0
unloc_file.seek(0)

output_text()

#close files
unloc_file.close()
loc_file.close()

#end

