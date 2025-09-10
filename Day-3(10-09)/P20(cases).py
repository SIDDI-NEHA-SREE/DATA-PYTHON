'''A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists
 (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and 
 email case may vary (Upper/Lower).
Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.'''


def duplicates(s):
    return set(i.lower().strip() for i in s)
def days3(d1,d2,d3):
    a1=duplicates(d1)
    a2=duplicates(d2)
    a3=duplicates(d3)
    return f"{a1&a2&a3}"

def unique(d1,d2,d3):
    a1=duplicates(d1)
    a2=duplicates(d2)
    a3=duplicates(d3)
    return f"{a1|a2|a3}"



d1=['a@','b@','c@','c@','D@','d@','f@']
d2=['b@','c@','c@','D@','d@','f@']
d3=['a@','b@','c@','c@','D@']
print(f"Day-1- {len(duplicates(d1))}")
print(f"Day-2- {len(duplicates(d2))}")
print(f"Day-3- {len(duplicates(d3))}")
print(f"3-days attendees- {days3(d1,d2,d3)}")
print(f"3-days unique attendees- {unique(d1,d2,d3)}")