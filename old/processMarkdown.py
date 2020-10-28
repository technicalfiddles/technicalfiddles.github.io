import glob
import markdown
import subprocess
import os

def convertMarkdown():


	files = glob.glob("*.md")
	# outFiles = files.replace(".md",".html")
	for i in files:
     # access data using column names
  #    	input_file = codecs.open(i, mode="r", encoding="utf-8")
		# text = input_file.read()
		out = i.replace(".md",".html")
		out = ''.join(out)
		in1 = ''.join(i)
		# print in1
		# print out
		# print markdown.markdownFromFile("first.md","first.html")
		cmd = 'python -m markdown ' + in1 + " > " + out;
		print cmd
		os.system(cmd)

convertMarkdown()