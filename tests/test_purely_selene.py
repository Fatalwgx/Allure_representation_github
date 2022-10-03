from selene.support import by
from selene.support.conditions import  have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_pure_selene_github():
    browser.open("https://github.com")
    s('.header-search-input').click()
    s('.header-search-input').send_keys("Fatalwgx/Allure_representation_github")
    s('.header-search-input').submit()
    s(by.link_text("Fatalwgx/Allure_representation_github")).click()
    s('#issues-tab').click()
    s('#issue_1_link').should(have.exact_text('This issue is better be found'))
