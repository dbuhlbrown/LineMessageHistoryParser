# LineMessageHistoryParser
A simple Python script that parses LINE message history files (.txt)

I wanted to do some data visualization coding with my LINE chat history so I made a pretty basic Python script to parse everything.

Using it is quite simple, just run the Program and enter the filepath for your LINE history file. Mine was just .txt file.

It will run automatically then write out a csv file (in the same directory that your text file is in) with the following format:

Time (HH:MM)(24-hour clock), Name of sender, message, date, day of the week, message character counter, language used (only supports English/Chinese) written as Eng/Chi.

Future Work and Extra Features:

1. I would like to add some testing code just for further development purposes.

2. Add the ability to run it directly from the CMD line.

3. Expand this to parse other types of personal messaging files (I.E FB, WeChat...)

4. Add the visualization code (currently I am doing the visualization separately in Excel.
