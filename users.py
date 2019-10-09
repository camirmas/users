import csv
from faker import Faker


def main():
    fake = Faker()
    users = [create_user(fake) for i in range(10000)]
    create_csv(users)

def create_user(fake):
    return [fake.first_name(), fake.last_name(), fake.email()]

def create_csv(users):
    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["first_name", "last_name", "email"]
        writer.writerow(header)
        writer.writerows(users)


main()
