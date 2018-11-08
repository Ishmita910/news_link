from flask import Flask,render_template
import time
import sys
import logging
import datetime as dt


from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' |  'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        print(event.src_path, event.event_type)  # print now only for debug

    def on_modified(self, event):
        self.process(event)


app = Flask(__name__)
@app.route('/check')
def flaggingScript():
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
            # print('checking')
    except KeyboardInterrupt:
        observer.stop()

    observer.join()




@app.route('/')
def index():
    
    with open('TP2M_status.txt', 'r') as TP2M_content:
        TP2M_content=TP2M_content.read().replace('\n', ' ')
        TP2M_content = TP2M_content.replace('\t', ' ')
        TP2M_content=TP2M_content.split()

        TP2M_content_list1 = TP2M_content[0:7]
        TP2M_content_list2 = TP2M_content[8:15]
        TP2M_content_list3 = TP2M_content[16:23]
        TP2M_content_list4 = TP2M_content[24:31]



    with open('ReEDS_status.txt', 'r') as ReEDS_content:
        ReEDS_content=ReEDS_content.read().replace('\n', ' ')
        ReEDS_content = ReEDS_content.replace('\t', ' ')
        ReEDS_content=ReEDS_content.split()

        ReEDS_content_list1=ReEDS_content[0:6]
        ReEDS_content_list2 = ReEDS_content[8:14]
        ReEDS_content_list3= ReEDS_content[16:22]
        ReEDS_content_list4 = ReEDS_content[24:30]


    return render_template('index.html',ReEDS_content_list1=ReEDS_content_list1,ReEDS_content_list2=ReEDS_content_list2,ReEDS_content_list3=ReEDS_content_list3,ReEDS_content_list4=ReEDS_content_list4,TP2M_content_list1=TP2M_content_list1,TP2M_content_list2=TP2M_content_list2,TP2M_content_list3=TP2M_content_list3,TP2M_content_list4=TP2M_content_list4)



if __name__ == '__main__':

    app.run(threaded=True)


