try:
	x = 1.0/0.0
except ZeroDivisionError:
	print "got it! i'm awesome"
finally:
	raiseTypeError("Just Kidding!")

