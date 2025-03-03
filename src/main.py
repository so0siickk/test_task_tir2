import asyncio
from src.entities.classes import Wallet, Twitter, User
from src.models.database import UserBase
from src.repositores.librarian import create_db_and_tables, create_user


def main():
    wallet1 = Wallet("private_key_test", "address_test")
    wallet2 = Wallet("private_key_test2", "address_test2")
    # ...
    # wallet999 = Wallet("private_key_test999", "address_test999")
    all_wallets = [wallet1, wallet2]
    twitter1 = Twitter("nickname_test", "bearer_token_test", "api_key_test",
                       "api_secret_test", "access_token_test", "access_secret_test")
    twitter2 = Twitter("nickname_test2", "bearer_token_test2", "api_key_test2",
                       "api_secret_test2", "access_token_test2", "access_secret_test2")
    # ...
    # twitter999 = Twitter("nickname_test999", "bearer_token_test999", "api_key_test999",
    #                        "api_secret_test999", "access_token_test999", "access_secret_test999")
    all_twitters = [twitter1, twitter2]
    user1 = User("test_email", "password_test", "nickname_test", wallet1)
    user2 = User("test_email2", "password_test2", "nickname_test2", wallet2)
    # ...
    # user999 = User("test_email999", "password_test999", "nickname_test999", wallet999)
    all_users = [user1, user2]

    # Если акки не зарегистрированы
    # asyncio.run(User.registration_website([user1,user2]))
    # create_db_and_tables()
    # first_note = UserBase(email=user1.get_email(), password=user1.get_password(), twitter=user1.get_twitter(),
    #                       wallet_address=user1.get_wallet().get_address(),
    #                       wallet_key=user1.get_wallet().get_private_key())
    # second_note = UserBase(email=user2.get_email(), password=user2.get_password(), twitter=user2.get_twitter(),
    #                        wallet_address=user2.get_wallet().get_address(),
    #                        wallet_key=user2.get_wallet().get_private_key())
    #
    # create_user(first_note)
    # create_user(second_note)

    # Ежедневная транзакция
    for current_wallet in all_wallets:
        current_wallet.make_daily_transaction()

    # Выполнение квестов
    retweet_tasks, follow_tasks = twitter1.get_tasks()

    async def make_retweets(twitter: Twitter):
        for tweet_id in retweet_tasks:
            id = list(tweet_id.values())[0]
            await twitter.make_retweet(id)
            await asyncio.sleep(0.6)

    async def make_follows(twitter: Twitter):
        for follow_id in follow_tasks:
            id = list(follow_id.values())[0]
            await twitter.follow(id)
            await asyncio.sleep(0.6)

    for current_twitter in all_twitters:
        asyncio.run(make_retweets(current_twitter))
        asyncio.run(make_follows(current_twitter))

    # Сбор наград
    retweet_tasks, follow_tasks = twitter1.get_tasks()
    tasks_id = []
    for tweet_id in retweet_tasks:
        id = list(tweet_id.keys())[0]
        tasks_id.append(id)

    for follow_id in follow_tasks:
        id = list(follow_id.keys())[0]
        tasks_id.append(id)
    asyncio.run(User.collect_rewards(all_users, tasks_id))

    if __name__ == 'main':
        main()
