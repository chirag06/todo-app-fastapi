import requests
import json
class My_funtions():
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"
    def add(self, task, description = None):
        r = requests.post(self.url+'items/', json ={'title':task, 'description': description})
        print("Following task added")
        return r
    def done(self, task_id):
        r = self.update(task_id, "status", "1")
        print("Following task completed")
        return r
    def show(self, task_id):
        r = requests.get(self.url+'item/'+str(task_id))
        return r
    def tasks_status(self, tasks_status):
        r = requests.get(self.url+'items/'+str(tasks_status))
        return r
    def all(self):
        r = requests.get(self.url+'all/')
        return r
    def update(self, task_id, update_key, update_value):
        r = self.show(task_id)
        json_obj = json.loads(r.content)
        json_obj[update_key] = update_value
        r = requests.put(self.url+'items', json = json_obj)
        return r
