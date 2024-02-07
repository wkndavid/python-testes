import re


###########################################################################
txt = "The rain in Spain" 'result => The-rain-in-Spain'
x = re.sub("\s", "-", txt)
###########################################################################


###########################################################################
txt = "hello planet"
# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
###########################################################################


###########################################################################
txt = "hello planet"
# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
###########################################################################


###########################################################################
txt = "The rain in Spain falls mainly in the plain!"
# Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
###########################################################################


###########################################################################
txt = "The rain in Spain"
# Check if the string starts with "The" and ends with "Spain":
x = re.search("^The.*Spain$", txt)
###########################################################################


###########################################################################

txt = "88* times before 11:45 *AM"
#Check if the string has any + characters:
x = re.findall("[*]", txt)
###########################################################################


###########################################################################
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
###########################################################################


###########################################################################
REPLACEMENTS = [
    ("BLASTED", "😤"),
    ("Blast", "😤"),
    ("2022-08-24T", ""),
    ("+00:00", ""),
    ("[support_tom]", "Agent "),
    ("[johndoe]", "Client"),
]

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""
for old, new in REPLACEMENTS:
    transcript = transcript.replace(old, new)

print(transcript)
###########################################################################
