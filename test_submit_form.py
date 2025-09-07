from resource import RegistrationPage
from users import User, john


def test_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(john)
    registration_page.should_have_registered(john)

