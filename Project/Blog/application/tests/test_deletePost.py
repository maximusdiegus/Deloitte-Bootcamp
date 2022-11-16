from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import User, Post
from application.forms import AddUser

class TestBase(LiveServerTestCase):
    TEST_PORT = 5000 # test port, doesn't need to be open

    def create_app(self):

        
        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):

        # Create table
        db.create_all()
        # Create test registree
        sample1 = User(username="Diego", password="hey")
        # save users to database
        db.session.add(sample1)
        db.session.commit()
    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/update-question/1')
        self.assertEqual(response.code, 200)
        
class TestDelete(TestBase):
    def submit_input(self, case): # custom method
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/value[@lang="delete"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_delete(self):
         self.submit_input("id")

         entry = Post.query.filter_by(id="id").all()
         self.assertNotEqual(entry, None) 