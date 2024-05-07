from typing import NewType

# This is useful in helping catch logical errors
UserId = NewType('UserId', int)
some_id = UserId(524313)

def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(123))

# fails type checking; an int is not a UserId
user_b = get_user_name(123)