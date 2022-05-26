import json
import psycopg2

con = psycopg2.connect("dbname=test user=test host=localhost password=test")
cur = con.cursor()

insert_sql = """INSERT INTO tabletest VALUES(%s, %s)"""


record_list = '{"success":true,"timestamp":1619448844,"base":"EUR","date":"2021-04-26","rates":{"AED":4.438765,"AFN":93.597683,"ALL":123.266852,"AMD":628.973606,"ANG":2.169505,"AOA":793.273462,"ARS":112.71963,"AUD":1.547521,"AWG":2.173782,"AZN":2.056227,"BAM":1.954933,"BBD":2.440381,"BDT":102.484579,"BGN":1.956421,"BHD":0.455567,"BIF":2377.111091,"BMD":1.208496,"BND":1.602106,"BOB":8.333368,"BRL":6.583276,"BSD":1.208646,"BTC":2.2483098e-5,"BTN":90.32643,"BWP":13.045517}}'


record_dict = json.loads(record_list)

for record in record_dict["rates"].items():
    cur.execute(insert_sql, [record[0], record[1]])


con.commit()
