from time import localtime
wk_days = {0 : 'Mon',
           1 : 'Tues',
           2 : 'Wed',
           3 : 'Thurs',
           4 : 'Fri',
           5 : 'Sat',
           6 : 'Sun'
        }


def get_current_time():
    current_time = list(localtime())[:7]
    current_time.pop(5)
    return f'{wk_days.get(current_time[-1])},{current_time[3]:02}:{current_time[4]:02},{current_time[2]}/{current_time[1]}/{current_time[0]}'
    #print(current_time)
#print(get_current_time())

def add_record(time_stamp):
    new_entry = open(r'\Users\Stella Idiakhoa\Documents\VS CODE\personal_code\mini_project_1\record_data.csv','a', encoding="utf-8")
    new_entry.write('\n')
    new_entry.write(time_stamp)
    new_entry.close

def see_record(stat=False):
    
    archive = open(r'\Users\Stella Idiakhoa\Documents\VS CODE\personal_code\mini_project_1\record_data.csv','r', encoding="utf-8")
    round_hist = []
    for line in archive:
        if 'month' in line:
            continue
        line = line.split(',')#list slicing
        if stat:
            round_hist.append(line[3])
            
        else:
            print(f'{','.join(line[:3]):{25}}\t{line[3]:{2}}\t\t\t{line[4]:{13}}'.strip())
            
    else:
        bar_graph = {'Round 1' : round_hist.count('1'),
                    'Round 2' : round_hist.count('2'),
                    'Round 3' : round_hist.count('3'),
                    'Round 4' : round_hist.count('4'),
                    'Round 5' : round_hist.count('5'),
                    'Round 6' : round_hist.count('6'),
                    'Round 7' : round_hist.count('7'),
                    'Round 8' : round_hist.count('8'),
                    'Round 9' : round_hist.count('9'),
                    'Round 10' : round_hist.count('10'),
                    'Round 11' : round_hist.count('11'),
                    'Round 12' : round_hist.count('12')
                    }
        return bar_graph
        #print(type(line))
archive = open(r'\Users\Stella Idiakhoa\Documents\VS CODE\personal_code\mini_project_1\record_data.csv','r', encoding="utf-8")

