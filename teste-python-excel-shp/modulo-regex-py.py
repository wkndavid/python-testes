import re

###############################################################
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
###############################################################


###############################################################
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
###############################################################


###############################################################
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
###############################################################


###############################################################
txt = "The rain in Spain"
#Check if the string starts with "The" and ends with "Spain":
x = re.search("^The.*Spain$", txt)
###############################################################