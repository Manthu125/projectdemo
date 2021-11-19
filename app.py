from flask import Flask, render_template, request
import datetime as dt
import re
from datetime import datetime
import sys

app = Flask(__name__) #creating the Flask class object   

@app.route('/')
def upload_file():
   return render_template("home.html")
   
@app.route('/uploader', methods = ['POST']) #decorator drfines the   
def home(): 
    if request.method == 'POST':
        f = request.files['file']
        name=f.filename
        f.save(f.filename)
        resultant_data = []
        txt_file_data = []
        line_rec = ''
        with open(name,'r') as filedata:
        txt_file_data.extend(filedata.readlines())
        for each_line_number, each_line_data in enumerate(txt_file_data):
            if each_line_data.strip('\n').count("Time Log"):
                line_rec = each_line_number
                break
            else:
                line_rec = 'NoTimeLog'
        if line_rec != "NoTimeLog":
            for index in range(int(line_rec), len(txt_file_data)):
                first_half_data = (txt_file_data[index].split(' - ')[0].split())
                second_half_data = (txt_file_data[index].split(' - ')[1:])
                counter = (txt_file_data[index].split(' - ')[1:])
                if len(first_half_data) != 0:
                    time_format_status = check_time_format(first_half_data[-1].strip())
                    if len(counter) != 0:
                        time_format_status_v1 = check_time_format(second_half_data[0].split()[0])
                        if time_format_status == "Yes" and time_format_status_v1 == "Yes":
                            resultant_data.append((first_half_data[-1], str(second_half_data[0].split()[0])))
                    
                
            calculate_time_spent(resultant_data)
        else:
            print("here you can not find the timelogfile : ", filename)
        filedata.close()
        def check_time_format(time_data):
        
        # here i use try function to strptime
        try:
            time.strptime(time_data, '%I:%M%p')
            return "Yes"
        except ValueError:
            return "No"
        
        def calculate_time_spent(time_data):
        time_taken_by_author = datetime.timedelta()
        for data in time_data:
            time_data_v1 = datetime.datetime.strptime(data[1], "%I:%M%p")
            time_data_v2 = datetime.datetime.strptime(data[0], "%I:%M%p")
            difference_in_time = (time_data_v1 - time_data_v2)

            if str(difference_in_time).count('day') != 0:
                zero = "00:00:00"
                day_data = (str(difference_in_time).split(",")[1].strip())
                time_data_v4 = datetime.datetime.strptime(zero, "%H:%M:%S")
                time_data_v3 = datetime.datetime.strptime(day_data, "%H:%M:%S")
                difference_in_time_v1 = (time_data_v3 - time_data_v4)
                time_taken_by_author += difference_in_time_v1
            else:
                time_taken_by_author += difference_in_time
        main_split = str(time_taken_by_author).split()
        main_day =int(main_split[0]) * 24
        main_hours_split = main_split[2].split(':')
        main_hours = int(main_hours_split[0])
        #print("total time =",main_day + main_hours ,"hours", main_hours_split[1],"minutes" )
        return render_template("home.html",data="Total : "+str(sumh) + " h"+ str(summi) + " m")    
        #        return render_template("home.html",data="Total : "+str(sumh) + " h"+ str(summi) + " m")
        #except:
        #    return render_template("home.html",data="Excepion")

		
if __name__ == '__main__':
   app.run(debug = True)