import base64


class Base64Tool:
    def image_to_string(file_path):
        with open(file_path, "rb") as file:
            file_data = file.read()
            base64_encoded_data = base64.b64encode(file_data).decode("utf-8")
            return base64_encoded_data
