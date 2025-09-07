from selene import browser, be, have
import os, calendar
from users import User


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user:User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        if user.gender == 'Male':
            browser.element('label[for="gender-radio-1"]').should(be.clickable).click()
        elif user.gender == 'Female':
            browser.element('label[for="gender-radio-2"]').should(be.clickable).click()
        browser.element('#userNumber').type(user.phone_number)

        day=user.date_of_birth.day
        month=user.date_of_birth.month
        year=user.date_of_birth.year
        browser.element('#dateOfBirthInput').click()
        month_index = month - 1
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month_index}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        expected_text = f"{calendar.month_name[month]} {year}"
        browser.element('.react-datepicker__current-month').should(have.text(expected_text))
        browser.all('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
            .element_by(have.text(str(day))) \
            .should(be.visible) \
            .click()

        browser.element('#subjectsInput').type(user.subject).press_enter()

        if user.hobby == 'Sports':
            target = browser.element('[for="hobbies-checkbox-1"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()
        elif user.hobby == 'Reading':
            target = browser.element('[for="hobbies-checkbox-2"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()
        elif user.hobby == 'Music':
            target = browser.element('[for="hobbies-checkbox-3"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), user.file_name))
        browser.element('#uploadPicture').send_keys(file_path)

        browser.element('#currentAddress').type(user.adress)

        browser.element('#state').click()
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(user.city).press_enter()

        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('.modal-content').should(be.visible)

        full_name = f"{user.first_name} {user.last_name}"
        browser.element('.table-responsive').should(have.text(full_name))
        browser.element('.table-responsive').should(have.text(user.email))
        browser.element('.table-responsive').should(have.text(user.gender))
        browser.element('.table-responsive').should(have.text(user.phone_number))

        birth_date_str = user.date_of_birth.strftime("%d %B,%Y")
        browser.element('.table-responsive').should(have.text(birth_date_str))

        browser.element('.table-responsive').should(have.text(user.subject))
        browser.element('.table-responsive').should(have.text(user.hobby))
        browser.element('.table-responsive').should(have.text(user.file_name))
        browser.element('.table-responsive').should(have.text(user.adress))

        state_city = f"{user.state} {user.city}"
        browser.element('.table-responsive').should(have.text(state_city))








