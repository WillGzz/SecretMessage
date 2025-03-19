# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def secretMessage(doc_url):
    try:
        response = requests.get(doc_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table')
        rows = table.find_all('tr')

        grid_data = []
        for row_index, row in enumerate(rows[1:]):
            cells = row.find_all('td')
            
            x_span = cells[0].find('span')  
            char_span = cells[1].find('span')  
            y_span = cells[2].find('span')  

            if not x_span:
                print(f"Error: Could not find x-coordinate span in row {row_index + 1}.")
                continue
            if not char_span:
                print(f"Error: Could not find character span in row {row_index + 1}.")
                continue
            if not y_span:
                print(f"Error: Could not find y-coordinate span in row {row_index + 1}.")
                continue

        
            x = int(x_span.text)
            char = char_span.text
            y = int(y_span.text)
            grid_data.append((x, y, char))
       

        if not grid_data:
            print("No valid grid data found in the document.")
            return

        print("Grid data parsed:")
        print(grid_data)

        max_x = max(x for x, y, char in grid_data) 
        max_y = max(y for x, y, char in grid_data) 

        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for x, y, char in grid_data:
            grid[y][x] = char

        print("Message from grid:")
        for row in grid:
            print(''.join(row))


    except requests.exceptions.RequestException as e:
        print(f"Error fetching document: {e}")
# https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub
doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
secretMessage(doc_url)













