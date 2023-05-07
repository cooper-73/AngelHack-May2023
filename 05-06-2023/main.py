file = open("input.txt", "r")
friends = {}
time = 0

for idx, line in enumerate(file):
    if idx == 0:
        time = int(line)
        continue
    [name, velocity, duration, rest] = line.split("-")
    friends[name] = {"velocity": int(velocity), "duration": int(duration), "rest": int(rest), "distance": 0}

for friend in friends:
    time_per_step = friends[friend]["duration"] + friends[friend]["rest"]
    friends[friend]["distance"] += friends[friend]["velocity"] * (time // time_per_step) * friends[friend]["duration"]
    time_left = time % (time_per_step)
    time_left = min(time_left, friends[friend]["duration"])
    friends[friend]["distance"] += friends[friend]["velocity"] * time_left

winner, max_distance = "", 0
for friend in friends:
    if max_distance < friends[friend]["distance"]:
        winner = friend
        max_distance = friends[friend]["distance"]
        
print(f"The winner is {winner} who has travelled {max_distance}m")
file.close()