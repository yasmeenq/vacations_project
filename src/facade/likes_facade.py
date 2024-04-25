from utils.dal import *
from logic.likes_logic import *

likes_logic = LikesLogic()

#like a vacation 👍
print("Like a Vacation: ")
user_id_likes = str(input("userID: "))
vacation_id_likes = str(input("vacationID: "))

add_like = likes_logic.add_like(user_id_likes, vacation_id_likes)
print(add_like)
print()

#delete a like of a vacation 👍
print("Unlike a Vacation: ")
user_id_delete_like = str(input("userID: "))
vacation_id_delete_like = str(input("vacationID: "))

delete_like = likes_logic.delete_like(user_id_delete_like, vacation_id_delete_like)
print(delete_like)
