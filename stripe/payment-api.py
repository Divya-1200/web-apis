import stripe


def balance():
    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

    print(stripe.Balance.retrieve())

def transaction():

    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

    print(stripe.BalanceTransaction.list(limit=3))

if __name__ == "__main__":
    balance()
    transaction()