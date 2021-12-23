# Measurecon GUI Version

Python module to convert measurements from one unit (e.g. cup) to another (e.g. liter) and to compute energy equivalent for units in Joules.
This module illustrates how to do the following:
- Use a design created in an Excel file + PyOOder to create the shell of Measurecon.py
- Load a dictionary from a JSON file.
- Convert between units of measure using the dictionary and the technique of having a common measure (cubic centimeters) to avoid the O(n^2) possible combinations.
- Using TKinter as a means of creating a GUI for the module.
- Importing a class from a different module.
- Convert unit of measure to Joules.
- Under development: Convert Joules to ft-lbs

Overview of logic:

Two modules are used to develop this application: Measurecon.py and Measurecon GUI Version.
Measurecon GUI Version imports Measurecon and interacts with LM class methods.

Flow of Control:

Measurecon GUI Version creates the graphics user interface for the application.
The GUI interface consists of two windows, one to collect client inputs regarding the unit to convert from (from_unit) and the unit to convert to (to_unit, as well the quantity of from_units to convert.  
The second (sub-) window is used to display the output, consisting of the from_unit, to_unit, quantity and the equivalent Joules for the to_unit.

The Click-when-ready button triggers the myClick() method, which in turn, calls the dispatcher() class method of LM.
Dispatcher() orchestrates the method calling within the LM class to cause the conversion from from_unit to to_unit.
The method of conversion is to translate both the from_unit and to_unit to their equivalent in cubic centimeters and then divide one by the other to obtain the to_unit value.
The cc-equivalents are obtained from the LM Dictionary (lmdict), which is loaded by the load_dictionary() method from the lmdict.json file.

The entire process is intitiated by calling the Measurecon GUI Version.py module from the command line with an optional --path argument that gives the file path to lmdict.json.
If no --path argument is provided, it is assumed that lmdict.json is located in the current directory.
