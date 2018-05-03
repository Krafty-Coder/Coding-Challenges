def validate_pin(pin):
    if type(int):
        if not type(float) and pin>0:
	    if (len == 4) or (len == 6):
                print('True')
	        return True
	    else:
                print('False')
	        return False
        else:
            print('True')
            return True
    else:
        print('False')
        return False

validate_pin(0.234)
