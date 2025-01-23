# treat_ui

## Environment Setup

Note: The instructions below are primarily aimed at MacOS and if being executed on other OS's then may need modifying.

### Poetry Setup (Preferred)

The project can be setup using [Poetry](https://python-poetry.org/docs/#installation).
If Poetry is installed follow the commands below else refer to the [pip setup](#pip-section) section.

```shell
# Create poetry virtual environment and install project dependencies
poetry install
```

### Pip Setup

The project can be setup without Poetry. Follow the steps below

```shell
# Create a python virtual environment
python3 -m venv .venv
# Activate the viirttual environment
source .venv/bin/activate
# Install project dependencies
.venv/bin/pip3 install -r requirements.txt
```


## Test Execution

The tests within this repo can be executed using the below commands:

```shell
# Execute all UI tests related to login functtionality/page
poetry run pytest -m login

# Execute all UI tests in parallel
poetry run pytest -n auto -m ui

```

**Note:** If the pip setup was followed then instead of `poetry run pytest` in the command above, use `.venv/bin/pytest`.

E.g.
```shell
.venv/bin/pytest -m login
```


## Repository Design

Everything starts with a `site`.
A `site` class 

- inherits from the `BaseUISite` class
- has attributes for each page within the site
- includes higher level business functions

Tests should import the site and everything a test needs to interact with is contained within the site class.

Individual pages inherit from the `BaseUIPage` class.

Locators for page objects are defined using the `Locator` class and are included in the page class.

## Configuration

A central configuration mechanism can be implemented to allow the simpler selection of predefined configuraations.

E.g. 
- A configuration to run on latest chrome with large resolution.
- A configuration to run on old firefox with small resolution.

### Browsers Configuration

Different browser support can be added through a variety of files that specify the browser type, version and settings.

Configuration settings can be implemented to allow the specification of the required browser settings allowing tests to be executed against the required browser.


### Browser Instances

Support for local browser instances and dockerised browsers is required.

The local browser support is preferable when developing and debugging tests.

To maintain a level of consistency in test execution then specific browsers within docker images helps to achieve this.


## Data

For data driven capabilities, then the test data will need to be defined in a consistent format. E.g. JSON, YAML or csv.

The repository can then process the data and provide it to the required test.

This allows for increased test scenarios without code duplication.


## Future Improvements:

- Locators: Better handling of different locator strategies
- Browser Configurations:
