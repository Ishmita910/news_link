from flask import Flask,render_template


app = Flask(__name__)
@app.route('/check')
def flaggingScript():

    return event.event_type


@app.route('/')
def index():
    
    with open('TP2M_status.txt', 'r') as TP2M_content:
        TP2M_content=TP2M_content.read().replace('\n', ' ')
        TP2M_content = TP2M_content.replace('\t', ' ')
        TP2M_content=TP2M_content.split()

        TP2M_content_list1 = TP2M_content[1:8]
        TP2M_content_list2 = TP2M_content[9:16]
        TP2M_content_list3 = TP2M_content[17:24]
        TP2M_content_list4 = TP2M_content[25:32]





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
            <th style="width: 15%" class="cell_header_blue">I P</th>
            <th style="width: 20%" class="cell_header_blue">Host</th>
          </tr>
        _ROWS_
        </table>
        '''

    with open('ReEDS_status.txt', 'r') as ReEDS_content:
        ReEDS_content=ReEDS_content.read().replace('\n', ' ')
        ReEDS_content = ReEDS_content.replace('\t', ' ')
        ReEDS_content=ReEDS_content.split()

        ReEDS_content_list1=ReEDS_content[1:8]
        ReEDS_content_list2 = ReEDS_content[9:16]
        ReEDS_content_list3= ReEDS_content[17:24]
        ReEDS_content_list4 = ReEDS_content[25:32]
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

    return render_template('index.html',ReEDS_content_list1=ReEDS_content_list1,ReEDS_content_list2=ReEDS_content_list2,ReEDS_content_list3=ReEDS_content_list3,ReEDS_content_list4=ReEDS_content_list4,TP2M_content_list1=TP2M_content_list1,TP2M_content_list2=TP2M_content_list2,TP2M_content_list3=TP2M_content_list3,TP2M_content_list4=TP2M_content_list4,html_ReEDS_content=html_ReEDS_content)



if __name__ == '__main__':

    app.run(threaded=True)


