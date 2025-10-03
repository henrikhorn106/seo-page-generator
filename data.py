import requests
from bs4 import BeautifulSoup


def get_keywords():
    keyword_list = [
        'Markenidentität entwickeln', 'Branding-Agentur', 'visuelle Identität', 'Unternehmens-Branding',
        'Logo-Design', 'Webdesign', 'Corporate Design', 'Grafikdesign', 'UI/UX-Design', 'Motion-Graphics',
        'Illustrationen erstellen', 'Social Media Branding',
        'Branding für Start-ups', 'Branding für kleine Unternehmen', 'Kreativagentur Berlin',
        'Design-Services für Marketing', 'Branding für E-Commerce',
        'wie erstelle ich eine Markenidentität', 'was ist ein Corporate Design',
        'wie viel kostet ein Logo-Design', 'Bedeutung von Branding', 'Branding-Strategie entwickeln',
        'Alternative zu Canva', 'Webdesign-Agenturen vergleichen', 'Kreativ-Portfolio'
    ]
    return keyword_list


def scrape_pages(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    tags = soup.find_all('a', class_='blog-more-link')

    page_list = []
    for tag in tags:
        page = 'https://www.create-dot.com' + tag.get('href')
        page_list.append(page)
    return page_list


def get_lexikon_pages():
    url = 'https://www.create-dot.com/marketing-lexikon'
    return scrape_pages(url)


def get_blog_pages():
    url = 'https://www.create-dot.com/marketing-blog'
    return scrape_pages(url)
