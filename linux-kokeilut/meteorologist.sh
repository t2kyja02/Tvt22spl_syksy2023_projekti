#!/bin/bash
fmidata=$(curl --connect-timeout 10 -s 'https://opendata.fmi.fi/wfs?request=getFeature&storedquery_id=fmi::observations::weather::timevaluepair&place=oulu&timestep=10&parameters=temperature' | grep -oP '(?<=wml2:value>)[^<]+' | tail -2 | head -1)
echo $fmidata
MYDATA="1000, 1, "$fmidata", 'Oulu vihreäsaari'"
echo "INSERT INTO rawdata (watts, sensor, temperature, location) VALUES ($MYDATA);" | mysql -u dbaccess_rw -p"fasdjkf2389vw2c3k234vk2f3" measurements
