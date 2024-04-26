from facade.likes_facade import *

likes_facade = LikesFacade()

like_vacation = likes_facade.like(9,11)
print(like_vacation)

unlike_vacation = likes_facade.unlike(9,11)
print(unlike_vacation)