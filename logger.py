# imports would come here
# i need access to date, os and file modules
from datetime import datetime
import pickle

#pickle.dump(data, destination)
#pickle.load(address)

logs_container = []

def set_up(destination_address):
	global logs_container
	log_file = open(destination_address, "rb")
	logs_container = pickle.load(log_file)

def log_to_file(message, destination_address):
	print("logging from the file option")
	log_file = None
	try:
		log_file = open(destination_address, "wb")
		pickle.dump(logs_container, log_file)
		print("Successfully added message")
	except Exception as er:
		print("there was an error ooo")
		print(er)
	finally:
		if log_file is not None:
			log_file.close()

def log_to_remote(message, destination):
	pass

def log_to_console(message, destination):
	print(message)
	pass

def create_message(message, options = {}):
	message_object = {}
	message_object['time'] = str(datetime.now())
	message_object['message'] = str(message)
	message_object['severity'] = (options.get('severity') and options.get('severity')) or 1
	message_object['source'] = (options.get('source') and options.get('source')) or 'anon'
	return message_object

# method for logging message to destination
def log(message = None, options = {}):
	global logs_container
	log_message = create_message(message, options)
	logs_container.append(log_message)
	destinations = {
		"file" : log_to_file,
		"remote" : log_to_remote,
		"console" : log_to_console
	}
	log_destination_type = (options.get('destination') and options.get("destination").get("type")) or "console"
	log_destination_address =(options.get('destination') and options.get("destination").get("address")) or "errors.log"
	destinations[log_destination_type](log_message, log_destination_address)


def get_logs(options = {}):
	return logs_container


if __name__ == "__main__":
	set_up("errors.log")

log("The world is a messy place ", {"destination":{"type":"file", "address":"errors.log" }})
log("The world is a messy place ", {"destination":{"type":"file" }})
print("logs ")
print(get_logs())
