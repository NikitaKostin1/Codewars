

'''
Link to rhis 4 kyu kata from Codewars: 
-------------------------------------------------------
https://www.codewars.com/kata/52742f58faf5485cae000b9a
-------------------------------------------------------

To-do-list: 
-------------------------------------------------------
To change "double list" to dictionary
-------------------------------------------------------
'''


def format_duration(s):
    if not s:
        print('Now')
    a, list, x, y, d, h, m = -1, [], -1, 0, 0, 0, 0
    string, year, day, hour, minute = ' ', '','', '', ''
    if s / 31536000 > 0:
        y = s // 31536000
        s -= y * 31536000
        if y > 1:
            year = 'years'
        else:
            year = 'year'
    if s / 86400 > 0:
        d = s // 86400
        s -= d * 86400
        if d > 1:
            day = 'days'
        else:
            day = 'day'
    if s / 3600 > 0:
        h = s // 3600
        s -= h * 3600 
        if h > 1:
            hour = 'hours'
        else:
            hour = 'hour'
    if s / 60 > 0:
        m = s // 60
        s -= m * 60
        if m > 1:
            minute = 'minutes'
        else:
            minute = 'minute'
    if s > 1:
        second = 'seconds'
    else:
        second = 'second'
    
    list_1 = [[y, d, h, m, s], [year, day, hour, minute, second]]
    while 0 in list_1[0]:  
        for var in list_1[0]:
            x += 1
            if var < 1:
                del list_1[0][x]
                del list_1[1][x]
                x = -1
                break
    x = -1
    for i in list_1[0]:
        x += 1
        if x < len(list_1[0]) - 2:
            list.append(str(list_1[0][x]))
            list.append(list_1[1][x] + ',')
        else:
            try:
                list.append(str(list_1[0][-2]))
                list.append(list_1[1][-2])
                list.append('and ' + str(list_1[0][-1]))
                list.append(list_1[1][-1])
            except:
                list.append(str(list_1[0][-1]))
                list.append(list_1[1][-1])
            break
    string = string.join(list)
    print(string)



format_duration(int(input('Input there any time in seconds from 0 (Example: 7289424) - ')))