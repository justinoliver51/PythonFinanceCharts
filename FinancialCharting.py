import urllib2
import time
import datetime

stocks_to_pull = ['AAPL', 'GOOG', 'MSFT', 'CMG', 'AMZN', 'EBAY', 'TSLA']

def pullDataPart3(stock):
    try:
        path = 'C:\Users\B40904\Documents\Personal\PythonFinanceCharts\\'
        file_line = path+stock+'.txt'
        url_to_visit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        source_code = urllib2.urlopen(url_to_visit).read()
        split_source = source_code.split('\n')
        
        for line in split_source:
            split_line = line.split(',')
            if (len(split_line) == 6) and ('values' not in line):
                save_file = open(file_line, 'a')
                line_to_write = line+'\n'
                save_file.write(line_to_write)
                
        print 'Pulled ' + stock
        print 'sleeping'
        time.sleep(1)
            
    except Exception,e:
        print 'main loop', str(e)

def pullDataPart4(stock):
    
    print 'Currently pulling',stock
    print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    url_to_visit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1d/csv'
    path = 'C:\Users\B40904\Documents\Personal\PythonFinanceCharts\\'
    file_line = path+stock+'.txt'
    
    # Gets the last timestamp
    try:
        read_existing_data = open(file_line, 'r').read()
        split_existing = read_existing_data.split('\n')
        most_recent_line = split_existing[-2] # Last line is blank
        last_unix = most_recent_line.split(',')[0]
            
    except Exception,e:
        last_unix = 0
        
    save_file = open(file_line, 'a')
    source_code = urllib2.urlopen(url_to_visit).read()
    split_source = source_code.split('\n')
    
    for line in split_source:
        if 'values' not in line:
            split_line = line.split(',')
            if len(split_line) == 6:
                if int(split_line[0]) > int(last_unix):
                    line_to_write = line+'\n'
                    save_file.write(line_to_write)

    save_file.close()

    print 'Pulled ' + stock
    print 'sleeping'
    print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(10)
    
def part5():
    while True:
        for stock in stocks_to_pull:
            pullDataPart4(stock)
        
            time.sleep(10)

part5()
print 'Done!'