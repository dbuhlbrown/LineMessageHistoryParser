import re
from collections import Counter
import string
regex = re.compile('(\d\d\d\d{1}|\/\d\d{1}|\/\d\d{1}|\([A-Z]+[a-z]{2}\))+')

class Message:

	def __init__(self, time, person_messaging, message, date, day_of_the_week):
		self.time = time #24-hour time
		self.person_messaging = person_messaging
		self.message = message
		self.date = date
		self.day_of_the_week = day_of_the_week


	def calculate_length(self):

		self.length = len(self.message)

	#I am using some weird tricks to determine which language a message is using.
	def set_language_used(self):

		counter = Counter(self.message)
		total_english_characters = 0
		
		for letter in list(string.ascii_lowercase) + list(string.ascii_uppercase):
			total_english_characters += counter[letter]

		if total_english_characters / self.length >= 0.5:
			#English
			self.language_used = "Eng"
		
		else:
			#Chinese
			self.language_used = "Chi"


	def return_csv(self):
		
		self.calculate_length( )
		self.set_language_used( )

		return self.time+","+self.person_messaging+","+self.message.replace("\r","").replace(",","")+","+self.date+","+self.day_of_the_week.replace("\r","")+","+str(self.length)+","+self.language_used

def write_out_csv(messages, file_name):

	#This writes out a file called your_file_name_csv.txt (why .txt? Because it doesn't matter)
	#Todo: maybe make this nicer.
	file_out = open(file_name.replace(".txt","")+"_csv.txt","wb")

	#This is probably wildly inefficient.
	for message in messages:
		file_out.write((message.return_csv()+"\n").encode("utf-8"))


file_name = input("Enter your filename (can include directory): ")
	
#May not need the Try Except
with open(file_name,'rb') as f:
		
	contents = f.read()
	text = ""
	try:
		text = contents.decode("utf-8")
	except UnicodeDecodeError:

		try:
			text = contents.decode("big5")

		except UnicodeDecodeError:
			print("UnicodeError with = " + file)

#regex command to test if this is the beginning of a new day: (\d\d\d\d{1}|\/\d\d{1}|\/\d\d{1}|\([A-Z]+[a-z]{2}\))+
#looks for this format yyyy/mm/dd/(DAY_OF_THE_WEEK_3_CHAR)
data_array = text.split("\n")

message_list = []
most_recent_date = "2018/05/27"
most_recent_day_of_the_week = "Sun"

for i in range(0, len(data_array)):

	tmp_data_line = data_array[i]

	#There are some messages that are tricky to read, so I decided to ignore them,
	#mostly because out of like 13K messages, I found only around 100 were bad (real rough numbers)
	if regex.match(tmp_data_line) and tmp_data_line.find("/")!=-1:

		#Some files have different formatting (Android uses ( ) for the day of the week)
		if tmp_data_line.find("(") != -1:
		#this is the beginning of a new day of messages
			split_line = tmp_data_line.split("(")
			most_recent_date = split_line[0]
			most_recent_day_of_the_week = split_line[1][0:len(split_line[1])-2] #we need to cut off the last parenthesis
		
		else:
			split_line = tmp_data_line.split(",")
			most_recent_date = split_line[0]
			most_recent_day_of_the_week = split_line[1][1:len(split_line[1])] #we need to skip the 0th index because of a space
		
	else:

		split_line = tmp_data_line.split("	") #split by any whitespace
		
		if(len(split_line) >= 3 ):
			#print(split_line)
			message_list.append( Message(split_line[0], split_line[1], split_line[2],most_recent_date, most_recent_day_of_the_week) )
	#input( )
write_out_csv(message_list,file_name)

