import datetime
import sys
import time

from flask import Flask, render_template, request




 #creating the Flask class object   

@app.route('/')
def upload_file():
   return render_template("home.html")



def check_format(time_data):
    try:
        time.strptime(time_data, '%I:%M%p')
        return "Yes"
    except ValueError:
        return "No"

# def main(filename):
app = Flask(__name__)
@app.route('/uploader', methods = ['POST']) #decorator drfines the   

def calculate_time_spent(time_data):
    '''
    :param time_data:
    :return:
    '''
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
    #here i split the days into hourse and minute

    main_split = str(time_taken_by_author).split()
    main_day =int(main_split[0]) * 24
    main_hours_split = main_split[2].split(':')
    main_hours = int(main_hours_split[0])
    print("total time =",main_day + main_hours ,"hours", main_hours_split[1],"minutes" )


def main(filename):
    '''
    :param filename:
    :return:
    '''
    resultant_data = []
    txt_file_data = []
    line_rec = ''
    filedata = open(filename, "r")
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
                
        # print('ok')
        print("Time Log should noty be in %s while parsing." % (filename))
        print("File Name:-",filename,aa + bb ,"hours", b[1],"minutes", b[2],"seconds")
    else:
        print("No TimeLog file : ", filename)
    filedata.close()

if __name__ == '__main__':
    filename = (str(sys.argv[1]))
    app.run(debug = True)
# if __name__ == '__main__':
#     filename = (str(sys.argv[1]))
#     main(filename)