import requests
from bs4 import BeautifulSoup

def page_by_name(name):
    page, status = load_page_by_name(name)
    if status != 200:
        return
    text = parcing_page(page)
    return text


def load_page_by_name(name: str):
    # https://ru.wikipedia.org/wiki/Вкус_ночи
    name = name.replace(' ', '_')
    url = f'https://ru.wikipedia.org/wiki/{name}'
    response = requests.get(url)
    return response.text, response.status_code


def parcing_page(page: str):
    soup = BeautifulSoup(page, 'html.parser')
    # Находим элемент по классу
    element_with_class = soup.find(class_='mw-content-ltr mw-parser-output')
    if not element_with_class:
        return
    # Получаем второго потомка элемента
    children = list(element_with_class.children)
    second_child = children[2]
    # Находим все ссылки (<a>) и удаляем их, оставляя только текст
    for a_tag in second_child.find_all('a'):
        # Заменяем каждую ссылку её содержимым
        a_tag.replace_with(a_tag.text)
    # Удаляем все теги <script> (скрипты) из дерева DOM
    for script_tag in second_child.find_all('script'):
        script_tag.extract()
    # Получаем текст без тегов и ссылок
    text_without_links = second_child.get_text()
    print(text_without_links)
    return text_without_links



if __name__ == '__main__':
    page_by_name('Вкус ночи')


