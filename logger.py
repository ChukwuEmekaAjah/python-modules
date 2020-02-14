# imports would come here
# i need access to date, os and file modules
from datetime import datetime

logs_container = []

def log_to_file(message, destination):
	print("logging from the file option")
	print(message)

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
	log_message = create_message(message, options)
	logs_container.append(log_message)
	destinations = {
		"file" : log_to_file,
		"remote" : log_to_remote,
		"console" : log_to_console
	}
	destinations[(options.get('destination') and options.get("destination").get("type")) or "console"](log_message, 'error.log')


def get_logs(options = {}):
	return logs_container



log("The world is a messy place ", {"destination":{"type":"file" }})
log("The world is a messy place ", {"destination":{"type":"file" }})
print(get_logs())