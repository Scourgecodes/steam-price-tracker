# Industry Web Scraper: Steam Game Price Tracker

An interactive, terminal-based Python data application designed to extract live pricing structures from the Steam store and evaluate data inputs against a target financial budget.

---

## Technical Overview

This project demonstrates core data engineering and web scraping techniques. The script programmatically fires network requests to live online servers, pulls down raw HTML markup text, and uses nested HTML parsing trees to extract precise text nodes. This replaces the need for a formal data API.

### Key Features
* **Live HTML Parsing:** Uses BeautifulSoup to isolate web classes like `search_result_row` and `discount_final_price`.
* **Request Customization:** Implements a custom browser User-Agent header string to bypass standard server automated blocks.
* **String Manipulation Filters:** Automatically cleans and formats web text strings, removing hidden spaces and line breaks.
* **Dynamic Budget Matching:** Isolates numeric floating values out of messy currency text fields to calculate discount alerts cleanly.

---

## Technology Stack

* **Language Platform:** Python 3
* **Libraries Used:**
  * `requests` — Handles backend HTTP data transfers with external web servers.
  * `beautifulsoup4` — Parses raw HTML text data into a readable object tree structure.

---

## Operational Guide

1. Open your Anaconda Prompt terminal.
2. Route your terminal path to your project workspace:
   ```bash
   cd OneDrive\Desktop\AI_Agents
