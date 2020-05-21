from app import dbm
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(5), nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.String(120), nullable=False)
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean)
    shows = db.relationship('Show', cascade='all, delete', backref='venue', lazy='dynamic')

    def __repr__(self):
        return f'<Venue {self.id}, {self.name}, {self.city}, {self.state}, {self.address}, {self.phone}, {self.genres},\
         {self.facebook_link}, {self.seeking_talent}>'

    # implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean)
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', cascade='all, delete', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id}, {self.name}, {self.city}, {self.state}>'


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(Venue.id), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Show {self.id}, {self.artist_id}, {self.venue_id}, {self.start_time}>'

    # implement any missing fields, as a database migration using Flask-Migrate
db.create_all()

# Implement Show and Artist models, and complete all model relationships and properties, as a database migration.