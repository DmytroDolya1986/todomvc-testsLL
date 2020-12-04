from selene.support.conditions import have
from selene.support.shared import browser


def test_complete_tasks_css_only():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list > li').filtered_by(have.no.css_class('completed'))

    browser.all('#todo-list > li').filtered_by(have.no.css_class('completed')).element('.toggle').click()
    browser.all('#todo-list > li').filtered_by(have.css_class('completed'))
    browser.all('#todo-list > li').filtered_by(have.no.css_class('completed'))
