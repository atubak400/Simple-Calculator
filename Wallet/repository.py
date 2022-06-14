import sqlite3
import datetime
import abc
import redis
import json

from .entities import Customer
from .wallet_exceptions import CustomerNotFoundError


now = datetime.datetime.now()
datetime_format = "%Y-%m-%d %H:%M:%S.%f"



class CustomerRepoInterface(abc.ABC):

    @abc.abstractmethod
    def create_customer(self, email: str, first_name: str, last_name: str) -> Customer:
        pass
    
    @abc.abstractmethod
    def get_customer(self, email: str) -> Customer:
        pass
    
    @abc.abstractmethod
    def update_customer(self, email: str, balance: int, update_time) -> Customer:
        pass


class CustomerRedisRepo(CustomerRepoInterface):

    def __init__(self):
        self.__conn = self.__get_db_connection()
    
    def __get_db_connection(self):
        """
        Connect to a redis database and test the connection my pinging it. return a Redis connection object if 
        ping is successful or raise an error if not.
        """
        url = 'redis://localhost:6379'
        r = redis.from_url(url)

        try:
            r.ping()
        except redis.exceptions.ConnectionError:
            print('Error connecting to Redis on {}'.format(url))
        return r

    def create_table(self):
        pass

    def create_customer(self, email: str, first_name: str, last_name: str) -> Customer:
        customer_data = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'balance': 0,
            'created_at': str(now),
            'updated_at': str(now),
        }
        self.__conn.set(email, json.dumps(customer_data))
        return Customer(
            email=customer_data['email'],
            first_name=customer_data['first_name'],
            last_name=customer_data['last_name'],
            balance=customer_data['balance'],
            created_at=now,
            updated_at=now
        )
    
    def get_customer(self, email: str) -> Customer:
        customer_json_str = self.__conn.get(email)
        if not customer_json_str:
            raise CustomerNotFoundError('Customer with email {} does not exist.'.format(email))
        
        customer_dict = json.loads(customer_json_str)  # convert JSON string to dict
        return Customer(
            email=customer_dict['email'],
            first_name=customer_dict['first_name'],
            last_name=customer_dict['last_name'],
            balance=customer_dict['balance'],
            created_at=datetime.datetime.strptime(customer_dict['created_at'], datetime_format),
            updated_at=datetime.datetime.strptime(customer_dict['updated_at'], datetime_format)
        )

    def update_customer(self, email: str, balance: int, update_time: datetime.datetime) -> Customer:
        customer_json_str = self.__conn.get(email)
        if not customer_json_str:
            raise CustomerNotFoundError('Customer with email {} does not exist.'.format(email))

        customer_dict = json.loads(customer_json_str)  # convert JSON string to dict

        updated_customer = dict(customer_dict)  # create copy to customer_dict and update only the copy.
        updated_customer['balance'] = balance
        updated_customer['updated_at'] = str(update_time)

        self.__conn.set(email, json.dumps(updated_customer))
        
        return Customer(
            email=updated_customer['email'],
            first_name=updated_customer['first_name'],
            last_name=updated_customer['last_name'],
            balance=updated_customer['balance'],
            created_at=datetime.datetime.strptime(customer_dict['created_at'], datetime_format),
            updated_at=update_time
        )

    


class CustomerSQLiteRepo(CustomerRepoInterface):
    
    def __init__(self):
        self.__conn = sqlite3.connect('database.db')
        self.__cursor = self.__conn.cursor()  
    
    def create_table(self):
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
        Email text unique,
        First_name text,
        Last_name text,
        Created_at timestamp,
        Updated_at timestamp,
        Balance integer
        )""")     

    def create_customer(self, email: str, first_name: str, last_name: str) -> Customer:   
        item = self.__cursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?)", (email, first_name, last_name, now, "-", 0))
        self.__conn.commit()
        self.__conn.close()
        return Customer(email,first_name,last_name,0,now,"-")

    def get_customer(self, email) -> Customer:
        self.__cursor.execute("SELECT * FROM customers WHERE Email = ?", (email, ))
        item = self.__cursor.fetchone()
        self.__conn.commit()
        #self.__conn.close()
        return Customer(item[0], item[1], item[2], item[3], item[4], item[5])

        
    def update_customer(self, email, new_amount, now):
        self.__cursor.execute("UPDATE customers SET Balance = ?, Updated_at = ? WHERE Email = ?", (new_amount, now, email))
        self.__conn.commit()
        #self.__conn.close()
        #return Customer(email,first_name,last_name,0,now,new_amount)
        # return Customer object here
