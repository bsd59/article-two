# import time
import pages

class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        # assert 0
        pages.index_page.open_index_page(page)
        # pages.index_page.press_link_english_lang(page) # переходим на английский
        # time.sleep(10)
        actual_result = pages.index_page.get_text_from_google_search_button(page)
        assert actual_result == 'Cerca con Google', 'Google Search button text is not correct'
        # assert actual_result == 'Google Search', 'Google Search button text is not correct'
