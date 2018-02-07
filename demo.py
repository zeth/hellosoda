#!/usr/bin/python3
"""Very quickly written app.

Would not serve static files through Python normally but doing it for
ease of the user.
"""

import json

import tornado.ioloop
import tornado.web
from tornado.log import enable_pretty_logging

STATIC_PATH_DIR = "soda/"


class People(tornado.web.RequestHandler):
    """Send the list of people to the client.
    NOTE: It would be nice to flatten the data a bit."""
    def initialize(self):
        with open('people.json') as people_fp:
            self.people = json.load(people_fp)['people']

    def get(self, *args, **kwargs):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')
        self.write(json.dumps(self.people))


class Person(tornado.web.RequestHandler):
    """Send a single person data object to the client."""
    def initialize(self):
        with open('people.json') as people_fp:
            people = json.load(people_fp)['people']
        self.people = {person['id']: person for person in people}

    def get(self, person_id, *args, **kwargs):
        self.set_header("Content-Type", 'application/json; charset="utf-8"')
        person_data = json.dumps(self.people[int(person_id)])
        self.write(person_data)
        # TODO: Use logging module
        print("User selected person %s." % person_id)


def make_app():
    """Set the routes."""
    return tornado.web.Application([
        (r'/api/person/people', People),
        (r"/api/person/(?P<person_id>\w+)", Person),
        (r'/(.*)', tornado.web.StaticFileHandler,
         {'path': STATIC_PATH_DIR,
          "default_filename": "index.html"}),
    ])


def main():
    """Run the app when started as a script."""
    enable_pretty_logging()
    print("Please visit http://localhost:8888 in your browser.")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
