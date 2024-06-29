def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    welcome_messages = []
    for i, name in enumerate(names, start=1):
        message = f"Hello, {name}! You'll be assigned to room {i}."
        welcome_messages.append(message)
    return welcome_messages

    

def printer(names):
    return None
