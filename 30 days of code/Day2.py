mealCost=float(input())
tipPercent=int(input())
taxPercent=int(input())
totalCost=(mealCost*tipPercent/100)+(mealCost*taxPercent/100)+mealCost
print('The total meal cost is {} dollars.'.format(int(round(totalCost))))