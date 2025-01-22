# treat_ui

## Project Setup

```shell
poetry install
```


## Repository Design

Everything starts witth a `site`. 
A `site` class 

- inherits from the `BaseUISite` class
- has attributes for each page within the site
- includes higher level business functions

Tests should import the site and everything a test needs to interact with is contained within the site class.




## Future Improvements:

- Locators: Better handling of different locator strategies
- 


## Dockerised Browsers


```shell
docker-compose -f treat_ui/docker/docker-compose.yaml up -d
```

**Future**: The building and running of the browser docker containers can be included in to the repo to ensure they are available without requiring user intervention.


# o document

dev vs running e.g. debug vs simple
