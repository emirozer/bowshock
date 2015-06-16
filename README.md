![Screenshot](https://raw.githubusercontent.com/emirozer/bowshock/master/docs/bowshock2.png)
===========
[![PyPI version](https://badge.fury.io/py/bowshock.svg)](http://badge.fury.io/py/bowshock)
[![Downloads](https://pypip.in/download/bowshock/badge.svg)](https://pypi.python.org/pypi/bowshock/)
[![Latest Version](https://pypip.in/version/bowshock/badge.svg)](https://pypi.python.org/pypi/bowshock/)
[![Build Status](https://travis-ci.org/emirozer/bowshock.svg)](https://travis-ci.org/emirozer/bowshock)

===========

##About

bowshock is an all-in-one wrapper for NASA API's.
Here is a list of currently supported API's :

* NASA [Earth API](https://data.nasa.gov/developer/external/planetary/#imagery)
* NASA [APOD API](https://data.nasa.gov/developer/external/planetary/#address)
* NASA [Patents API](https://data.nasa.gov/developer/external/planetary/#sounds)
* NASA [Earth Temperature Anomalies API](https://data.nasa.gov/developer/external/planetary/#coordinates)
* [Asterank API](http://www.asterank.com/api)
* [HelioViewer API](http://helioviewer.org/api/docs/v1/)
* [Mars Weather API](http://marsweather.ingenology.com/#get_started)
* [MODIS API](http://daac.ornl.gov/MODIS/MODIS-menu/modis_webservice.html)
* [Skymorph API](http://www.asterank.com/skymorph)
* [Star API](http://hacktheuniverse.github.io/star-api/)
* [Techport API](https://data.nasa.gov/developer/external/techport/techport-api.pdf)
* [PredictTheSky API](http://predictthesky.org/developers.html)

##Install

Standart Procedure

	pip install bowshock

*Important Note*: The only requirement is the 'requests' package BUT if you want to use MODIS there is an external requirement which is 'suds' package

## Do i need an API Key ?

YES    | NO
------   |----
Earth  |The rest
APOD |
Patents |
Earth Temperature Anomalies|

**The rest does not require an API key for usage.**
Get your NASA API KEY from : https://data.nasa.gov/developer/external/planetary/#apply-for-an-api-key

####Setting up the API Key
===================
set an environment varible NASA_API_KEY which is equal to your key string


##Usage

-
#####Apod
```python
from bowshock import apod

# with specific date and tags - For apod all args are optional
apod.apod(date="2015-02-02", concept_tags=True)

```

-
#####Asterank
```python
from bowshock import asterank

# all args mandatory
asterank.asterank(
            	query={"e": {"$lt": 0.1},
               	       "i": {"$lt": 4},
                       "a": {"$lt": 1.5}},
                  limit=1)

```


-
#####Earth
```python
from bowshock import earth

# imagery endpoint lon & lat mandatory, rest optional
earth.imagery(lon=100.75,
                    lat=1.6,
                    dim=0.0025,
                    date="2015-02-02",
                    cloud_score=True)
# assets endpoint lon & lat & begin mandatory, end optional
earth.assets(lon=100.75, lat=1.6, begin="2015-02-02", end="2015-02-10")
```

-
#####HelioViewer
```python
from bowshock import helioviewer

# args are mandatory
helioviewer.getjp2image(date='2014-01-01T23:59:59', sourceId=14)
#args are mandatory
helioviewer.getjp2header(Id=7654321)

```


-
#####MAAS
```python
from bowshock import maas

# mandatory date begin / end
maas.maas_archive('2012-10-01', '2012-10-31')

maas.maas_latest()

```

-
#####Patents
```python
from bowshock import patents

# only query is mandatory, rest is optional
patents.patents(query="temperature", concept_tags=True, limit=5)

```


-
#####PredictTheSky
```python
from bowshock import predictthesky

#args are mandatory
predictthesky.space_events(lon=100.75, lat=1.5)

```


-
#####Star API
```python
from bowshock import star

star.stars()
star.search_star("Sun")

star.exoplanets()
star.search_exoplanet("11 Com")

star.local_group_of_galaxies()
star.search_local_galaxies("IC 10")

star.star_clusters()
star.search_star_cluster("Berkeley 59")

```


-
##### Skymorph
```python
from bowshock import skymorph

# mandatory obj id
skymorph.search_target_obj("J99TS7A")

#TODO : add search_position() , search_target_obj()

```


-
#####temperature anomalies
```python
from bowshock import temperature_anomalies

# end arg is optional, rest is mandatory
temperature_anomalies.coordinate(lon=100.3, lat=1.6, begin="1990", end="2005")


```


-
#####techport
```python
from bowshock import techport

techport.techport(Id="4795")

```
##TODO
- Lance-Modis API - http://lance-modis.eosdis.nasa.gov/user_services/api-lance.html

##BTW What is "bowshock"?
![Screenshot](https://raw.githubusercontent.com/emirozer/bowshock/master/docs/bowshock.jpg)
