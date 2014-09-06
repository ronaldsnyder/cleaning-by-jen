import webapp2
import cgi
import os
import jinja2
import re
from google.appengine.api import mail
import logging

jinja_environment = jinja2.Environment(autoescape = True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'path': jinja_environment
        }
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render(template_values))
class AboutPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'path': jinja_environment
        }
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render(template_values))
class FAQPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'path': jinja_environment
        }
        template = jinja_environment.get_template('faq.html')
        self.response.out.write(template.render(template_values))
class ServicesPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'path': jinja_environment
        }
        template = jinja_environment.get_template('services.html')
        self.response.out.write(template.render(template_values))
class ContactPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'path': jinja_environment
        }
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render(template_values))
    
    def post(self, myname = None, myphone = None, myemail = None, comments = None):
        message = mail.EmailMessage()
        message.sender = "ronalddsnyder@gmail.com"
        message.subject = "Cleaning By Jen Inquiry"
        message.to = "ronalddsnyder@gmail.com"
        message.body = "This is a pain in the rear"
        message.send()
        template_values = {
            'path': jinja_environment,
        }
        template = jinja_environment.get_template('success.html')
        self.response.out.write(template.render(template_values))
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage),
    ('/faq', FAQPage),
    ('/services', ServicesPage),
    ('/contact', ContactPage),
], debug=True)