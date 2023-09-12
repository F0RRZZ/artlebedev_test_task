import json
import os
from pathlib import Path

import environ
import psycopg2


def is_park_in_db(park_info: tuple):
    cursor.execute(
        """
        SELECT *
        FROM parks_park
        WHERE name = %s AND description = %s
        """,
        (park_info[0], park_info[1]),
    )
    result = cursor.fetchall()
    if result:
        return True
    return False


def add_park_to_db(park_info: tuple):
    if is_park_in_db(park_info):
        return
    cursor.execute(
        """
        INSERT INTO parks_park
        (
        name,
        description,
        address,
        coordinates,
        email,
        phone,
        website,
        organization,
        inn
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        park_info,
    )
    connection.commit()


BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_DB=(str, 'postgres'),
    POSTGRES_PASSWORD=(str, 'password'),
    POSTGRES_PORT=(str, '5432'),
    POSTGRES_USER=(str, 'postgres'),
)

connection = psycopg2.connect(
    user=env('POSTGRES_USER'),
    password=env('POSTGRES_PASSWORD'),
    host=env('POSTGRES_HOST'),
    port=env('POSTGRES_PORT'),
    database=env('POSTGRES_DB'),
)
cursor = connection.cursor()

with open(
    file='data-85-structure-3.json', mode='r', encoding='utf-8'
) as read_file:
    data = json.load(read_file)
    for park in data:
        park_name = park['data']['general']['name']
        description = park['data']['general']['description']
        address = park['data']['general']['address']['fullAddress']
        coordinates = park['data']['general']['address']['mapPosition'][
            'coordinates'
        ]
        coordinates = ', '.join(map(str, coordinates))
        if 'contacts' in park['data']['general']:
            email = park['data']['general']['contacts'].get('email', '')
            if park['data']['general']['contacts']['phones']:
                phone = park['data']['general']['contacts']['phones'][0][
                    'value'
                ]
            else:
                phone = None
            website = park['data']['general']['contacts'].get('website')
        organization = park['data']['general']['organization']['name']
        inn = park['data']['general']['organization'].get('inn')
        info = (
            park_name,
            description,
            address,
            coordinates,
            email,
            phone,
            website,
            organization,
            inn,
        )
        add_park_to_db(info)
