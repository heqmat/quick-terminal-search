import requests
from bs4 import BeautifulSoup
import argparse

def retrieveTheContent():
    parser = argparse.ArgumentParser(description='Search texts quickly.')
    parser.add_argument('searched', metavar='S', type=str, nargs='?',
                            help='The text you will search.(Example usage=./qct "how to remove a file in linux")')
    args = parser.parse_args()
    if args.searched == None:
        search_query = input("Enter your search query: ")
        url = 'https://www.google.com/search?q=' + search_query
    else:
        url = 'https://www.google.com/search?q=' + args.searched
    #User agent we're going to use:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_result = soup.find('div', class_='BNeawe').text
        return first_result
    else:
        return "Failed to fetch search results." 

def main():
    first_result = retrieveTheContent()
    print("-"*10)
    
    print(first_result)

if __name__=="__main__":
    main()
