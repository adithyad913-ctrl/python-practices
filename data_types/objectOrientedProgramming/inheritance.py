
"""
inherience
child class acess the  methods and 
attributes of the parent class
"""
class parent:
    def house(self):
        print("parent class house method")
class child:
    def social_media_account(self):
        print("child classs social media account")

child_instance=child()
child_instance.social_media_account()
child_instance.house()