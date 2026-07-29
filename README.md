# BestBookBuy

BestBookBuy is a Python web scraper that collects book listings — including price and customer rating — and ranks them using a custom scoring algorithm. Instead of just finding the cheapest option, it balances price *and* quality, acting like an unbiased recommendation engine: no hidden incentives, just the best overall value for the reader.

## How the Scoring Works

The ranking score combines two factors: price and customer rating. Since these exist on completely different scales (price varies widely in pounds, while ratings run from 1 to 5 stars), each is first normalized to a common 0–1 scale using min-max normalization — with price inverted, so cheaper books score higher rather than lower.

These two normalized values are then combined using a weighted formula: 60% rating, 40% price. This reflects a deliberate design choice — quality matters more than savings. A cheap book with poor reviews may look appealing on price alone, but ultimately delivers a worse experience; the formula favors well-reviewed books while still rewarding good value.

```
score = (0.6 × normalized_rating) + (0.4 × normalized_price)
```

## Tech Stack

- **Python** — core scraping and data processing logic
- **Requests** — fetches web pages via HTTP
- **BeautifulSoup (bs4)** — parses and extracts data from HTML
- **JSON** — stores the final ranked results
- **Git & GitHub** — version control and hosting

*(Planned: HTML/CSS/JavaScript frontend, deployed via GitHub Pages)*

## How to Run It

1. Clone the repository:
   ```
   git clone https://github.com/cloud9-er/Pickme.git
   cd Pickme
   ```

2. Install the required libraries:
   ```
   pip install requests beautifulsoup4
   ```

3. Run the scraper:
   ```
   python3 price_bot.py
   ```

This will scrape all 50 pages of books.toscrape.com, calculate a ranking score for each book, and save the results to `books.json`.

## Future Improvements

- Expand scraping to additional retailers to enable cross-site price and value comparisons, helping users find the best place to buy from
- For sites with strong anti-scraping protections (e.g. Amazon), investigate official APIs (e.g. Amazon Product Advertising API) rather than scraping directly, respecting each platform's terms of service
- Store results in a SQLite database instead of flat JSON, enabling historical price tracking over time
- Build an interactive Streamlit dashboard with search, filtering, and charts
- Add a command-line interface with options like `scrape`, `analyze`, and `dashboard`
- Export filtered results to CSV
- Cache downloaded pages to reduce repeat requests
- Add automated tests for price parsing, rating conversion, and the ranking algorithm
- Add structured logging in place of print statements
- Containerize the project with Docker

## Note

This project scrapes [books.toscrape.com](https://books.toscrape.com), a demo site built specifically for practicing web scraping. Prices and ratings on the site are randomly assigned for demo purposes and don't reflect real book data.