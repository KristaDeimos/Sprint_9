import random
from faker import Faker


fake = Faker('ru_RU')

def generate_test_user():
    random_suffix = random.randint(1000, 9999)
    unique_id = f"{random_suffix}"

    return {
        'first_name': f"{fake.first_name()}_{unique_id}",
        'last_name': f"{fake.last_name()}_{unique_id}",
        'username': f"user_{unique_id}",
        'email': f"test_{unique_id}@yandex.ru",
        'password': f"TestPass123!_{unique_id}"
    }
