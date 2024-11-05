# We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

# 🇨🇴 Colombian pesos
# 🇵🇪 Peruvian soles
# 🇧🇷 Brazilian reais
# Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

# Make sure to Google the current exchange rates!



# The output of the program should look like this:

# What do you have left in pesos? 5600
# What do you have left in soles? 105
# What do you have left in reais? 280
# 413.0

# The sequence should be:

# Currency code example

# Cha-ching! Now you have the total in USD. 💰

# Once you are done, post a screenshot of your code to Twitter by clicking the icon below, and then head over to #CodedexCurrency and review another learner's work. Be supportive! :)

# Write code below 💖

pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

p = pesos * 0.000226
s = soles * 0.26
r = reais * 0.19

total = p + s + r

print(total)
