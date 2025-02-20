class User:
    def __init__(self, email, password, twitter, wallet, balance=0, status="create"):
        self.email = email
        self.password = password
        self.twitter = twitter
        self.wallet = wallet
        self.balance = balance
        self.status = status

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_twitter(self):
        return self.twitter

    def get_wallet(self):
        return self.wallet

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_twitter(self, twitter):
        self.twitter = twitter

    def set_wallet(self, wallet):
        self.wallet = wallet

    def set_balance(self, balance):
        self.balance = balance

    def set_status(self, status):
        self.status = status
