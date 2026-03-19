
def read_ips():
	# TODO
	# read all content of file as string
	# put all ips in a list
	# filter out double ips, only unique ips in the list
	# return list

def get_pattern():
	# see https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
	# uses regex to determine of IP address is a valid IP in the range:
	# 47.82.11.0 - 47.82.11.255
    # return the pattern, so something like r"^47.....$"

def filter_ips(all_ips):
	correct = list()
    # TODO
	# receives a list with a lot of possible IP addresses
	# filters out only valid addresses using the function: get_pattern()
	# returns a list with valid IP addresses
	# the list contains no identical IP's, so filter for doubles.

def main():
	# do not change below code
	all_ips = read_ips()
	correct_ips = filter_ips(all_ips)
	for p in correct_ips:
		print(p)
	print(len(correct_ips))

if __name__ == "__main__":
	main()
