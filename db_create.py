from project import db
from project.models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 2))
db.session.add(BlogPost("Excellent", "I\'m excellent.",1))
db.session.add(BlogPost("Okay", "I\'m okay.",1))
db.session.add(BlogPost("postgres", "we setup a local postgres instance",1))

# commit the changes
db.session.commit()
