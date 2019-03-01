"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os

from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, FollowersFollowee
from flask_bcrypt import Bcrypt

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.session.rollback()
        User.query.delete()
        Message.query.delete()
        FollowersFollowee.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_user_model_repr(self):
        """ Does repr return correct values? """

        u = User(
            id=10000,
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        self.assertEqual(repr(u), '<User #10000: testuser, test@test.com>')

    def test_is_following(self):
        """ Can user1 follow user2? """

        u1 = User(
            id=10000,
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            id=15000,
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        follow = FollowersFollowee(
            followee_id=10000,
            follower_id=15000,
        )

        db.session.add(follow)
        db.session.commit()

        self.assertEqual(u1.is_following(u2), True)

    def test_is_not_following(self):
        """ Confirm user1 is NOT following user2. """

        u1 = User(
            id=10000,
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            id=15000,
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(u1.is_following(u2), False)

    def test_is_followed_by(self):
        """ Is user1 followed by user2? """

        u1 = User(
            id=10000,
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            id=15000,
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        follow = FollowersFollowee(
            followee_id=10000,
            follower_id=15000,
        )

        db.session.add(follow)
        db.session.commit()

        self.assertEqual(u2.is_followed_by(u1), True)

    def test_is_not_followed_by(self):
        """ Confirm user1 is NOT following user2. """

        u1 = User(
            id=10000,
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            id=15000,
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(u2.is_followed_by(u1), False)

    def test_user_create(self):
        """ Is the user instance properly created? """

        u1 = User(
            id=10000,
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.commit()

        self.assertEqual(u1.id, 10000)
        self.assertEqual(u1.email, "user1@test.com")
        self.assertEqual(u1.username, "user1")
        self.assertEqual(u1.password, "HASHED_PASSWORD")

    def test_user_create_invalid(self):
        """ If user instance is passed invalid values, no user is created. """

        u1 = User(
            id=50000,
            email=None,
            username="user1",
            password="HASH"
        )

        db.session.add(u1)

        self.assertRaises(IntegrityError, db.session.commit)
        db.session.rollback()
        self.assertEqual(User.query.get(50000), None)

############################################################################

    def test_user_authenticate(self):
        """ Does authenticate return a user when given valid input? """

        u1 = User.signup(
            email="user1@test.com",
            username="user1",
            password="taco",
            image_url="quesadilla"
        )

        db.session.add(u1)
        db.session.commit()

        self.assertEqual(u1.authenticate("user1", "taco"), u1)

    def test_user_auth_username_fail(self):
        """ Does authenticate return a user when given valid input? """

        u1 = User.signup(
            email="user1@test.com",
            username="user1",
            password="taco",
            image_url="quesadilla"
        )

        db.session.add(u1)
        db.session.commit()

        self.assertEqual(u1.authenticate("u2", "taco"), False)

    def test_user_auth_pwd_fail(self):
        """ Does authenticate return a user when given valid input? """

        u1 = User.signup(
            email="user1@test.com",
            username="user1",
            password="taco",
            image_url="quesadilla"
        )

        db.session.add(u1)
        db.session.commit()

        self.assertEqual(u1.authenticate("user1", "burrito"), False)
