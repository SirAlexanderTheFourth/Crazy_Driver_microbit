from microbit import *
while True:
    a = accelerometer.get_values()
    if(accelerometer.get_x()>150 and accelerometer.get_y()>150):
        display.show(Image('00000:'
                           '00000:'
                           '00903:'
                           '00066:'
                           '00366'))
    elif(accelerometer.get_x()>150 and accelerometer.get_y()<-150):
        display.show(Image('00366:'
                           '00066:'
                           '00903:'
                           '00000:'
                           '00000'))
    elif(accelerometer.get_x()<-150 and accelerometer.get_y()>150):
        display.show(Image('00000:'
                           '00000:'
                           '30900:'
                           '66000:'
                           '66300'))
    elif(accelerometer.get_x()<-150 and accelerometer.get_y()<-150):
        display.show(Image('66300:'
                           '66000:'
                           '30900:'
                           '00000:'
                           '00000'))
    elif(accelerometer.get_x()>150):
        display.show(Image('00000:'
                           '00060:'
                           '00966:'
                           '00060:'
                           '00000'))
    elif(accelerometer.get_x()<-150):
        display.show(Image('00000:'
                           '06000:'
                           '66900:'
                           '06000:'
                           '00000'))
    elif(accelerometer.get_y()<-150):
        display.show(Image('00600:'
                           '06660:'
                           '00900:'
                           '00000:'
                           '00000'))  
    elif(accelerometer.get_y()>150):
        display.show(Image('00000:'
                           '00000:'
                           '00900:'
                           '06660:'
                           '00600'))
    else:
        display.show(Image('00300:'
                           '03630:'
                           '36963:'
                           '03630:'
                           '00300'))
        
    print(a)
    sleep(100)