## Activity 3: Spot the Error!

Answer: Snippet B is the legal code that will run and print `"Success!"`.

* Snippet A gives a `TypeError` because `TempSensor` forgot to include the required `get_data` method.
* Snippet B works properly because `PHMeter` implements its own `get_data` method before creating the object.
* Snippet C gives a `TypeError` because it tries to create an object straight from the abstract `Sensor` class.