import unittest
from app.models import Blog, Writer

class BlogModelTest(unittest.TestCase):

    def SetUp(self):
        self.new_writer = Writer(fullname = "Bella", email = "bella@example.com", password = "1234")
        self.new_blog = Blog(blog_messsage = "bla blaaah", writer_id = self.new_writer.id)
        
    def tearDown(self):
        Blog.query.delete()
        Writer.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_writer.fullname, "Bella")

    def test_create_blog(self):
        self.new_blog.create_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_single_blog(self):
        self.new_blog.create_blog()
        got_blog = self.new_blog.get_single_blog()
        self.assertEquals("bla blaaah", self.new_blog.blog_message)