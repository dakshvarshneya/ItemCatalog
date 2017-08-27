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
User1 = User(name="Daksh Varshneya",
              email="dakshvarshneya7@gmail.com",
              picture='static\img\blank_user.gif')
session.add(User1)
session.commit()

## User2 = User(name="Renado Gress",
##               email="rgress1@t.co",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User2)
## session.commit()


# Create fake categories
Category1 = Category(name="Football",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Gadgets",
                      user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name="Food",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Cricket",
                      user_id=1)
session.add(Category4)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Helmet",
               date=datetime.datetime.now(),
               description="Unmatched protection, High tensile steel bars, Vents for heat dissipation",
               picture="http://www.khelmart.com/Cricket/zoomer_Image/SS_HL_0001_large.jpg",
               category_id=4,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Barcelona Shirt",
               date=datetime.datetime.now(),
               description="Navex Footbal Jersey, Club Barcelona Football Kit",
               picture="http://www.prodirectsoccer.com/productimages/V3_1_Main/108163.jpg",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Chicken Tikka",
               date=datetime.datetime.now(),
               description="Chicken tikka is a chicken dish originating in the Punjab region of the Indian Subcontinent; the dish is popular in India and Pakistan",
               picture="http://cdn.awesomecuisine.com/wp-content/uploads/2015/09/grilled_chicken_tikka.jpg",
               category_id=3,
               user_id=1)
session.add(Item3)
session.commit()

print "Your database has been populated with sample data!"
