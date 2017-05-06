import requests

def detection(url):
    data = {
        "api_id": "8075d09d343d4dbc8fa579364adf1aa0",
        "api_secret": "0bc4e95c39434d44b781d56f3fdb820e",
        "url": url,
        "attributes": 1
    }
    r = requests.post("https://v1-api.visioncloudapi.com/face/detection", data=data)

    result = r.json()

    face_id_emotion_dict = {}
    face_id_eye_open_dict = {}

    if not result['faces']:
        print "No face detected in this picture"
    else:
        for face in result['faces']:
            id = face["face_id"]
            emotion = max(face["emotions"].keys(), key=lambda x: face["emotions"][x])
            # print face["emotions"]
            eye_open = face["attributes"]["eye_open"]
            face_id_emotion_dict[id] = emotion
            face_id_eye_open_dict[id] = eye_open > 50

    return face_id_emotion_dict, face_id_eye_open_dict
#
# if __name__ == '__main__':
#     face_id_emotion_dict, face_id_eye_open_dict = detection("https://ooo.0o0.ooo/2017/05/06/590d4b2be7f5f.jpeg")
#     print face_id_emotion_dict, face_id_eye_open_dict
