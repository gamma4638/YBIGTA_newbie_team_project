from app.user.user_repository import UserRepository
from app.user.user_schema import User, UserLogin, UserUpdate

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        """UserService 생성자"""
        self.repo = user_repository

    def login(self, user_login: UserLogin) -> User:
        user = self.repo.get_user_by_email(user_login.email)
        if not user:
            raise ValueError("User not Found.")  # 대소문자와 문장 부호 일치
        if user.password != user_login.password:
            raise ValueError("Invalid ID/PW")    # 테스트 기대 메시지에 맞춤
        return user

    def register_user(self, new_user: User) -> User:
        existing_user = self.repo.get_user_by_email(new_user.email)
        if existing_user:
            raise ValueError("User already Exists.")  # 테스트 기대 메시지에 맞춤
        return self.repo.save_user(new_user)

    def delete_user(self, email: str) -> User:
        user = self.repo.get_user_by_email(email)
        if not user:
            raise ValueError("User not Found.")
        return self.repo.delete_user(user)

    def update_user_pwd(self, user_update: UserUpdate) -> User:
        user = self.repo.get_user_by_email(user_update.email)
        if not user:
            raise ValueError("User not Found.")
        user.password = user_update.new_password
        return self.repo.save_user(user)
