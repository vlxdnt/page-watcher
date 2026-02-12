import requests
import hashlib
import time
import os
import platform
from datetime import datetime
from bs4 import BeautifulSoup


URL = "https://www.example.com" # Replace with the URL you want to monitor
INTERVAL = 60 # In seconds, adjust as needed

def get_page_hash(URL):
    headers = { # Set a user-agent to mimic a browser request and avoid potential blocking by the server
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()

        # Checks if the content is a webpage or a raw file (CSV, PDF, etc.)
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' in content_type:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Removes dynamic elements that change constantly or aren't "page content"
            for element in soup(["script", "style" , "nav", "footer", "header", "aside"]):
                element.decompose()

            # Get only the text content
            clean_text = soup.get_text(separator=' ', strip=True)
            return hashlib.md5(clean_text.encode('utf-8')).hexdigest()
        
        else: # Raw hashing for files
            return hashlib.md5(response.content).hexdigest()
        
    except Exception as e:
        print(f"Error fetching the page: {e}")
        return None
    
def play_buzzer(): 
    for _ in range(3):
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            os.system('echo -n "\a"; sleep 0.5; echo -n "\a"')
    
def main():
    print(f"Monitoring page for changes every {INTERVAL} seconds...")
    last_hash = get_page_hash(URL)

    if not last_hash:
        print("Failed to get initial page hash. Exiting.")
        return
    
    while True:
        time.sleep(INTERVAL)
        current_hash = get_page_hash(URL)

        if current_hash and current_hash != last_hash:
            print(f"Page changed at {datetime.now()}")
            play_buzzer()
            last_hash = current_hash

        elif current_hash:
            print("No change yet...")

if __name__ == "__main__":
    main()
