aksh=input(' please enter the password -->>>>>>>>>>> ' )
print('\n')
if aksh=='roy@zig':
   print(' your password is correct ' )

else:
  print(' your password is incorrect ' )
  print('\n')
  exit()
print('\n')

import os, uuid, string, random

try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests


class Xnce():
    def __init__(self):
        self.target= input("[ + ] Username: ")
        if self.target[0] == "@":
            print("[ - ] Enter User Without '@' ", end="")
            input()
            exit()
        if "@" in self.target:
            self.data = {
                "_csrftoken":
                    "".join(
                        random.choices(string.ascii_lowercase +
                                       string.ascii_uppercase + string.digits,
                                       k=32)),
                "user_email":
                    self.target,
                "guid":
                    uuid.uuid4(),
