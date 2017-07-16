# The modularised bits...

Separate functions to pull in data from each of the sensors. Each is named after the model number of hte device it's pulling in. Each returns a key/value array of the form: [name][value][type] where:

* name: the title - UID for thsi measurement
* value: the reading
* type: what we are measuring 
