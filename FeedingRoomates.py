def FeedingRoomate1(NumberofMeals,Grams):
    import random
    print("Looks like you will be eating", Numberofmeals, "meals today")
    NumberofMeals = random.randint(2,8)
    
    for i in range (NumberofMeals):
        NumberofMeals -= 1
        Grams = float(input("How many grams was the meal""?"))
        Roomate1 += Grams
    return Roomate1
