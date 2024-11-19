from die import Die

# Create a D6.
die = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analyse the rolls.
occurences = []
for value in range(1, die.num_sides+1):
    occurence = results.count(value)
    occurences.append(occurence)

print(occurences)