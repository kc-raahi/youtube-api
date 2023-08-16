import json
import os


class URLStorage:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(filename):
            with open(self.filename, 'r') as f:
                existing_arr = json.load(f)
                self.existing = set(existing_arr)
        else:
            self.existing = set()

    def close(self):
        with open(self.filename, 'w') as f:
            existing_arr = list(self.existing)
            json.dump(existing_arr, f)

    def already_used(self, url):
        return url in self.existing

    def add_used_url(self, url):
        self.existing.add(url)

    # def add_to_urls(self, url_list, existing_urls, dl_ct=10):
    #     while dl_ct > 0:
    #         r = random.randint(0, len(url_list) - 1)
    #         u = url_list[r]
    #         if u not in existing_urls:
    #             existing_urls.append(u)
    #             url_list.remove(u)
    #             dl_ct -= 1
    #
    #     return url_list, existing_urls
