Description:

Client to save lists of filters available at filterlists.com

How to build:

On the path where the dockerfile exists run:
    docker build --tag filter-list-scrapper .

How to execute:
    docker run -v <local directory>:/usr/src/data filter-list-scrapper
