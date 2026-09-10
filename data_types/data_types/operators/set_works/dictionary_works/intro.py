
daily_calories={
                 "mon":2100,"tue":2200,
                 "wed":1800,"thr":1900,
                 "fri":2100,"sat":2200,
                 "sunday":2500
                }

daily_calories["total_calories"]= sum(daily_calories.values())

print(daily_calories)

set_consumed_calorie=daily_calories["sat"]

print("saturday cal",set_consumed_calorie)

daily_calories["thur"]=1500

print(daily_calories)

#store last week weathe


print("all keys====")

for k in daily_calories.keys():

    print(k)

print("all values")

for v in daily_calories.values():

    print(v)

print("key and values")

for k,v in daily_calories. iteam():

    print(k,v) 


total_calorie=daily_calories.get("tue",0)

print(total_calorie)   


