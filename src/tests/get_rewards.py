import requests
import asyncio
from random import shuffle

from src.entities.classes import Wallet, User

all_tasks = []
with requests.Session() as session:
    login_data = {
        'email': "email",
        'password': "password",
        'login_button': '1'
    }
    url = "https://castile.world//api/guest/login"
    response = session.post(url=url, data=login_data)
    response_json = response.json()
    bearer_token = response_json.get("data").get("auth")
    for number in range(11):
        try:
            headers = {'Authorization': f'Bearer {bearer_token}'}
            response = session.get(f"https://castile.world/gapi/task/v1/tasks?community_id={number}", headers=headers)
            all_tasks += response.json().get("data").get("tasks")
        except Exception as e:
            print(f"Заданий с id:{number} нет")
retweet_numbers = []
follow_numbers = []
for index, task in enumerate(all_tasks):
    print(task)
    if "Repost" in task.get("description"):
        retweet_numbers.append(index)
    if ("Follow" in task.get("description")) and ("target=" in task.get("url")):
        follow_numbers.append(index)
retweet_tasks = []
follow_tasks = []
for index in retweet_numbers:
    retweet_tasks.append({all_tasks[index].get("id"): all_tasks[index].get("url").split("target=")[1]})
for index in follow_numbers:
    follow_tasks.append({all_tasks[index].get("id"): all_tasks[index].get("url").split("target=")[1]})
print("\nRetweet tasks: \n")
shuffle(retweet_tasks)
for task in retweet_tasks:
    print(task)
print("Follow tasks: \n")
shuffle(follow_tasks)
for task in follow_tasks:
    print(task)

tasks_id = []

for tweet_id in retweet_tasks:
    id = list(tweet_id.keys())[0]
    tasks_id.append(id)

for follow_id in follow_tasks:
    id = list(follow_id.keys())[0]
    tasks_id.append(id)

test_email = "email"
password = "password"
wallet1 = Wallet("test_key", "test address")
user1 = User(test_email, password, "twitter", wallet1)
wallet2 = Wallet("test_key1", "test address")
user2 = User("test@mail.ru", "password", "twitter", wallet2)
users = [user1, user2]


async def get_rewards():
    await User.collect_rewards(users, tasks_id)


asyncio.run(get_rewards())
