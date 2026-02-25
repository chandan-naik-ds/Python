# A dataset has:

# 1200 total rows

# 300 missing rows
# Find the percentage of clean data.

total = 1200
missing = 300

clean = ((total - missing)/total)*100

print("Clean data percentage:",clean)