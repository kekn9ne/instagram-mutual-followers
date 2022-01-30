import instaloader
import argparse

L = instaloader.Instaloader()

parser = argparse.ArgumentParser(description='Instagram mutual followers detector.')
parser.add_argument('-u', required=True, type=str, help="Instagram account to login. DON'T USE YOUR MAIN ACCOUNT!")
parser.add_argument('-p', required=True, type=str, help="Instagram account's password. DON'T USE YOUR MAIN ACCOUNT!")
parser.add_argument('-user1', required=True, type=str, help="First user to get followers")
parser.add_argument('-user2', required=True, type=str, help="Second user to get followers")
args = parser.parse_args()

username = args.u
password = args.p
L.login(username, password)
print("Logged in.")

user1 = args.user1
user2 = args.user2


profile1 = instaloader.Profile.from_username(L.context, user1)
print("Parsing user1's followers")
for follower in profile1.get_followers():
    open("{}.txt".format(user1), "a").write("{}\n".format(follower.username))

profile2 = instaloader.Profile.from_username(L.context, user2)
print("Parsing user2's followers")
for follower in profile2.get_followers():
    open("{}.txt".format(user2), "a").write("{}\n".format(follower.username))

print("Comparing two users.")
set1 = set()
with open('{}.txt'.format(user1), 'r') as file1:
    for line in file1:
        set1.add(line.strip())

set2 = set()
with open('{}.txt'.format(user2), 'r') as file2:
    for line in file2:
        set2.add(line.strip())

print("Saving mutuals")
common = set1.intersection(set2)
_list = list(common)
for line in _list:
    open("mutuals.txt", "a").write("{}\n".format(line))

print("Done")