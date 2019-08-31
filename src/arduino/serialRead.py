from	time	import sleep
import	threading
import	serial

try:
	device	= serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
except serial.serialutil.SerialException:
	try:
		device	= serial.Serial('/dev/ttyUSB1', 9600, timeout=.1)
	except Exception as e:
		device	= None

def start():
	sleep(1)
	if threading.active_count() == 3:
		return
	if device:
		checkSerial()
	else:
		sleep(5)
		print("Dispositivo não conectado!")
		sleep(20)
		start()

hello	= False
list	= []
def checkSerial():
	global hello, list
	if not hello:
		device.write("@".encode())
		sleep(.2)
		response	= device.readline().decode()
		if response == "@@":
			hello	= True
			sleep(.1)
	if hello:
		device.write(str.encode("$"))
		sleep(.1)
		response	= device.readline().decode()
		if response:
			if response[0] == "$" and response[-1:] == "$":
				code	= response[1:-1]
				if list and next((item for item in list if item["code"] == code), None):
					sleep(1)
					checkSerial()
			elif response == "#":
				checkSerial()
			else:
				sleep(.1)
				device.write(str.encode("!"))
				sleep(.1)
				hello	= False
				checkSerial()
		else:
			sleep(.1)
			device.write(str.encode("!"))
			sleep(.1)
			hello	= False
			checkSerial()
		sleep(.2)
		device.write(str.encode("%"))
		sleep(.1)
		response	= device.readline().decode()
		if response:
			if response[0] == "%" and response[-1:] == "%":
				weight	= response[1:-1]
			elif response == "#":
				checkSerial()
			else:
				sleep(.1)
				device.write(str.encode("!"))
				sleep(.1)
				hello	= False
				checkSerial()
		else:
			sleep(.1)
			device.write(str.encode("!"))
			sleep(.1)
			hello	= False
			checkSerial()
	else:
		sleep(1)
		checkSerial()
	if code and weight:
		list.append({
			"code": code,
			"weight": weight
		})
		postData()
		print(list)
		sleep(1)
		checkSerial()

def postData():
	return ""
