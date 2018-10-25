from flask import Flask,render_template
# import tablib
# from string import rstrip


app = Flask(__name__)
@app.route('/check')
def flaggingScript():

    return event.event_type


@app.route('/')
def index():
    #TP2M_content= tablib.Dataset()
    
    with open("TP2M_status.txt", "r") as file:
        TP2M_content=file.read()
        TP2M_content = file.readlines()


        TP2M_content=str(TP2M_content)
        TP2M_content = TP2M_content.replace(",", "<br>")

        html_TP2M_content = '''
        <table class="table_top">
          <tr>
            <th class="cell_header_blue" colspan="6"><span style="font-size:larger;">_SET_</span>
        	<a href="" class="refresh-log">(Refresh Now:</a> Auto-refresh interval is 1 hour)</th>
          </tr>
          <tr>
            <th style="width: 35%" class="cell_header_blue">Simulation ID</th>
            <th style="width:  5%" class="cell_header_blue">Move</th>
            <th style="width: 10%" class="cell_header_blue">Action</th>
            <th style="width: 15%" class="cell_header_blue">Date Uploaded</th>
            <th style="width: 15%" class="cell_header_blue">IP</th>
            <th style="width: 20%" class="cell_header_blue">Host</th>
          </tr>
        _ROWS_
        </table>
        '''
        html_TP2M_content +=TP2M_content
    with open("ReEDS_status.txt", "r") as file:
        ReEDS_content = file.readlines()
        ReEDS_content=str(ReEDS_content)
       
        ReEDS_content = ReEDS_content.replace(",", "<br>")
        html_ReEDS_content = '''
        <table class="table_top">
          <tr>
            <th class="cell_header_blue" colspan="6"><span style="font-size:larger;">_SET_</span>
        	<a href="" class="refresh-log">(Refresh Now:</a> Auto-refresh interval is 1 hour)</th>
          </tr>
          <tr>
            <th style="width: 35%" class="cell_header_blue">Simulation ID</th>
            <th style="width:  5%" class="cell_header_blue">Move</th>
            <th style="width: 10%" class="cell_header_blue">Action</th>
            <th style="width: 15%" class="cell_header_blue">Date Uploaded</th>
            <th style="width: 15%" class="cell_header_blue">IP</th>
            <th style="width: 20%" class="cell_header_blue">Host</th>
          </tr>
        _ROWS_
        </table>
        '''
        html_ReEDS_content +=ReEDS_content
    return render_template('index.html',**locals())



if __name__ == '__main__':

    app.run(threaded=True)


