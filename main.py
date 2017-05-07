# -*- coding: utf-8 -*-
import os
import tornado
import tornado.web
import tornado.httpserver
import random
import torndb

import detection
import verification
import voice

face_id_name_dict = {"10db487ca3f04ce1b886a9b314458e1a":"Zhang", "af023ebaa7b14131b728a624d337b55d":"Ding", "bcf2a592846d4a03aa9e1dadc7aa7381":"Luo"}
photo_list = ["https://ooo.0o0.ooo/2017/05/06/590d424294629.png", "https://ooo.0o0.ooo/2017/05/06/590d4b2be7f5f.jpeg",
              "https://ooo.0o0.ooo/2017/05/06/590d38b18507f.jpeg","https://ooo.0o0.ooo/2017/05/06/590d767456f4f.jpg"]

db = torndb.Connection(host='127.0.0.1:3306', database='monitor', user='root', password='123456')
Order_list=[]
def Add_Order(decorated):
    """
    装饰器，作callback用
    :param decorated:
    :return:
    """
    Order_list.append(decorated)
    return decorated

@Add_Order
def Order_Sleep(text):
    if 'sleep' not in text:
        return False
    ###DO SOMETHING
    return True


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomeHandler),
            (r'/detect', DetectHandler),
            (r'/history', HistoryHandler),
            (r'/capture', CaptureHandler),
            (r'/record', RecordHandler),
            (r'/analyze', AnalyzeHandler)

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
        self.render('home.html', title='Eye of Providence', content='')


class HistoryHandler(tornado.web.RequestHandler):
    def get(self):
        data = db.query("SELECT * FROM log")
        time_list = [d['ts'] for d in data]
        names_list = [d['names'] for d in data]
        self.render('history.html', title='Eye of Providence', content='', time_list=time_list, names_list=names_list)


class DetectHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.request.body
        face_id_emotion_dict, face_id_eye_open_dict = detection.detection(url)
        # print face_id_emotion_dict, face_id_eye_open_dict
        eye_close_id_list = [id for id in face_id_eye_open_dict.keys() if not face_id_eye_open_dict[id]]
        # print eye_close_id_list
        sleep_ones = []
        for id in eye_close_id_list:
            for known_face_id in face_id_name_dict.keys():
                if verification.verification(id, known_face_id):
                    sleep_ones.append(face_id_name_dict[known_face_id])
        db.execute("""INSERT INTO log(ts, names) VALUES(UTC_TIMESTAMP, %s)""", ",".join(sleep_ones))
        self.write({"id": sleep_ones})

class CaptureHandler(tornado.web.RequestHandler):
    def post(self):
        new_url = random.choice(photo_list)
        # print new_url
        self.write({"new_url": new_url})

class RecordHandler(tornado.web.RequestHandler):
    def post(self):
        url =  self.request.headers['image_url']
        with open('record.wav', 'w') as f:
            f.write(self.request.body)
        result = 'find sleeping students'
        # if 'sleep' in result:

class AnalyzeHandler(tornado.web.RequestHandler):
    def post(self):
        # record_result = 'find sleeping students'
        print 'begin'
        record_result = voice.Voice2Text('record.wav')
        print record_result
        if 'sleep' in record_result:
            url = self.request.body
            face_id_emotion_dict, face_id_eye_open_dict = detection.detection(url)
            # print face_id_emotion_dict, face_id_eye_open_dict
            eye_close_id_list = [id for id in face_id_eye_open_dict.keys() if not face_id_eye_open_dict[id]]
            # print eye_close_id_list
            sleep_ones = []
            for id in eye_close_id_list:
                for known_face_id in face_id_name_dict.keys():
                    if verification.verification(id, known_face_id):
                        sleep_ones.append(face_id_name_dict[known_face_id])
            db.execute("""INSERT INTO log(ts, names) VALUES(UTC_TIMESTAMP, %s)""", ",".join(sleep_ones))
            self.write({"id": sleep_ones, "analyze_result": record_result, "flag": '1'})
        else:
            self.write({"id": [], "analyze_result": record_result, "flag":'0'})


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(9999)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
