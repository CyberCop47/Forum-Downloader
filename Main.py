import requests
from bs4 import BeautifulSoup
import os

login_url = 'https://example.com/login'  # if the websites need you to login then use this if it doesn't then keep it as is and comment the "login" function call out
login_payload = {
    'username': 'your_username',
    'password': 'your_password',
    'login': 'Login',
    'redirect': 'index.php',
    'sid': ''
}

def login(session, login_url, payload):
    print("Attempting to log in...")
    response = session.post(login_url, data=payload)
    return response

def is_logged_in(session, check_url):
    response = session.get(check_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find('a', string='Logout') is not None
    return False

def fetch_page(session, url):
    print(f"Fetching page: {url}")
    response = session.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    return None

def save_content(content, folder, filename):
    print(f"Saving content to {filename}")
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
        file.write(content)

def scrape_forum(base_url, start, page_number):
    folder = 'downloaded_forum'
    os.makedirs(folder, exist_ok=True)

    with requests.Session() as session:
        login_response = login(session, login_url, login_payload)
        if is_logged_in(session, 'https://example.com/forum'):
            print("Login successful!")
        else:
            print("Login failed!")
            return

        url = f"{base_url}&start={start}"
        soup = fetch_page(session, url)

        if soup:
            print("Checking links...")
            titles = soup.find_all('span', class_='topicTitle')
            for title in titles:
                parent_link = title.find_parent('a', href=True)
                if parent_link and parent_link['href'].endswith('.html'):
                    question_url = parent_link['href']
                    if not question_url.startswith('http'):
                        question_url = f"https://example.com{question_url}"
                    
                    print("Pattern found, downloading...")
                    question_soup = fetch_page(session, question_url)

                    if question_soup:
                        question_content = question_soup.prettify()
                        filename = f"question_{start}_{parent_link['href'].split('/')[-1]}.html"
                        save_content(question_content, folder, filename)
                        print(f"Saved: {filename}")

        print(f"Page done {page_number}. Moving to next page...")

base_url = 'https://example.com/forum/search'
max_pages = 1  # Adjust to the number of pages you want to scrape

for page_number in range(max_pages): #this loop is specifically for the website I used it in. You can remove this if you want.
    scrape_forum(base_url, page_number * 50, page_number + 1)
# This is very unrefined. After my exams I will make it more for general usage
