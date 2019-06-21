import json


def read_json(path):
    try:
        file = open(path, encoding="utf8")
        return file
    except Exception as e:
        print(f"Error to read JSON File: {e}")


if __name__ == '__main__':

    response = read_json('reviews_post_facebook_test.json')
