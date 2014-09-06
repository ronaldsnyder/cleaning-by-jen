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
    
    def post(self):
        
        myname = self.request.get('myname')
        myphone = self.request.get("myphone")
        myemail = self.request.get("myemail")
        comments = self.request.get("comments")

        mail.send_mail(sender="ronalddsnyder@gmail.com",
                      #to="Jcarpenter481@hotmail.com",
                      to="ronalddsnyder@gmail.com",
                      subject="Cleaning By Jen Inquiry",
                      body="""You have a new inquiry from cleaningbyjen.com.
        Name: %s
        Phone: %s
        Email: %s
        Comment:  %s
                      
        
        """ % (myname, myphone, myemail, comments))
        
        template_values = {
            'path': jinja_environment,
            'myname': myname,
            'myphone': myphone,
            'myemail': myemail,
            'comments': comments,
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