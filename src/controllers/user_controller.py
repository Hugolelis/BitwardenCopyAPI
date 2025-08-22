from db.schemas.user_schemas import UserSchema

class UserController: 
    def get_users(self):
        return UserSchema(
            id=1,
            name="Hugo",
            email="Hugo@gmail",
            password="123"
        )
