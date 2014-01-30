from add import add
def test_add_two_numbers():
	result=add(10,1)
	print result
	assert 11==result
	print "Test Case 1 is executed successfully"

def test_add_strings():
	result=add("User","Case")
	print result
	assert "UserCase"==result
	print "Test Case 2 is executed successfully"

def test_add_lists():
	result=add(["Hello"],["Talat"])
	print result
	assert ['Hello','Talat']==result
	print "Test Case 3 is executed successfully"

if __name__ == '__main__':
	test_add_two_numbers()	
	test_add_strings()
	test_add_lists()
