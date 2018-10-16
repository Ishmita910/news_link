from flask import Flask,render_template

app = Flask(__name__)


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for debug
    def on_modified(self, event):
        index()
        self.process(event)
   

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    app.run(threaded=True)