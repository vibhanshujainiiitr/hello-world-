import base64
print(base64.b64decode("SGVsbG8gV29ybGQ=".encode("UTF-8")).decode("UTF-8"))
