def paperwork(n, m):
    if n <=0 or m <= 0:
        return 0
    else: return n * m

def make_upper_case(s):
    return s. upper()

def past(h, m, s):
    return (h* 3600 + m * 60 + s)*1000

def are_you_playing_banjo(name):
    if name[0]== "r" or name[0]=="R":
        return name +" " +  "plays banjo"
    else: return name + " " +  "does not play banjo"    