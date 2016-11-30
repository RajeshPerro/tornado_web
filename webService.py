import tornado.ioloop
import tornado.web
import os.path

class MainHandler(tornado.web.RequestHandler):
	def get(self):
        	self.write("GET is working..")

	def put(self, *args, **kwargs):
		self.write(self.request.body)
		self.write("\nPUT is working..")
		my_file = os.path.exists("write_file.txt")
		if my_file:
			print "<<<<<<-----File already exists------>>>>>>"
			text_file = open("write_file.txt", "a")
			text_file.write(self.request.body)
			text_file.write("\n")
			text_file.close()
		else:	
			print "<<<<----Creating new file to write---->>>>"
			text_file = open("write_file.txt", "w")
			text_file.write(self.request.body)
			text_file.write("\n")
			text_file.close()
	


					
	            
class FileHandler(tornado.web.RequestHandler):
	def get(self):
		#just have to change the file name..
		my_file_read =  os.path.exists("write_file.txt")

		if my_file_read:
			print "<<<<<<-----File Found------>>>>>>"
			text_file = open("write_file.txt","r")
			lines = text_file.readlines()
			x= len(lines)
			print "The number of line is : ",x
			#print len(lines)
			for line in lines:
				self.write(line)
			text_file.close()
		else:
			print "<<<<<<-----File not Found------>>>>>>"
			def prepare(self):
				raise tornado.web.HTTPError(404)
        		self.set_status(404)
        		self.write("404 FILE NOT FOUND")
        		self.write("<br>")
        		self.write("There are no files send a PUT request for creating a new file")
   	
   	def post(self, *args, **kwargs):
   		#just have to change the file name..
   		my_file_read =  os.path.exists("write_file.txt")
   		if my_file_read:
			self.write("POST is working..")
			print "<<<<<-----File exists----->>>>>"
			text_file = open("write_file.txt", "w")
			text_file.write(self.request.body)
			text_file.write("\n")
			text_file.close()
			print "<<<<----Old data replaced in File---->>>>"
		else:
			print "<<<<<<---File not Found-------->>>>>>"
			def prepare(self):
				raise tornado.web.HTTPError(404)
        		self.set_status(404)
        		self.write("404 FILE NOT FOUND")
        		self.write("<br>")
        		self.write("There are no files send a PUT request for creating a new file ")
	
	def delete(self, *args, **kwargs):
		os.remove("write_file.txt")
		print "<<<<<----file deleted---->>>>>"
		self.write("File Deleted")				
            



application = tornado.web.Application([
        (r"/", MainHandler),
	(r"/file_read", FileHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


