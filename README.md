# LAB - Class 17

## Project: Web Scraper

### Author: Christopher Yamas

### Setup

#### How to run application

Within module `scraper.py`, there are two functions:

- `get_citations_needed_count()` takes in a url string for a particular Wikipedia page, and returns the number of passages in the article that are marked with a "citation needed" tag
- `get_citations_needed_report()` takes in a url string for a particular Wikipedia page, and returns the particular paragraphs/passages in the article that are marked with a "citation needed" tag

### Example

- If the url for the Wikipedia page about computer scientist and transgender activist Lynn Conway ("https://en.wikipedia.org/wiki/Lynn_Conway") passed into the `get_citations_needed_count()` function, it would return `1` because there is just one "citation needed" tag in that article.
- If the same url was passed into the `get_citations_needed_report()` function, it would return the string of that one passage:
  - Conway grew up in White Plains, New York. Conway was shy and experienced gender dysphoria as a child. She became fascinated by astronomy (building a 6-inch (150 mm) reflector telescope one summer) and did well in math and science in high school. Conway entered MIT in 1955, earning high grades but ultimately leaving in despair after an attempted gender transition in 1957–58 failed due to the medical climate at the time.[citation needed] After working as an electronics technician for several years, Conway resumed education at Columbia University's School of Engineering and Applied Science, earning B.S. and M.S.E.E. degrees in 1962 and 1963.[12][13]
