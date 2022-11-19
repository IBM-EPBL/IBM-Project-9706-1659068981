

import pandas as pd
import random
import requests, json
import time
from twilio.rest import Client
import gspread
from datetime import datetime



sa= gspread.service_account(filename=r"C:\Users\K B PAVITHRAN\ibm-crop-protection-9837998227d9.json")
sh = sa.open("IBM_db")
whs =sh.worksheet("Animal Instrusion notification history")



def update_sheet(loc_list,message,time_stamp,soil_humidity,current_humidity,current_pressure,current_temperature):
#     update_sheet(loc_list,temporary_text , str(time_stamp),str(soil_humidity[i]) ,str(current_humidity ),str(current_pressure),str(current_temperature))
    index = 'A'
    time_stamp_index = 'B'
    current_temperature_index = 'C'
    current_pressure_index = 'D'
    current_humidity_index= 'E'
    soil_humidity_index = 'F'
    message_index = 'G'
    location_1_index='H'
    location_2_index='I'
    location_3_index='J'
    location_4_index='K'
    TEMP_LEN = len(whs.get_all_values())
    if TEMP_LEN ==0:
        TEMP_LEN =1
    print(whs.get_all_values())
    print(whs.row_count)
    print("total_length",TEMP_LEN)

    index += str(TEMP_LEN +1)              
    current_temperature_index +=str((TEMP_LEN) +1)
    current_pressure_index +=str((TEMP_LEN) +1)

   
    current_humidity_index +=str((TEMP_LEN) +1)
    soil_humidity_index +=str((TEMP_LEN) +1)
    message_index +=str((TEMP_LEN) +1)
    time_stamp_index +=str((TEMP_LEN) +1)
    
    location_1_index +=str((TEMP_LEN) +1)
    location_2_index +=str((TEMP_LEN) +1)
    location_3_index +=str((TEMP_LEN) +1)
    location_4_index +=str((TEMP_LEN) +1)

    whs.update(index,TEMP_LEN)
    whs.update(message_index,message  )
    whs.update(time_stamp_index,time_stamp)
    whs.update(current_temperature_index,current_temperature)
    whs.update(current_pressure_index,current_pressure)
    whs.update(soil_humidity_index,soil_humidity)
    whs.update(current_humidity_index,current_humidity)
    whs.update(location_1_index,loc_list[0])
    whs.update(location_2_index,loc_list[1])
    whs.update(location_3_index,loc_list[2])
    whs.update(location_4_index,loc_list[3])
def get_values():
    data=whs.get_all_values()
    for i in data:
        print(i )




df = pd.DataFrame()
username = "Pavithran 1904032 "




rand_prox_location_1=[]
constrain_location_1=9.7
rand_prox_location_2=[]
constrain_location_2=7
rand_prox_location_3=[]
constrain_location_3=9.5
rand_prox_location_4=[]
constrain_location_4=9.9
soil_humidity=[]
constrain_soil_humidity= 75
constrain_temp= 295
constrain_humidity= 80
constrain_pressure= 1030
constrain_soil_humidity_low =40
for i in range(1,100):
    rand_prox_location_1.append(round(random.uniform(0.25,10),2))
    rand_prox_location_2.append(round(random.uniform(0.25,10),2))
    rand_prox_location_3.append(round(random.uniform(0.25,10),2))
    rand_prox_location_4.append(round(random.uniform(0.25,10),2))
    soil_humidity.append(round(random.uniform(1,100),1))
print("--------",rand_prox_location_4)
print("--------",rand_prox_location_3)
print("--------",rand_prox_location_2)
print("--------",rand_prox_location_1)
print("--------",soil_humidity)



df['Location_1']=rand_prox_location_1
df['Location_2']=rand_prox_location_2
df['Location_3']=rand_prox_location_3
df['Location_4']=rand_prox_location_4
df['soil_humidity']=soil_humidity
df.to_excel('IBM_sensor_data.xlsx', index = False)



def send_sms(username,text):
    SID= 'AC34c7f1445fd65764ad5af8cfb249afc5'
    auth_token='9fc5715505bd02ac73be8429b116d7a8'

    cl = Client(SID, auth_token)
    cl.messages.create(body="Hey,"+username+text,from_='+13609975006',to='+919894567077' )



def get_whether():
    api_key = "b48129c70234f815d857006719283786"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Coimbatore"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
#     print(x)
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
#         print(" Temperature (in kelvin unit) = " + str(current_temperature))
#         print(" Atmospheric pressure (in hPa unit) = " +str(current_pressure)) 
#         print(" Humidity (in percentage) = " + str(current_humidity))
#         print(" Description = " + str(weather_description))
        return(current_temperature,current_pressure,current_humidity,weather_description)
    else:
        print(" City Not Found ")
        return(None)
    




for i in range(1):
    time_stamp = datetime.now()
    time.sleep(5)
    temp=[0,0,0,0]
    value=[0,0,0,0]
    animal_intrusion_set=0
    temp_set=0
    soil_humidity_set=0
    pressure_set=0
    atmos_humidity_set=0
    animal_intrusion_text = ' Animal intrusion at'
    temporary_text= ''
    try:
        current_temperature,current_pressure,current_humidity,weather_description = get_whether()
    except:
        print("enter appropriate location")
    
    if current_temperature > constrain_temp:
        temp_set=1
        temporary_text += ' Temperature is high :'+str(current_temperature) + ' || '
    if current_pressure > constrain_pressure:
        pressure_set=1
        temporary_text += ' Pressure is high :'+str(current_pressure) + ' || '
    if current_humidity > constrain_humidity:
        atmos_humidity_set=1
        temporary_text += ' Atmosphereic humidity is high :'+str(current_humidity ) + ' || '
    if soil_humidity[i] > constrain_soil_humidity:
        soil_humidity_set=1
        temporary_text += ' Soil humidity is high :'+str(soil_humidity[i]) + ' || '
    if soil_humidity[i] < constrain_soil_humidity_low:
        soil_humidity_set=1
        temporary_text += ' Soil humidity is low :'+str(soil_humidity[i]) + ' || '
        # send_sms("activate the pump",username)
        print("The soil humidity is low turning on the pump")
    if rand_prox_location_1[i] > constrain_location_1:
        temp[0]=1
        value[0]=rand_prox_location_1[i]
    if rand_prox_location_2[i] > constrain_location_2:
        temp[1]=1
        value[1]=rand_prox_location_2[i]
    if rand_prox_location_3[i] > constrain_location_3:
        temp[2]=1
        value[2]=rand_prox_location_3[i]
    if rand_prox_location_4[i] > constrain_location_4:
        temp[3]=1
        value[3]=rand_prox_location_4[i]
    for j in range(len(temp)):
        if temp[j]==1:
            animal_intrusion_set=1
            animal_intrusion_text += ' location '+str(j)+ ' with a distance from sensor of ' + str(value[j]) + ' || '
    trigger=0
    loc_list = [rand_prox_location_1[i],rand_prox_location_2[i],rand_prox_location_3[i],rand_prox_location_4[i]]

    if animal_intrusion_set==1:  
        temporary_text+=animal_intrusion_text
        trigger = 1
    else:
        if temporary_text != '':
            trigger = 1
    update_sheet(loc_list,temporary_text , str(time_stamp),str(soil_humidity[i]) ,str(current_humidity ),str(current_pressure),str(current_temperature))
    if trigger ==1:
        print(temporary_text,username)
        print("-------------------------------------------------------------------")
        print("updating db")
        print("-------------------------------------------------------------------")
        print("sending sms")
        print("-------------------------------------------------------------------")
        time.sleep(30)
        try:
            # send_sms(temporary_text,username)
            print("sms sent")
            print("-------------------------------------------------------------------")
        except:
            print("failed to send sms")
        get_values()
