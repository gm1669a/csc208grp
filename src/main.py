from src.Battle import Battle


with open('SuperpowerDataset.csv') as f:
    data = f.read()

characters = data.split()

wins = {}
losses = {}

for character in characters:
    for other in characters:
        if character == other:
            continue
        if character in wins and other in losses and other in wins[character]:
            wins[character] += 1
        elif character in losses and other in wins and other in losses[character]:
            losses[character] += 1
        else:
            wins[character] = 1
            losses[character] = 1

# print the results
print('wins:', wins)
print('losses:', losses)
