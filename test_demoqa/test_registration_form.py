from selene import browser, have, be,  by
import os

def test_registration_form(browser_setup):
    FIRSTNAME = 'First Name'
    LASTNAME = 'Last Name'
    EMAIL = 'test@test.ru'
    MOBILE = '8900555332'
    ADDRESS = 'Current Address'
    STATE = 'Uttar Pradesh'
    CITY = 'Agra'
    FILE = 'photo_test.jpg'
    FILE_PATCH = '/img/photo_test.jpg'

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type(FIRSTNAME)
    browser.element('#lastName').type(LASTNAME)
    browser.element('#userEmail').type(EMAIL)
    browser.element('div[class*="custom-control"] label[for="gender-radio-2"]').click()
    browser.element(by.id('userNumber')).should(be.blank).type(MOBILE)
    # fill field the date of birth
    browser.element(by.id('dateOfBirthInput')).click()
    browser.element(
        'select[class="react-datepicker__month-select"] option[value="6"]').click()
    browser.element(
        'select[class="react-datepicker__year-select"] option[value="1993"]').click()
    browser.element(
        'div[class="react-datepicker__day react-datepicker__day--026"]').click()
    browser.element('div[class="custom-control custom-checkbox custom-control-inline"] label[for="hobbies-checkbox-1"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#uploadPicture').send_keys(os.getcwd() + FILE_PATCH)
    browser.element('#currentAddress').type(ADDRESS)
    browser.element(by.id('react-select-3-input')).type(STATE).press_enter()
    browser.element(by.id('react-select-4-input')).type(CITY).press_enter()
    browser.execute_script("document.querySelector('#close-fixedban').remove()")
    browser.element(by.id('submit')).click()

    # check result
    browser.element(by.id('example-modal-sizes-title-lg')).should(
        have.text('Thanks for submitting the form'))
    browser.element('tr:nth-child(1) td:nth-child(2)').should(
        have.text(f'{FIRSTNAME} {LASTNAME}'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text(EMAIL))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Female'))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(MOBILE))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('26 July,1993'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Sports'))
    browser.element('tr:nth-child(8) td:nth-child(2)').should(have.text(FILE))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text(ADDRESS))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text(f'{STATE} {CITY}'))
    browser.element(by.id('closeLargeModal')).click()