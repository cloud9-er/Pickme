import requests
from bs4 import BeautifulSoup 
import time 
import json
book_list=[]
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
for page_num in range(1,51):
    url=f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    response.encoding = 'utf-8'
    if response.status_code==200:
        print(f'page-{page_num} is successfully scraped')
    else:
        continue
    s = BeautifulSoup(response.text, 'html.parser')
    books = s.find_all('article', class_='product_pod')
    for book in books:
        title=book.h3.a['title']
        price=float(book.find('p',class_='price_color').text.replace('£',''))
        tag=book.find('p',class_='star-rating') 
        if tag:
            rating=rating_map[tag['class'][1]]
            print(rating)
        else:
            rating=None
        dct={"title":title,"price":price,"rating":rating}
        book_list.append(dct)
        time.sleep(1)
    print(book_list[0])
prices=[p['price'] for p in book_list]
lowest_price=min(prices)
highest_price=max(prices)
ratings=[r['rating'] for r in book_list if r['rating'] is not None]
lowest_rating=min(ratings)
highest_rating=max(ratings)
#make the scoring system 
for book in book_list:
    if book['rating'] is  not None:
        normalization_score = (book['rating']-lowest_rating)/(highest_rating-lowest_rating)
        normalization_price = (highest_price-book['price'])/(highest_price-lowest_price)
        book['score'] = (normalization_score *0.6) + (normalization_price *0.4)
    else:
        book['score']=0
ranking=sorted(book_list ,key=lambda book:book['score'], reverse=True )
with open('books.json', 'w') as f:
    json.dump(ranking, f, indent=2)