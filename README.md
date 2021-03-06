# Web Scraper/Data API

## Project Info

### Tech Stack

`Python 3.9.2` <br>
`BeautifulSoup4` <br>
`Matplotlib`

### Project Purpose

I made this project to learn python and web scraping technologies, as well as learning to connect it to a frontend using an API.

### Project Outcome

This is a very small yet effective script that pulls information about stock market indices and uses it to show the latest market movement. In making it I learned how to: write more pythonic code, simplify loops and if statements using list comprehension, and simplifying nested lists into dictionaries.

## How to Run

`Note: Steps 1 and 2 are only needed for first time setup.`

### Step 1

Install Python for your system:  
https://wiki.python.org/moin/BeginnersGuide/Download

### Step 2

Download the repo from github:

```bash
  $ cd #whatever directory you want to install into
  $ git clone https://github.com/aaronrine/web-scraper.git
```

### Step 3

Setup and start the virtual environment:

```bash
  $ python -m venv venv
  $ source venv/bin/activate
  #For first time setup only
  $ pip install -r requirements.txt
```

### Step 4

Run the Script:

```bash
  $ python scraper.py
```

### Step 5

Exit the virtual environment when you are finished using the program:

```bash
  $ deactivate
```
