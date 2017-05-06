# -*- coding: utf-8 -*-
import os
import tornado
import tornado.web
import tornado.httpserver

import detection


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomeHandler),
            (r'/detect', DetectHandler),
            (r'/history', HistoryHandler)

        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            debug=True
        )
        super(Application, self).__init__(handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', title='eyes', content='hiiiiii')


class HistoryHandler(tornado.web.RequestHandler):
    def get(self):
        pass


class DetectHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.request.body
        face_id_emotion_dict, face_id_eye_open_dict = detection.detection(url)
        print face_id_emotion_dict, face_id_eye_open_dict
        self.write("ok")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(9999)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
