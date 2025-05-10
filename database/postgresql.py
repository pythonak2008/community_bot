from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data.config import *


class DataBase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def conf(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME,
            port=5432
        )

    async def execute(self, sql, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql, *args)
                elif fetchval:
                    result = await connection.fetchval(sql, *args)
                elif fetchrow:
                    result = await connection.fetchrow(sql, *args)
                elif execute:
                    result = await connection.execute(sql, *args)
            return result

    async def make_user_database(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users(
                user_id BIGINT PRIMARY KEY,
                full_name VARCHAR(30),
                last_name VARCHAR(30),
                age VARCHAR(30),
                phone_number VARCHAR(30)
            )
        """
        await self.execute(sql, execute=True)

    async def make_user(self, user_id):
        sql = """
            INSERT INTO users(user_id)
            VALUES($1)
            ON CONFLICT (user_id) DO NOTHING
        """
        await self.execute(sql, user_id, execute=True)

    async def insert_some_information_of_user(self, full_name, last_name, age, phone_number, user_id):
        sql = """
            UPDATE users
            SET full_name = $1, last_name = $2, age = $3, phone_number = $4
            WHERE user_id = $5
        """
        await self.execute(sql, full_name, last_name, age, phone_number, user_id, execute=True)

    async def is_authenticated(self, user_id):
        sql = """
            SELECT status FROM users
            WHERE user_id = $1
        """
        return await self.execute(sql, user_id, fetchval=True)


    async def users_12(self,user_id):
        sql = """
            SELECT group_id FROM groups
            WHERE user_id = $1
        """
        return await self.execute(sql,user_id, fetch=True)






    async def create_register_list_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS register_list (
                id SERIAL PRIMARY KEY,
                name VARCHAR(130),
                first_name VARCHAR(130),
                last_name VARCHAR(130),
                age VARCHAR(130),
                phone VARCHAR(130),
                state VARCHAR(130),
                district VARCHAR(130),
                author VARCHAR(130),
                status VARCHAR(130),
                group_id BIGINT,
                FOREIGN KEY (group_id) REFERENCES groups(id)
            )
        """
        await self.execute(sql, execute=True)

    async def create_groups_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS groups (
                id SERIAL PRIMARY KEY,
                group_id TEXT,
                user_id BIGINT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """
        await self.execute(sql, execute=True)

    async def create_clear_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS clear (
                id SERIAL PRIMARY KEY,
                group_id BIGINT,
                status BOOLEAN,
                FOREIGN KEY (group_id) REFERENCES groups(id)
            )
        """
        await self.execute(sql, execute=True)

    async def create_remove_ads_table(self):
        sql = """
             CREATE TABLE IF NOT EXISTS remove_ads (
                 id SERIAL PRIMARY KEY,
                 group_id BIGINT,
                 status VARCHAR(130),
                 attempts VARCHAR(130),
                 text VARCHAR(130),
                 FOREIGN KEY (group_id) REFERENCES groups(id)
            )
        """
        await self.execute(sql, execute=True)

