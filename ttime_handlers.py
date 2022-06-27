def seconds(num):
    days = num // 86400
    d = 'days'
    ost1 = num - 86400 * days
    hours = ost1 // 3600
    h = 'hours'
    ost2 = num - (86400 * days + hours * 3600)
    mins = ost2 // 60
    m = 'minutes'
    sec = num - (mins * 60 + 86400 * days + 3600 * hours)
    s = 'seconds'
    dict_time = {
        'days': num // 86400,
        'hours': hours,
        'minutes': mins,
        'seconds': sec
    }
    return dict_time