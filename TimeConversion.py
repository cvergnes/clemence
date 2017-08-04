import sys

def timeConversion(s):
    ampm=s[-2:]
    hour=s[0:2]
    minsec=s[2:-2]
    if (ampm == "AM" and hour != "12") or (ampm == "PM" and hour == "12") :
        return hour + minsec
    elif ampm == "AM" :
        return "00" + minsec
    else:
        return str(int(hour)+12) + minsec
    
s = "12:05:00AM"
print s + " " + timeConversion(s)