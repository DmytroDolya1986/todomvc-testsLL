from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.jquery_style_selectors import s
from selene.support.shared.jquery_style import ss


def test_complete_tasks():
    browser.open('http://todomvc.com/examples/emberjs/')

    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()

    ss('#todo-list > li').should(have.exact_texts('a', 'b', 'c'))

    ss('#todo-list > li').element_by(have.exact_text('b')).element('.toggle').click()
    ss('#todo-list > li').filtered_by(have.css_class('completed')).should(have.exact_text('b'))
    ss('#todo-list > li').filtered_by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))

