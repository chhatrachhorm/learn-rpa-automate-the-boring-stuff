import re

# Testing string
phone = 'Number is 452-563-6325'

# No Grouping
# phone number pattern
noGroup = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# matching regex obj
mo = noGroup.search(phone)
print('Phone found ' + mo.group())

# Grouping with Parenthesis
# phone with group
withGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = withGroup.search(phone)
print('Groups', mo.groups())
for g in mo.groups():
    print(g)

# Matching multiple group with | -
# regex to match either 'Yong' or 'Abg Gila'
r = re.compile(r'Yong|Abg Gila')
mo = r.search('Dk Ong Yong Sim is Abg Gila')
print('Return the first match is', mo.group())

# Optional Matching Group with ?
# regex to match either Batman or Batwoman
r = re.compile(r'Bat(wo)?man')
mo = r.search('The adventure of Batwoman')
print('? found', mo.group())

# Matching Zero or More with *
# regex to match 0 or more => Batman Batwoman Batwowoman ...
r = re.compile(r'Bat(wo)*man')
print('* found', r.search('Batwowowoman').group())

# Matching One or More with +
# regex to match at least 1 => Batwoman Batwowoman ...
r = re.compile(r'Bat(wo)+man')
mo = r.search('Batman')
print('* found none',  mo == None)

# Matching Specific Repetitions with {}
# regex to match HaHaHa not Ha or Ha or HaHaHa
r = re.compile(r'(Ha){3}')
print('{} found HaHaHa', r.search('HaHaHa').group())
# regex to match from 3 to 5 of HaHa
r = re.compile(r'(Ha){3,5}')
print('{} found HaHaHaHa', r.search('HaHaHaHa').group())

# Greedy and Non-Greedy Matching
# Greedy - match the longest string possible
# Non-Greedy - match the shortest string possible

# For Grouping and {} use ? to specify non-greedy
r = re.compile(r'(Ha){3,5}?')
print('Non-Greedy HaHaHaHaHa is', r.search('HaHaHaHaHa').group())
print('Non-Greedy', r.search('HaHa') == None)

# FindAll - return array of string of the matching object
# regex to match phone num
r = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print('Normal Search:', r.search('Cell: 415-555-9999 Work: 212-555-0000').group())
print('FindAll', r.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# If the regex has groups,
# findall will return the array of tuples of string of the matching objects and its group
r = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print('Normal Search:', r.search('Cell: 415-555-9999 Work: 212-555-0000').group(0))
print('FindAll', r.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Character Class
# regex to match one or more numeric followed by a white space
# and followed by one or more letter/digit/underscore
r = re.compile(r'\d+\s\w+')
print('Char', r.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens'))
# to match aeiouAEIOU => [aeiouAEIOU]
# to match not vowel => [^aeiouAEIOU]

# Caret ^ and Dollar $
# ^ match the beginning
# $ match the end
# Wildcard . to match any char except new line `\n`
# (.*) to match every thing (string) - greedy mode
# (.*?) to match every thing (string)- non-greedy mode
# re.compile('.*', re.DOTALL) to match everything includes \n

# to make regex insensitive
# re.compile('insensitive', re.IGNORECASE)
# or re.compile('insensitive', re.I)

# Substitute String with Regex
# \w - no whitespace
r = re.compile(r'Agent \w+')
print('Normal Sub\n', r.sub('Secret', 'Agent Alice gave the secret docs to Agent Bob'))
r = re.compile(r'Agent (\w)\w*')
print('Replace except the first one\n', r.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# Complex Regex
phoneRegex = re.compile(r'''
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)?         # separator
\d{3}
(\s|-|\.)?         # separator
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})? #  extension
''', re.VERBOSE)
# phoneRegex = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)?d{4}(\s*(ext|x|ext.)\s*\d{2,5})?')
print('Phone Num', phoneRegex.search('125-5226 (125)-125.2558'))
