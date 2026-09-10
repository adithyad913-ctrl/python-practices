#event add,list,detail,update,delete



class EventWise:


    def __init__(self):

        self.programs =[
            {"id":1,"event":"group song","name":"abi","contact":"3456789","batch":"djangoct","faculty":"anju"},

        ]
    def post(self,**kwargs):

        self.programs.append(kwargs)

        print("record has been created...")

    def get(self):




        if len(self.programs)==0:

            print("no records")

        else:

            for p in self.programs:

                print(p)

    def retrieve(self,id=None):

      programs=[ p for p in self.programs if p.get("id")==id][0] 

      print(programs)

    def put(self,id=None,**kwargs):



        programs=[p for p in self.programs if p.get("id")==id][0]

        programs.update(kwargs)
        print("record has been updated..")
        print(programs)   

    def delete(self,id=None):

        programs=[p for p in self.programs if p.get("id")==id][0]

        self.programs.remove(programs)

        print("deleted..")

        self.get()


        
        
event_instance= EventWise()

event_instance.post(id=2,event="dance",name="avin",contact="456789",batch="django",faculty="sukumar")

#event_instance.get()

#event_instance.retrieve(id=10)

#event_instance.put(id=2,name="avin a.b",contact="567890")

event_instance.delete(id=2)