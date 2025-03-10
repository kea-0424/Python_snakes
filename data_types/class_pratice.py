class UserInfo:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address

   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False

user = UserInfo('user043', 'kuenenekeabetsoe@gmail.com')

print(user.check_username('user043')) # returns True
print(user.check_username('kuenenekeabetsoe@gmail.com')) # returns False