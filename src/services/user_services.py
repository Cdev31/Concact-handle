from src.db.models import UserModel
from src import User, hash_password

class UserService:

    def __init__(self):
        self.user = UserModel()

    def find_users( self ):
        new_users = []
        users = self.user.find_users()

        for user in users:
            new_users.append(user)
            
        return new_users    

    def login( self, email: str , password: str ):
        pass

    def create( self, employee: User ):

        new_password  = hash_password( employee['password'] )

        employee.update({ 'password': new_password })

        self.user.create_user( employee = employee )
        