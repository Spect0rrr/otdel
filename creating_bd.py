import psycopg2

conn = psycopg2.connect("dbname=otdel_new user=postgres password=03062004tim host=localhost")
cursor = conn.cursor()

query = '''
CREATE TABLE FIO (
    fio_id INT NOT NULL UNIQUE,
    fio VARCHAR(200),
    password VARCHAR(80),
    key INT NOT NULL,
    PRIMARY KEY(fio_id)
);

CREATE TABLE Otdel_plans (
    Otdel_plans_id INT NOT NULL UNIQUE,
    f_fio INT NOT NULL,
    name_plan VARCHAR(200),
    start_date VARCHAR(20),
    end_date VARCHAR(20),
    marker VARCHAR(5),
    PRIMARY KEY (Otdel_plans_id),
    FOREIGN KEY (f_fio) REFERENCES FIO(fio_id)
);

CREATE TABLE Single_plans (
    single_plans_id INT NOT NULL UNIQUE,
    f_fio INT NOT NULL,
    plan_name varchar(240),
    marker VARCHAR(5),
    PRIMARY KEY (single_plans_id),
    FOREIGN KEY (f_fio) REFERENCES FIO(fio_id)
)
'''
cursor.execute(query)
conn.commit()

cursor.close()
conn.close()