Description:

Save certstream tail data.

How to build:

On the path where the dockerfile exists run:
    docker build --tag certificates .

How to execute:
    `docker run --restart unless-stopped -v <local directory>:/usr/src/data certificates`
