from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Fatalwgx')
@allure.feature('Repository issues accessability')
@allure.story("First issue's name is \'This issue is better be found\'")
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps_github():
    with allure.step('Opening github homepage'):
        browser.open("https://github.com")

    with allure.step('Searching for repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys("Fatalwgx/Allure_representation_github")
        s('.header-search-input').submit()

    with allure.step('Go to repository page'):
        s(by.link_text("Fatalwgx/Allure_representation_github")).click()

    with allure.step('Switching to Issues tab'):
        s('#issues-tab').click()

    with allure.step('Issue #1 name should match "This issue is better be found"'):
        s('#issue_1_link').should(have.exact_text('This issue is better be found'))
