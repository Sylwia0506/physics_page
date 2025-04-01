import requests
from bs4 import BeautifulSoup
import json
import re

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'[^\w\s\-.,()ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', '', text)
    return text.strip()

def get_exam_links(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        entry_content = soup.find('div', class_='entry-content')
        if not entry_content:
            return None, None
            
        links = entry_content.find_all('a')
        exam_link = None
        answer_link = None
        
        for link in links:
            href = link.get('href', '')
            text = link.text.lower()
            if href.endswith('.pdf'):
                if 'odpowiedzi' in text or 'odpowiedzi' in href.lower():
                    answer_link = href
                else:
                    exam_link = href
                    
        return exam_link, answer_link
    except Exception as e:
        print(f"Error getting exam links from {url}: {str(e)}")
        return None, None

def scrape_matura_data():
    urls = [
        "https://arkusze.pl/fizyka-matura-poziom-rozszerzony/",
        "https://arkusze.pl/fizyka-matura-poziom-podstawowy/"
    ]
    
    matury = []
    
    for url in urls:
        try:
            print(f"Scraping {url}...")
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            table = soup.find('table', class_='tablepress')
            if not table:
                print(f"No table found at {url}")
                continue
                
            level = 'rozszerzony' if 'rozszerzony' in url else 'podstawowy'
            
            rows = table.find('tbody').find_all('tr')
            print(f"Found {len(rows)} rows at {url}")
            
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 4:
                    date = clean_text(cells[0].text)
                    type_exam = clean_text(cells[1].text)
                    publisher = clean_text(cells[2].text)
                    
                    exam_page_link = cells[3].find('a')['href'] if cells[3].find('a') else None
                    
                    if exam_page_link:
                        exam_link, answer_link = get_exam_links(exam_page_link)
                        
                        if exam_link:
                            matura_data = {
                                'date': date,
                                'type': type_exam,
                                'publisher': publisher,
                                'level': level,
                                'link': exam_link,
                                'answer_link': answer_link
                            }
                            matury.append(matura_data)
                            print(f"Added exam from {date} ({publisher})")
                    
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
    
    return matury

def save_matura_data():
    matury = scrape_matura_data()
    
    with open('static/data/matury.json', 'w', encoding='utf-8') as f:
        json.dump(matury, f, ensure_ascii=False, indent=2)
    
    print(f"Zapisano {len(matury)} arkuszy maturalnych")

if __name__ == "__main__":
    save_matura_data() 