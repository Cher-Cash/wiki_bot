import requests
from bs4 import BeautifulSoup, Tag

def page_by_name(name: str):
    page, status = load_page_by_name(name)
    if status != 200:
        return
    text = parsing_page(page)
    return text


def load_page_by_name(name: str):
    # https://ru.wikipedia.org/wiki/Вкус_ночи
    name = name.replace(' ', '_')
    url = f'https://ru.wikipedia.org/wiki/{name}'
    response = requests.get(url)
    return response.text, response.status_code


def parsing_page(page: str):
    soup = BeautifulSoup(page, 'html.parser')
    for table in soup.find_all('table'):
        table.decompose()
    element_with_class = soup.find(class_='mw-content-ltr mw-parser-output')
    if not element_with_class:
        return
    looking_for = None
    for child in element_with_class.children:
        if isinstance(child, Tag) and child.find('b'):
            looking_for = child
            break
    if not looking_for:
        return
    for a_tag in looking_for.find_all('a'):
        a_tag.replace_with(a_tag.text)
    for script_tag in looking_for.find_all('script'):
        script_tag.extract()
    text_without_links = looking_for.get_text()
    print(text_without_links)
    return text_without_links


if __name__ == '__main__':
    page_by_name('Солнце')
