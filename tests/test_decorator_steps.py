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
def test_decorator_steps_github():
    open_home_page()
    search_for_repository('Fatalwgx/Allure_representation_github')
    go_to_repository_page('Fatalwgx/Allure_representation_github')
    switch_to_issues()
    nth_issue_name_equals(1, 'This issue is better be found')


# These methods are supposed to be located in a separate file, but were left here for convenience of this presentation

@allure.step('Opening github homepage')
def open_home_page():
    browser.open('https://github.com')


@allure.step('Searching for repository {repository}')
def search_for_repository(repository):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repository)
    s('.header-search-input').submit()


@allure.step('Go to repository "{repository}" page')
def go_to_repository_page(repository):
    s(by.link_text(repository)).click()


@allure.step('Switch to issues tab')
def switch_to_issues():
    s('#issues-tab').click()


@allure.step('Issue number "{issue_number}" should have name "{issue_name}"')
def nth_issue_name_equals(issue_number: int, issue_name: str):
    s(f'#issue_{issue_number}_link').should(have.exact_text(issue_name))
