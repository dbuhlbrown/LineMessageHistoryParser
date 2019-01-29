file_name = input("Enter your filename (can include directory): ")

common_english_words = ["lol","me","you","her","he","time","now","will","the","a","an","it","they","them","us",
					   	"i","like","there","when","where","yeah","hey","hi",
					   	"can","just","fine","one","see","two","sure","got","hour","minute","time","day"]
	
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

text = text.lower()

for word in common_english_words:
	text = text.replace(" " + word + " "," ")

text = text.replace("hey ","")
text = text.replace("hi ","")
text = text.replace("fine ","")
text = text.replace("he ","")
text = text.replace("i ","")
text = text.replace("yeah ","")

file_out = open(file_name.replace(".txt","")+"_cleaned.txt","wb")

file_out.write((text).encode("utf-8"))