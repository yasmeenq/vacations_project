from facade.users_facade import * 

users_facade = UsersFacade()

#1) add new user:
new_user = users_facade.user_registration("Mia", "Patel", "m@mail.com",7771)
print(new_user)