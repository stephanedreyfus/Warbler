# Warbler

## About

[This web app](https://kittensmurfwarbler.herokuapp.com/) is a clone of the popular social platform Twitter.

Users can log in a send "warbles," micro blogs or messages, out in the Warblesphere, where other users can then like (or unlike) the tweets. Users can follow their favorite warblers to better follow all their warbles.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This app's dependencies are listed in `requirements.txt`. 

### Installing

* Make a virtual environment: `mkvirtualenv <NAME>`.
* Make the `warbler` database: `createdb warbler`.
* Pip install the requirements: `pip install -r requirements.txt`.
* Seed the database with by running the `create_csvs.py` file.

## Running the tests

To run a tests (if you want to debug with iPython):
`python -m unittest` with in the root of the project.

To run a specific test:
`python -m unittest <name_of_test>`.

## Deployment

To deploy this on a live system, follow the instructions [here](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).


## Built With

* [Python](https://www.python.org/) - Used for server-side development
* [Flask](http://flask.pocoo.org/) - Python microframeworkrecommendations
* [SQLAlchemy](https://www.sqlalchemy.org/) - Used for database manipulation
* [jQuery](http://jquery.com/) - Used to manipulate the DOM and make AJAX calls
* CSS
* HTML

## Contributing

This is a personal project that is only rarely updated by myself and my fellow conributor. We are not accepting other contributions.

## Versioning

Git was used for versioning. For the versions available, see this repository.

## Authors

* **Katie Krieger**
* **Annika Lund**
* **Rithm 10 Staff**

## License

This project is licensed under the MIT License.

Copyright 2017 Katie Krieger

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgements

* Special thanks to Elie, Matt, and Tim at [Rithm School](http://rithmschool.com/) for their support and guidance.
* Thanks to Annika Lund, for being patient and super knowledgeable, and being a great coding partner.

