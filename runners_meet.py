runner1_speed = 5 #km/h

v1 = runner1_speed*1000/60 #km/h -> m/min
v2 = 5*v1#km/h -> m/min
s1 = 0
s2 = 0

track = 5000 #m
T = 60 #min

def approx(x, y, tol):
    return abs(x-y) < tol

for t in range(T+1):
    s1 = round(v1*t) % track
    s2 = round(v2*t) % track
    if approx(s1, s2, 10**(-8)):
        print(f"The runners meet at {t} minutes on meter {s1} of the track.")
        print(f"Runner 1: {v1*t} m, Runner 2: {v2*t} m\n")
