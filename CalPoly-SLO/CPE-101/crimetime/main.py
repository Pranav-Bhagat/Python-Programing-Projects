class Robbery:

    def __init__(self, crime_id, time=None):
        self.crime_id = crime_id
        self.time = time

    def __eq__(self, other):
        return self.crime_id == other.crime_id

    def __repr__(self):
        clean_time = ""
        if self.time == None:
            clean_time = "None"
        else:
            split = self.time.split(':')
            if(int(split[0]) < 12):
                if(split[0] == '00' or split[0] == '0'):
                    split[0] = '12'
                clean_time =  str(int(split[0])) + ':' + split[1].strip() + 'AM'
            else:
                split[0] = str(int(split[0]) - 12)
                if(split[0] == '00' or split[0] == '0'):
                    split[0] = '12'
                clean_time =  str(int(split[0])) + ':' + split[1].strip() + 'PM'
        return str(self.crime_id) + '\t' + clean_time + '\n'

    def __lt__(self, other):
        my_time = self.time
        other_time = other.time
        if(my_time == None or other_time == None):
            return False
        my_hours, my_mins = tuple(my_time.split(':'))
        other_hours, other_mins = tuple(other_time.split(':'))

        if(my_hours != other_hours):
            return int(my_hours) < int(other_hours)
        else:
            return int(my_mins) < int(other_mins)

    def copy(self):
        return Robbery(self.crime_id, self.time)


def main():
    robberies = []
    seen = []
    crimes =  open('crimes.tsv', 'r', encoding = "utf-8")
    line = crimes.readline()
    line = crimes.readline()
    while line:
        line_data = line.split('\t')
        if line_data[1] == 'ROBBERY' and line_data[0] not in seen:
            robberies.append(Robbery(int(line_data[0])))
            seen.append(line_data[0])
        line = crimes.readline()
    crimes.close()
    robberies = sort_crimes(robberies, 'id')


    times = open('times.tsv', 'r', encoding = "utf-8")
    line = times.readline()
    line = times.readline()
    while line:
        line_data = line.split('\t')
        crime_id = line_data[0]
        t = line_data[1]
        crime_index = find_crime(robberies, int(crime_id))
        if(crime_index != -1):
            robberies[crime_index].time = t
        line = times.readline()
    times.close()


    sort = sort_crimes(robberies, 'time')
    out =  open('robberies.tsv', 'w+', encoding = "utf-8")
    out.write('ID\tTime\n')
    for crime in sort:
        out.write(str(crime))
    out.close()

def sort_crimes(crimes, by):
    crimes_cpy = []
    sorted_crimes = []
    for c in crimes:
        crimes_cpy.append(c.copy())
    if by == 'id':
        return sort_crimes_id(crimes_cpy)
    elif by == 'time':
        return sort_crimes_time(crimes_cpy)
    else:
        return None

def sort_crimes_id(crimes):
    sorted_crimes = []
    while(len(crimes) > 0):
        s_id = 0
        for i in range(0, len(crimes)):
            if crimes[i].crime_id < crimes[s_id].crime_id:
                s_id = i
        sorted_crimes.append(crimes.pop(s_id))
    return sorted_crimes

def sort_crimes_time(crimes):

    sorted_crimes = []
    while(len(crimes) > 0):
        min_time_crime = crimes[0]
        for crime in crimes:
            if crime < min_time_crime:
                min_time_crime = crime

        first_time = min_time_crime.time
        same_time_crimes = []
        for crime in crimes:
            if crime.time == first_time:
                same_time_crimes.append(crime)

        same_time_crimes = sort_crimes_id(same_time_crimes)
        for crime in same_time_crimes:
            sorted_crimes.append(crime)
        for crime in same_time_crimes:
            crimes.remove(crime)
    return sorted_crimes;



def find_crime(crimes, crime_id):
    left = 0
    right = len(crimes)
    while True:
        if left == right-1:
            if(crimes[left].crime_id == crime_id):
                return left
            else:
                return -1
        mid = int((left + right) / 2)
        if crimes[mid].crime_id == crime_id:
            return mid
        elif crimes[mid].crime_id > crime_id:
            right = mid
        else:
            left = mid

    return -1

    

main()
