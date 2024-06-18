from src.db.libs.connection import connection
from src import User

class UserModel:

    def __init__( self ):
        self.connection = connection

    def find_users( self ):
        
        cursor = self.connection.cursor()

        query_data = "SELECT * FROM users"

        cursor.execute( query_data )

        result = cursor.fetchall()

        return result

    def create_user( self, employee: User ):

        cursor = self.connection.cursor()

        insert_user = "INSERT INTO users ( name, email, password, phone_number ) VALUES (%s,%s,%s,%s )"
        
        data = ( employee['name'], employee['email'], employee['password'], employee['phoneNumber'] )

        cursor.execute( insert_user, data )

        self.connection.commit()

        cursor.close()



    def find_by_id( self, id: int ):    
        pass


    def find_one_by( self, condition: str, term: str,  ):

        cursor = self.connection.cursor()

        query_data = f"SELECT * FROM employees WHERE {condition}='{term}'"

        cursor.execute( query_data )

        result = cursor.fetchone()

        return result

    def update(self):
        pass