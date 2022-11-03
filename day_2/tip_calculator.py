#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def tip_calc():
    num_of_people = int(input("How many are splitting the bill?\n"))
    tip = int(input("How much percent tip, 10, 12 15%? \nEnter digits only:\n"))
    total_bill = tip / 100 * cost + cost
    indiv_bill = "{:.2f}".format(total_bill / num_of_people)
    print(f"Total Bill: ${total_bill} \nEach should pay: ${indiv_bill}")

cost = input("How much is the bill?\n")

if cost.startswith('$'):
    cost = int(cost[1:]) #$20
    # print(cost)
    tip_calc()
else:
    cost = int(cost)
    tip_calc()
