from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Bhatti Bhai",
             email="bobbynarang1970@gmail.com",
             picture='static\img\blank_user.gif')
session.add(User1)
session.commit()

# User2 = User(name="Modi",
#               email="modi@bjp.co",
#               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
# session.add(User2)
# session.commit()


# Create fake categories
Category1 = Category(name="Football",
                     user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Cars",
                     user_id=2)
session.add(Category2)
session.commit

Category3 = Category(name="Gadgets",
                     user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Food",
                     user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Cricket",
                     user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Mongoose Bat",
              date=datetime.datetime.now(),
              description="ceat size 6 Poplar Willow Cricket Bat  (6,700 g)",
              picture="https://rukminim1.flixcart.com/image/832/832/j1l10nk0/bat/y/z/d/700-size-5-5-na-ceat-original-imaestuqrtzgfsng.jpeg?q=70",
              category_id=5,
              user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Real Madrid Shirt",
              date=datetime.datetime.now(),
              description="""Navex Navex Footbal Jersey Club Real Madrid
                             White Full Sleeve Ket L Football Kit""",
              picture="https://rukminim1.flixcart.com/image/832/832/j0tvngw0/kit/c/w/d/navex-footbal-jersey-club-real-madrid-white-full-sleeve-ket-l-original-imaesdxybejvmemh.jpeg?q=70",
              category_id=1,
              user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Chicken lollypop",
              date=datetime.datetime.now(),
              description="""Chicken lollipop is an hors d'oeuvre popular in Indian Chinese cuisine.
                             Chicken lollipop is,
                             essentially a frenched chicken winglet,
                             where in the meat is cut loose
                             from the bone end and pushed down
                             creating a lollipop appearance""",
              picture="https://i.ytimg.com/vi/0bYYU3X10Sw/maxresdefault.jpg",
              category_id=4,
              user_id=1)
session.add(Item3)
session.commit()

print "fake data added to catalog.db!"
