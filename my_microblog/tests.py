from datetime import datetime, timedelta
import unittest
import hashlib
from app import app, db
from app.models import User, Posts

class UserModelCase (unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hash(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar (self):
        u = User(username='john', email='john@example.com')
        digest = hashlib.md5(u.email.lower().encode('utf-8')).hexdigest()
        expected_url = f'https://www.gravatar.com/avatar/{digest}?d=identicon&s=128'
        self.assertEqual(u.avatar(128), expected_url)

    def test_follow(self):
        u1=User(username='john', email='john@example.com')
        u2=User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u1.followers.count(), 0)

    def test_follow_posts(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='anna', email='anna@example.com')
        u4 = User(username='tom', email='tom@example.com')
        db.session.add_all([u1, u2, u3, u4])

        now=datetime.utcnow()
        p1 = Posts(body='post from john', author=u1, 
                   timestamp=now + timedelta(seconds=1))
        p2 = Posts(body='post from susan', author=u2, 
                   timestamp=now + timedelta(seconds=4))
        p3  = Posts(body='post from anna', author=u3, 
                    timestamp=now + timedelta(seconds=3))
        p4 = Posts(body='post from tom', author=u4, 
                   timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
