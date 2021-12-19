from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.user_id})"


if __name__ == "__main__":
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda user: user.user_id))
    # to jest troche szybsze niż lambda
    print(sorted(users, key=attrgetter('user_id')))
