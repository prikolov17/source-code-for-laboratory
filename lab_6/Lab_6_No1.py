class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self._password = password
    def set_password(self,new_password):
        if new_password == self._password:
            print('Ошибка: пароль совпадает со старым')
        elif len(new_password)<6:
            print('Ошибка: пароль должен содержать минимум 6 символов')
        else:
            self._password = new_password
            print('Пароль успешно измненён')
    def check_password(self,password):
        return self._password == password

user = UserAccount('cate_pirson','catepirson@example.com','catepirson1999')
print('Проверка старого пороля:',user.check_password('catepirson1999'))
user.set_password('catepirson1999')
user.set_password('catepirson2000')
print('Проверка нового пороля:',user.check_password('catepirson2000'))
print('Проверка неправильного пароля:',user.check_password('catepirson2001'))






