#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup

def parse_file(filename):
    # Open and parse the HTML file
    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Find all <a> tags with href containing '/cgi/cbook.cgi'
    for a in soup.find_all("a", href=True):
        if "/cgi/cbook.cgi" in a["href"]:
            text = a.get_text().strip()
            if text:
                print(text)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <html_filename>")
        sys.exit(1)

    filename = sys.argv[1]
    parse_file(filename)

if __name__ == "__main__":
    main()

