from src.db.models import UserModel
from src import User, hash_password

class UserService:

    def __init__(self):
        self.user = UserModel()


    def login( self, email, password ):
        pass   

    def create( self, employee: User ):

        new_password  = hash_password( employee['password'] )

        employee.update({ 'password': new_password })

        self.user.create_user( employee = employee )
        