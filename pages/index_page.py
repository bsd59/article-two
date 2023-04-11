from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"

    # по Ctrl+F в DevTools сторінки знайти XPATH для посилання на англійську мову.
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    # модуль реализует клик на переход на английский
    # (в тальянской версии нет такого)
    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    def get_text_from_google_search_button(self,page: Page):
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')
