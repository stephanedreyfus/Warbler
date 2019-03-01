"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os

from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, FollowersFollowee
from flask_bcrypt import Bcrypt

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app

db.create_all()


class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test message, add sample data."""

        db.session.rollback()
        User.query.delete()
        Message.query.delete()
        FollowersFollowee.query.delete()

        u = User(
            id=10000,
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        self.client = app.test_client()

    def test_message_model(self):
        """ Test basic functionality of message model. """

        t = Message(id=10000,
                    text="Something about Mexican food.",
                    user_id=10000,
                    )

        db.session.add(t)
        db.session.commit()

        self.assertEqual(t.id, 10000)
        self.assertEqual(t.text, "Something about Mexican food.")
        self.assertEqual(t.user_id, 10000)

    # def test_msg_repr(self):
    #     """ Does repr appear properly?"""

    #     t = Message(id=10000,
    #                 text="Something about Mexican food.",
    #                 user_id=10000,
    #                 )

    #     db.session.add(t)
    #     db.session.commit()

    #     self.assertEqual(repr(t), f'<Message #10000: Something about Mexican food., {t.timestamp}, 10000>')
