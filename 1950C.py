t = int(input())
for _ in range(t):
    s = input()

    s1 = "hh:mm"
    
    if s[:2] == "00":
        s1 = f"{12}{s[2:]} AM"
    elif s[:2] == "12":
        s1 = f"{12}{s[2:]} PM"
    elif int(s[:2]) < 12:
        s1 = f"{s} AM"
    elif int(s[:2]) > 12:
        hrs = int(s[:2]) - 12
        s1 = f"{hrs:02}{s[2:]} PM" 

    print(s1)
