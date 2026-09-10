# 1. Remove spaces
names = [" John "," Alice "," Bob","Emma"]
trimmed = [n.strip() for n in names]   # ['John','Alice','Bob','Emma']
print(trimmed)
# 2. Capitalize
names = ["john","alice","bob","emma"]
capitalized = [n.capitalize() for n in names]   # ['John','Alice','Bob','Emma']
print(capitalized)

# 3. First character
words = ["Python","Java","Django","React"]
first_chars = [w[0] for w in words]   # ['P','J','D','R']
print(first_chars)
# 4. Add ".com"
sites = ["google","amazon","github","openai"]
websites = [s+".com" for s in sites]   # ['google.com','amazon.com','github.com','openai.com']
print(websites)

# 5. Replace spaces with underscores
courses = ["Python Basics","Learn Django","React Course"]
underscored = [c.replace(" ","_") for c in courses]   # ['Python_Basics','Learn_Django','React_Course']
print(underscored)
