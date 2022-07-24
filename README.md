
Face Detect API
=====================

Detect faces from an image in base64. 
Receives one image in base64 and check if has faces or not.


System requirements
-------------------

- Python >= 3.6


Installation
------------

```bash
$ sudo mkdir /var/log/fksolutions  # creates fksolutionslogging folder
$ sudo chown $USER:$USER /var/log/fksolutions  # give fksolutionslogging folder group permissions
$ pip install -e .
```


Usage
-----

```bash
$ face-detect  # run API
```

Read REST API documentation through ``/docs`` endpoint for API usage.