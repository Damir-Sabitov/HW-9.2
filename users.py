import dataclasses
from datetime import date

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: date
    subject: str
    hobby: str
    file_name: str
    adress: str
    state: str
    city: str

john = User('John','Smith','example@mail.ru','Male','5555555555', date(1995,5,15),'Hist','Sports','my_file.png','test street address','NCR','Delhi')

