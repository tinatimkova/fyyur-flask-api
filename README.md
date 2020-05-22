Fyyur
-----

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner. Fyyur is designed as a platform that artists and musical venues can use to find each other, and discover new music shows.

### User stories:
  * when a user submits a new artist record, the user should be able to see it populate in /artists;
  * when a user submits a new venue form, the user should be able to see it populated in /venues;
  * when a user submits a new show form, the user should be able to see it created in /shows;
  * a user should be able to search for the artist or the venue by name and have the search return results. Search should be partial string matching and case-insensitive;
  * a user should be able to visit a particular artist’s or venue's page;
  * a user should be able to update information about a particular artist or venue;
  * a user can see venues displayed in groups by city and state;
  * a user can see past shows and upcoming shows distinguished in venue and artist pages;
  * a user should be able to click on the venue for an upcoming show in the Artist's page, and on that Venue's page, see the same show in the Venue Page's upcoming shows section;
  * a user should be able to delete a particular artist or venue.

### Development process

While the views and controllers were defined in this application, I built out the data models and model interactions to be able to store, retrieve and update data from a PostgreSQL database.

The development process included the following steps:
1. Connecting the app to a database in `config.py`
2. Setting up normalized models using SQLAlchemy
3. Implementing model properties and relationships using database migrations via Flask-Migrate
3. Implementing form submissions for creating new Venues, Artists, and Shows
4. Implementing the controllers for listing venues, artists, and shows
5. Implementing search, powering the `/search` endpoints that serve the application's search functionalities
6. Completing venue and artist detail pages, powering the `<venue|artist>/<id>` endpoints.

### Technologies used

* **SQLAlchemy ORM** - ORM library of choice
* **PostgreSQL** - database of choice
* **Python3** and **Flask** - server language and server framework
* **Flask-Migrate** - creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for the website's frontend

### Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes my SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** My forms
  ├── requirements.txt *** The dependencies I need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```

Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`

##### Stretch goals

*  Implement artist availability. An artist can list available times that they can be booked. Restrict venues from being able to create shows with artists during a show time that is outside of their availability.
* Show Recent Listed Artists and Recently Listed Venues on the homepage, returning results for Artists and Venues sorting by newly created. Limit to the 10 most recently listed items.
* Implement Search Artists by City and State, and Search Venues by City and State. Searching by "San Francisco, CA" should return all artists or venues in San Francisco, CA.

### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask).

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```
2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
3. Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```
4. Navigate to Home page [http://localhost:5000](http://localhost:5000)
