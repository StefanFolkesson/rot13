# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env=jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

alfabete =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabeteU = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw);

    def render_str(self,template,**params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def konvertera(self,texten):
        leftover =""

        for letter in texten:
            if letter in alfabete:
                newletter=alfabete[(alfabete.index(letter)+13)%26]
                leftover+=newletter
            elif letter in alfabeteU:
                newletter=alfabeteU[(alfabeteU.index(letter)+13)%26]
                leftover+=newletter
            else:
                leftover+=letter
        return leftover


class MainHandler(Handler):
    def get(self):
        self.render("rot13.html")

    def post(self):
        texten = self.request.get('text');
        self.render("rot13.html",texten= self.konvertera(texten))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
