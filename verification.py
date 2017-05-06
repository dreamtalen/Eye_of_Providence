import requests

def verification(face_id, face2_id):
    data = {
        "api_id": "8075d09d343d4dbc8fa579364adf1aa0",
        "api_secret": "0bc4e95c39434d44b781d56f3fdb820e",
        "face_id": face_id,
        "face2_id": face2_id
    }
    r = requests.post("https://v1-api.visioncloudapi.com/face/verification", data=data)

    result = r.json()

    return result['same_person']

# if __name__ == '__main__':
#     id_list = ['10db487ca3f04ce1b886a9b314458e1a', 'af023ebaa7b14131b728a624d337b55d', 'bcf2a592846d4a03aa9e1dadc7aa7381']
#     face2_id = '1883215445d34219b4859d17e0c4cf82'
#     for id in id_list:
#         print verification(id, face2_id)