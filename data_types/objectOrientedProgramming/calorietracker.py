#user add food_logs name,meal_type,calorie,date_time,owner
#oops
#create|add=post
#list:all=>get
#detail=>retrive
#update=>put
#remove=>delete
class Dietlens:
    def __init__(self):
        self.food_logs=[
            {"id":1,"titles":"dosa","calorie":180,"owner":"hari"},
        ]

    def post(self,**kwargs):
        self.food_logs.append(kwargs)
        print("record has been added....")

diet_instance=Dietlens()

diet_instance.post(id=2,name="idly",calorie=170,owner="vipin")
diet_instance.post(id=3,name="dosha",calorie=180,owner="anu")