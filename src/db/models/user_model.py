from src.db.libs.connection import connection
from src import User

class UserModel:

    def __init__( self ):
        self.connection = connection

    def create_user( self, employee: User ):

        cursor = self.connection.cursor()

        insert_user = "INSERT INTO employees ( name, email, password, phone_number ) VALUES (%s,%s,%s,%s )"
        
        data = ( employee['name'], employee['email'], employee['password'], employee['phoneNumber'] )

        cursor.execute( insert_user, data )

        self.connection.commit()

        cursor.close()



    def find_by_id( self, id ):    
        pass


    def find_one_by( self, term ):
        pass