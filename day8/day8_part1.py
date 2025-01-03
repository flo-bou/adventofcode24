# each antenna is tuned to a specific frequency that one char from a-zA-Z0-9
# input is a map of antennas
# the signal applies at specific antinodes based on the resonant frequencies of the antennas
# an antinode occurs at any point that is perfectly in line with two antennas of the same frequency (on the line formed by the 2 antennas). but only when one of the antennas is twice as far away as the other (a node is in the direction of the other antenna but 2 times farther )
# This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them. (for 2 antennas there is 1 pair so 2 nodes; for 3 antennas, there is 3 pairs so 6 nodes; for 4 antennas, there is 6 pairs so 12 nodes; for 5 antennas, there is 10 pairs ...)
# Antennas with different frequencies don't create antinodes; A and a count as different frequencies.
# antinodes can occur at location with antennas
# antinodes out of map don't count
# how many UNIQUE locations in the map countain an antinode.


