import requests
from bs4 import BeautifulSoup
import time

class SteamPriceTracker:
    def __init__(self):
        # We search the Steam store using a standard browser header to avoid blocks
        self.base_url = "https://store.steampowered.com/search/?term="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_game_price(self, game_name):
        """Scrapes Steam search results to find the title and price of a game."""
        # Replace spaces with plus signs for the URL string
        search_url = self.base_url + game_name.replace(" ", "+")
        
        try:
            response = requests.get(search_url, headers=self.headers)
            if response.status_code != 200:
                print("Error: Could not access Steam servers.")
                return None
            
            # Parse the HTML markup
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find the first game container block in search results
            game_row = soup.find("a", class_="search_result_row")
            if not game_row:
                print(f"Could not find any games matching '{game_name}'.")
                return None
            
            # Extract the actual title text
            title_element = game_row.find("span", class_="title")
            title = title_element.text.strip() if title_element else "Unknown Title"
            
            # Extract the final price text
            price_element = game_row.find("div", class_="discount_final_price")
            if not price_element:
                # Check alternative class if game is not on discount
                price_element = game_row.find("div", class_="search_price")
                
            if price_element:
                price_text = price_element.text.strip()
                # Clean up empty spaces or line breaks from HTML output
                price_text = " ".join(price_text.split())
                return {"title": title, "price": price_text}
            else:
                return {"title": title, "price": "Free or Unpriced"}
                
        except Exception as e:
            print(f"An error occurred while parsing: {e}")
            return None

    def check_alert(self, game_name, max_budget):
        """Checks the live price and compares it against your target budget."""
        print(f"\nSearching live data for '{game_name}'...")
        game_data = self.get_game_price(game_name)
        
        if game_data:
            print("-" * 40)
            print(f"Game Match Found: {game_data['title']}")
            print(f"Current Store Price: {game_data['price']}")
            print("-" * 40)
            
            # Simple check: extract numbers from the text to see if it meets budget
            # Removes currency symbols like $, ₹, or text to evaluate numbers safely
            digits = "".join([char for char in game_data['price'] if char.isdigit() or char == '.'])
            
            if digits:
                try:
                    current_price_value = float(digits)
                    if current_price_value <= max_budget:
                        print(f"🚨 DEAL ALERT! {game_data['title']} is within your budget of {max_budget}!")
                    else:
                        print(f"No discount deal yet. It is still higher than your {max_budget} target.")
                except ValueError:
                    print("Could not parse numeric price value to verify budget limit.")
            else:
                print("Price info is non-numeric (Free or Unavailable).")

# --- Main Program Execution ---
if __name__ == "__main__":
    tracker = SteamPriceTracker()
    
    print("=== Welcome to the Industry Steam Price Scraper ===")
    target_game = input("Enter the game name to track (e.g., Elden Ring): ")
    budget = float(input("Enter your target budget price value (as a number): "))
    
    tracker.check_alert(target_game, budget)