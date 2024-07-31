import psycopg2
import random
from faker import Faker
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import bcrypt
import secrets
import string

conn = psycopg2.connect("dbname=otdel_new user=postgres password=03062004tim host=localhost")
cursor = conn.cursor()

try:
    for i in range(50):
        id = i + 1

        fake = Faker('ru_RU')
        fio = fake.name_male()

        def generate_random_password(length=12):
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(characters) for i in range(length))
            return password

        def hash_password(password):
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password.decode('utf-8')  # Добавлено decode для преобразования в строку

        not_hashed_password = generate_random_password(random.randint(6, 10))
        print(not_hashed_password)
        new_password = hash_password(not_hashed_password)
        key = random.randint(1, 2)

        query = 'INSERT INTO FIO (fio_id, fio, password, key) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (id, fio, new_password, key))
        conn.commit()
    
    for i in range(30):
        id = i + 1

        f_fio = random.randint(1, 50)
        name_plan = "НИР " + str(random.randint(1, 100))

        
        def random_date(start_date_not, end_date_not):
            time_between_dates = end_date_not - start_date_not
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date_not + timedelta(days=random_number_of_days)
            return random_date
        
        start_date_not = date(2000, 1, 1)
        end_date_not = date.today()

        start_date = random_date(start_date_not, end_date_not)
        end_date = start_date + relativedelta(months=3)

        marker_mas = ["+", "-"]
        marker = random.choice(marker_mas)

        query = 'INSERT INTO Otdel_plans (Otdel_plans_id, f_fio, name_plan, start_date, end_date, marker) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (id, f_fio, name_plan, start_date, end_date, marker))
        conn.commit()

    for i in range(30):
        id = i + 1
        f_fio = random.randint(1, 50)
        plan_name = "Разработка №" + str(random.randint(1,50))
        marker_mas = ["+", "-"]
        marker = random.choice(marker_mas)

        query = 'INSERT INTO Single_plans (single_plans_id, f_fio, plan_name, marker) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (id, f_fio, plan_name, marker))
        conn.commit()

finally:
    cursor.close()
    conn.close()
