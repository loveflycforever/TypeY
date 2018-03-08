from bs4 import BeautifulSoup


def strippedTagString(tag):
    return tag.get_text().replace('\n', '').replace(' ', '')


def selectStrippedStrings(soup, selector, index=0):
    return soup.select(selector)[index].stripped_strings


def selectFindAll(soup, selector, tag, index=0):
    return soup.select(selector)[index].find_all(tag)
