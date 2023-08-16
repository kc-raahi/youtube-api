from url_storage import URLStorage

url_storage = URLStorage("myfile.json")
print(url_storage.existing)
url_storage.add_used_url("abc")
url_storage.add_used_url("def")
print(url_storage.existing)
url_storage.close()

