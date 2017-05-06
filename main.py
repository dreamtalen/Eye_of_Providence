import detection

url = "https://ooo.0o0.ooo/2017/05/06/590d4b2be7f5f.jpeg"
face_id_emotion_dict, face_id_eye_open_dict = detection.detection(url=url)
print face_id_emotion_dict
print face_id_eye_open_dict

