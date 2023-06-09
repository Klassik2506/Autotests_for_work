import time

from selene import browser, have, be
import os

def test_lk_main_menu():
    browser.element('#nav_bar_category').click()
    browser.element('.user-statistics-card>article>.headline').should(have.exact_text('Новости'))
    browser.element('#nav_bar_document').click()
    browser.element('.ng-star-inserted>div>.headline').should(have.exact_text('Заявки'))
    browser.element('#nav_bar_star').click()
    browser.element('.ng-star-inserted>div>.headline').should(have.exact_text('Программа лояльности'))
    browser.element('#nav_bar_bookmark').click()
    browser.element('.mat-tab-label-content').should(have.exact_text('Новые'))
    browser.open('https://b2b.rosbank-dom.ru/Home/shatl/home/main')
    browser.element('#nav_bar_useful_links').click()
    browser.element('.ng-star-inserted>section>.headline').should(have.exact_text('Полезные сервисы'))
    browser.element('#nav_bar_info').click()
    browser.switch_to_next_tab()
    browser.element('#zone-left>.name_titile').should(have.exact_text('База знаний'))

def test_dropdaun_button_create_request():
    browser.element('#create_lead_btn').click()
    browser.element('#create_lead_for_reward').click()
    browser.element('.title').should(have.exact_text('Профиль'))
    browser.open('https://b2b.rosbank-dom.ru/Home/shatl/home/main')

    browser.element('#create_lead_btn').click()
    browser.element('#create_full_lead').click()
    browser.element('#leadex_leadTypeString').should(have.exact_text('Полная заявка'))
    browser.open('https://b2b.rosbank-dom.ru/Home/shatl/home/main')

    browser.element('#create_lead_btn').click()
    browser.element('#create_express_lead').click()
    browser.element('#leadex_leadTypeString').should(have.exact_text('Экспресс заявка'))
    browser.open('https://b2b.rosbank-dom.ru/Home/shatl/home/main')

    browser.element('#create_lead_btn').click()
    browser.element('#create_nonmort_deal').click()
    browser.element('.ng-star-inserted+.headline').should(have.exact_text('Неипотечная сделка'))
    browser.open('https://b2b.rosbank-dom.ru/Home/shatl/home/main')

def test_form_full_reqwest():
    browser.element('#create_lead_btn').click()
    browser.element('#create_full_lead').click()
    browser.element('#leadex_leadTypeString').should(have.exact_text('Полная заявка'))

    # Выберите продукт
    browser.element('#showcase_default').click()
    browser.element('#showcase_default_product').click()

    # Объект
    browser.execute_script("window.scrollTo(0, 300);")
    browser.element('#navicons_flat_regionid').click()
    browser.element(f'#mat-option-{28}>.mat-option-text').should(have.exact_text('Московская область')).click()
    time.sleep(1)
    browser.element('#new_ref_city_services').click()
    browser.element(f'#mat-option-{1672}>.mat-option-text').should(have.exact_text('Химки')).click()
    browser.element('#object_mcdsoft_type_object').click()
    browser.element(f'#mat-option-{465}>.mat-option-text').should(have.exact_text('Квартира в строящемся доме')).click()
    browser.element('#navicons_credit_sum').type('15000000')
    browser.element('#mcdsoft_period_year').type('20')
    browser.element('#navicons_first_pay_money').type('3000000')
    browser.element('#description').type('Заявка на успех!!')

    # Персональные данные
    browser.execute_script("window.scrollTo(0, 600);")
    browser.element('.mat-form-field-infix>#full_fio').type('Данилов Николай Иванович')
    browser.element('#mat-select-value-7').click()
    browser.element(f'#mat-option-{476}>.mat-option-text').should(have.exact_text('Мужской')).click()
    browser.element('#mat-select-value-9').click()
    browser.element(f'#mcdsoft_familystatus-panel>#mat-option-{478}>.mat-option-text').should(have.exact_text('Холост/не замужем')).click()
    browser.element('#mat-input-2').click()
    browser.element(f'#mat-option-{486}>.mat-option-text').should(have.exact_text('Высшее')).click()
    browser.element('.mat-form-field-infix>#mobilephone1').type('9271165062')
    browser.element('.mat-form-field-infix>#emailaddress1').type('aaa@mail.ru')
    browser.element('.mat-form-field-infix>#mcdsoft_children_not_resident_amount').type('0')
    browser.element('.mat-form-field-infix>#dc_snils').type('00000000000')

    # Гражданство
    browser.execute_script("window.scrollTo(0, 1250);")
    browser.element('.mat-form-field-infix>#mcdsoft_tax_number').type('6516516516516651651616516')

    # Паспорт
    browser.execute_script("window.scrollTo(0, 1700);")
    browser.execute_script('document.querySelector("#recognition_uploadDocs > form > input[type=file]").style.opacity=1;'
                           'document.querySelector("#recognition_uploadDocs > form > input[type=file]").style["transform"]="translate(0px, 0px) scale(1)";'
                           'document.querySelector("#recognition_uploadDocs > form > input[type=file]").style["MozTransform"]="translate(0px, 0px) scale(1)";'
                           'document.querySelector("#recognition_uploadDocs > form > input[type=file]").style["WebkitTransform"]="translate(0px, 0px) scale(1)";'
                           'document.querySelector("#recognition_uploadDocs > form > input[type=file]").style["msTransform"]="translate(0px, 0px) scale(1)";'
                           'document.querySelector("#recognition_uploadDocs > form > input[type=file]").style["OTransform"]="translate(0px, 0px) scale(1)";')
    browser.element('.passport_with_title>#recognition_uploadDocs>form>input').send_keys(os.path.join(os.path.abspath(
        'resources/test_photo.jpg')))
    browser.execute_script("window.scrollTo(0, 2100);")
    browser.element('#mcdsoft_actual_doc_number').type('0000000000')
    browser.element('#mcdsoft_actual_code_org').type('621111')
    browser.element('#doc_date>.mat-form-field>.mat-form-field-wrapper>.mat-form-field-flex>.mat-form-field-suffix>.mat-datepicker-toggle>.mat-focus-indicator').click()
    browser.element('[id^=mat-calendar][id*=button]').click()
    browser.element('.mat-calendar-body-cell[aria-label="2015"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="июнь 2015"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="28 июня 2015 г."]').click()
    browser.element('#birthday>.mat-form-field>.mat-form-field-wrapper>.mat-form-field-flex>.mat-form-field-suffix>.mat-datepicker-toggle>.mat-focus-indicator').click()
    browser.element('[id^=mat-calendar][id*=button]').click()
    browser.element('.mat-calendar-body-cell[aria-label="1995"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="июнь 1995"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="25 июня 1995 г."]').click()
    browser.element('#inputField').type('ГУ МВД РОССИИ ПО САРАТОВСКОЙ ОБЛ.')
    browser.element('#mcdsoft_birth_place').type('Саратов')
    browser.element('#mat-input-22').type('РОССИЯ')
    browser.execute_script("window.scrollTo(0, 2800);")

    # Адрес
    browser.element('#mcdsoft_full_address').type('г Москва, пр-кт Вернадского, д 2')
    browser.element('[id^=mat-option]>.mat-option-text>.ng-star-inserted').should(have.exact_text('г Москва, пр-кт Вернадского, д 2')).click()

    # Место работы"
    browser.element('#mcdsoft_employment_type>.mat-select-trigger>[id^=mat-select-value]>.mat-select-value-text').click()
    browser.element('[id^="mat-option"]>.mat-option-text').should(have.exact_text('По найму')).click()
    browser.element('#companyname').type('7727004113')
    browser.element('[id^=mat-option]>.mat-option-text>.ng-star-inserted>.suggestion-title').should(have.exact_text('АО "ЛАНИТ"')).click()
    browser.element('#mcdsoft_company_address').type('Москва, вн.тер.г. Муниципальный Округ Басманный, ул Доброслободская, д. 5')
    browser.element('#job_mcdsoft_date_job_placement>.mat-form-field>.mat-form-field-wrapper>.mat-form-field-flex>.mat-form-field-suffix>.mat-datepicker-toggle>.mat-focus-indicator').click()
    browser.element('[id^=mat-calendar][id*=button]').click()
    browser.element('.mat-calendar-body-cell[aria-label="2018"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="май 2018"]').click()
    browser.element('.mat-calendar-body-cell[aria-label="29 мая 2018 г."]').click()
    browser.execute_script("window.scrollTo(0, 3200);")
    browser.element('#jobtitle').type('Директор')
    browser.element('[id^=mat-autocomplete]>[id^=mat-option]>.mat-option-text>.ng-star-inserted').should(have.exact_text('Директор')).click()
    browser.element('#job_add_job').click()
    browser.element('#job_remove_job').click()
    browser.execute_script("window.scrollTo(0, 3700);")

    # Доходы
    browser.element('#income_2ndfl').click()
    browser.execute_script("window.scrollTo(0, 4000);")
    browser.element('#income_2ndfl_recognition>section>#recognition_uploadDocs>form>input').send_keys(os.path.join(os.path.abspath(
        'resources/test_photo.jpg')))
    browser.execute_script("window.scrollTo(0, 4500);")
    browser.element('#mcdsoft_grey_avg').type('50000')
    browser.element('#mcdsoft_pension').type('0')

    # Расходы

    # Дополнительные вопросы
    browser.execute_script("window.scrollTo(0, 5700);")
    browser.element('#documents-required_approval_recognition>section>#recognition_uploadDocs>form>input').send_keys(
        os.path.join(os.path.abspath(
            'resources/test_photo.jpg')))
    browser.execute_script("window.scrollTo(0, 6000);")
    browser.element('#documents-required_object_doc_recognition>section>#recognition_uploadDocs>form>input').send_keys(
        os.path.join(os.path.abspath(
            'resources/test_photo.jpg')))
    browser.execute_script("window.scrollTo(0, 6500);")
    browser.element('#agreement_setConsentTypeWritten').click()
    browser.element('#uploadAgreementBlank>.mat-raised-button>label').should(have.exact_text('Загрузить'))
    time.sleep(3)






    # browser.element('#firstName').type('Nikolai')
    # browser.element('#lastName').type('Danilov')
    # browser.element('#userEmail').type('Danilov@gmail.com')
    # browser.element('[for=gender-radio-1]').click()
    # browser.element('#userNumber').type('9270535555')
    #
    # browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__month-select').click()
    # browser.all('.react-datepicker__month-select option').should(have.size_greater_than(0)).filtered_by(have.exact_text('June')).first.click()
    # browser.element('.react-datepicker__year-select').click()
    # browser.all('.react-datepicker__year-select option').should(have.size_greater_than(0)).filtered_by(have.exact_text('1991')).first.click()
    # browser.element('.react-datepicker__day--025').should(have.no.css_class('.react-datepicker__day--outside-month')).click()
    #
    # browser.element('#subjectsInput').type('Chemistry').press_enter()
    # browser.element('#subjectsInput').type('Arts').press_enter()
    #
    # browser.element('[for="hobbies-checkbox-3"]').click()
    #
    # browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('test_photo.jpg')))
    #
    # browser.element('#currentAddress').type('Saratov')
    # browser.element('#state').click()
    # browser.element('#react-select-3-option-0').should(have.exact_text('NCR')).click()
    # browser.element('#city').click()
    # browser.element('#react-select-4-option-0').should(have.exact_text('Delhi')).click()
    # browser.element('#submit').click()
    #
    # browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    # browser.all('tbody tr').should(have.exact_texts(
    #     'Student Name Nikolai Danilov',
    #     'Student Email Danilov@gmail.com',
    #     'Gender Male',
    #     'Mobile 9270535555',
    #     'Date of Birth 25 June,1991',
    #     'Subjects Chemistry, Arts',
    #     'Hobbies Music',
    #     'Picture test_photo.jpg',
    #     'Address Saratov',
    #     'State and City NCR Delhi'
    # ))