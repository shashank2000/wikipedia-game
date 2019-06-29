import requests
from bs4 import BeautifulSoup

def get_links(url):
    """This method gets the links contained in the body of the given url.
    The URL is assumed to be a wikipedia page. This method returns a list of links as strings.
    """
    links = []
    soup = BeautifulSoup(url, 'html.parser')
    for link in soup.find_all('a'):
        if "wiki" in link:
            links.append(link)
    return links
        
def run_bfs(end_url, start_url):
    """Run BFS to find the shortest path from start_url to end_url by clicking
    links on the page. This method returns a list of links one needs to click to get
    from start_url to end_url.
    """
    pass

if __name__ == "__main__":
    kevin_bacon_url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
    start_url = "https://en.wikipedia.org/wiki/Nicole_Kassell"
    run_bfs(kevin_bacon_url, start_url)
