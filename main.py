import bottle
import classes
import json
import random

data=[{"url":"https://www.airbnb.com/rooms/16101052","loc":{'lat': 42.91942, 'lng': -78.8656},"city":"Buffalo","Country":"United States","State":"New York"},{"url":"https://www.airbnb.com/rooms/1633607","loc":{'lat': 42.9011, 'lng': -78.87445},"city":"Buffalo","Country":"United States","State":"New York"},{"url":"https://www.airbnb.com/rooms/19821724","loc":{'lat': 42.89871, 'lng': -78.87178},"city":"Buffalo","Country":"United States","State":"New York"},{"url":"https://www.airbnb.com/rooms/53146203","loc":{'lat': 42.90607, 'lng': -78.88533},"city":"Buffalo","Country":"United States","State":"New York"},{"url":"https://www.airbnb.com/rooms/27771774","loc":{'lat': 25.81884, 'lng': -80.18198},"city":"Miami","Country":"United States","State":"Flordia"},{"url":"https://www.airbnb.com/rooms/27227049","loc":{'lat': 25.84816, 'lng': -80.15216},"city":"Miami","Country":"United States","State":"Florida"},{"url":"https://www.airbnb.com/rooms/53659253","city":"Miami","Country":"United States","State":"Florida"},{"url":"https://www.airbnb.com/rooms/53659253","city":"Miami","Country":"United States","State":"Florida"},{"url":"https://www.airbnb.com/rooms/50065431","city":"Tusan","Country":"Italy","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/54010781","city""Paris":"Tusan","Country":"France","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/45572531","city":"Paris","Country":"France","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/50535107","city":"Paris","Country":"France","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/557860536348673100","city":"Paris","Country":"France","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/32868872","city":"San Diego","Country":"United States","State":"California"},{"url":"https://www.airbnb.com/rooms/47537417","city":"San Diego","Country":"United States","State":"California"},{"url":"https://www.airbnb.com/rooms/39692666","city":"San Diego","Country":"United States","State":"California"},{"url":"https://www.airbnb.com/rooms/47537417","city":"San Diego","Country":"United States","State":"California"},{"url":"https://www.airbnb.com/rooms/47537417","city":"San Diego","Country":"United States","State":"California"},{"url":"https://www.airbnb.com/rooms/33374106","city":"Austin","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/plus/11479813","city":"Austin","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/31746889","city":"Austin","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/43347086","city":"Austin","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/50599006","city":"Dallas","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/45424433","city":"Dallas","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/54320995","city":"Dallas","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/16603243","city":"Dallas","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/48864026","city":"Houston","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/52944826","city":"Houston","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/42840989","city":"Houston","Country":"United States","State":"Texas"},{"url":"https://www.airbnb.com/rooms/38535683","city":"London","Country":"United Kingdom","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/48118935","city":"London","Country":"United Kingdom","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/13896423","city":"London","Country":"United Kingdom","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/852169","city":"Berlin","Country":"Germany","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/15978345","city":"Berlin","Country":"Germany","State":"Not A State"},{"url":"https://www.airbnb.com/hotels/42583346","city":"Berlin","Country":"Germany","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/48119449","city":"Berlin","Country":"Germany","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/46004444","city":"Washington D.C","Country":"United States","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/50152089","city":"Washington D.C","Country":"United States","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/50154046","city":"Washington D.C","Country":"United States","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/49613123","city":"Washington D.C","Country":"United States","State":"Not A State"},{"url":"https://www.airbnb.com/rooms/49211457","city":"Seattle","Country":"United States","State":"Washington"},{"url":"https://www.airbnb.com/rooms/13224936","city":"Seattle","Country":"United States","State":"Washington"},{"url":"https://www.airbnb.com/rooms/12964731","city":"Gettysberg","Country":"United States","State":"Pennsylvania"},{"url":"https://www.airbnb.com/rooms/29099102","city":"Gettysberg","Country":"United States","State":"Pennsylvania"},{"url":"https://www.airbnb.com/rooms/29595917","city":"Gettysberg","Country":"United States","State":"Pennsylvania"},{"url":"https://www.airbnb.com/rooms/6493327","city":"Gettysberg","Country":"United States","State":"Pennsylvania"}]

setnum=0.5

datatemp=classes.getImages("https://www.airbnb.com/rooms/13124733?source_impression_id=p3_1648927787_Gbo%2BLlM18pvDx8bh")

def randiGen():
  num=random.randint(0,len(data)-1)
  return num

@bottle.route("/")
def index():
    return bottle.static_file("index.html",root=".")
  
@bottle.route("/styleSheet.css")
def styleSheet():
    return bottle.static_file("styleSheet.css", root='.')
  
@bottle.route("/processing.js")
def process():
    return bottle.static_file("processing.js", root='.')

def s(num):
  setnum=num
  
@bottle.route("/image")
def img():
    num=randiGen()
    while setnum == num:
      num=randiGen()
    images=classes.getImages(data[num].get("url"))
    out=[data[num],images]
    out1=json.dumps(out)
    s(num)
    return out1
  
  
bottle.run(host='0.0.0.0',port=8080)
