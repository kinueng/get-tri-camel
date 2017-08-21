#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

def main():
    priceMaxMin()
    priceChange()
    sys.exit(0)

def priceMaxMin():
    ccc_base_url = "http://camelcamelcamel.com/search?sq="
    amazon_url = str(sys.argv[1])
    print amazon_url
    r = requests.get(ccc_base_url + amazon_url)
    rr = requests.get(r.url)
    soup = BeautifulSoup(rr.text, 'html.parser')

    print "\n---------------"
    current = soup.select("#section_amazon table tbody tr")[0]
    for line in current.text.splitlines():
        line = line.strip(' \t\n\r')
        if line:
            print line
    print "---------------"

    highest = soup.select("#section_amazon .highest_price")[0]
    for line in highest.text.splitlines():
        line = line.strip(' \t\n\r')
        if line:
            print line
    print "---------------"

    lowest = soup.select("#section_amazon .lowest_price")[0]
    for line in lowest.text.splitlines():
        line = line.strip(' \t\n\r')
        if line:
            print line

def priceChange():
    ccc_base_url = "http://camelcamelcamel.com/search?sq="
    amazon_url = str(sys.argv[1])
    # print amazon_url
    r = requests.get(ccc_base_url + amazon_url)
    # print r.url
    rr = requests.get(r.url)
    soup = BeautifulSoup(rr.text, 'html.parser')

    print "---------------"
    current = soup.select("#section_amazon table")[1]
    rawText = current.text
    for line in rawText.splitlines():
        line = line.strip(' \t\n\r')
        if line:
            print line

    print "---------------"

if __name__ == '__main__':
    main()
