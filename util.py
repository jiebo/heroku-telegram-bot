def vote_option(message, test):
    if str(message).lower() == '/option1':
        test[0] += 1
    else:
        test[0] -= 1