import argparse
from include.user_auth import User

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help='Enter username')
    parser.add_argument("-p", "--password", help='Enter password')
    parser.add_argument("-l", "--level", help='Enter level')
    args = parser.parse_args()
    user = args.username
    password = args.password
    level = args.level
    return user, password, level

if __name__ == "__main__":
    username, password, level = parse_args()
    user = User(username)
    user.add(password, level)