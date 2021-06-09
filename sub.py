import argparse
import requests

def banner():
	#Banner creation
	print( """
                                                                                                                                                             
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗  
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                                                                                                 
                                                                                                          OPEN-SOURCE PROJECT | https://github.com/Amrita2000 
                                                                                                           BY AMRITA NAYAK

""")
	helpmenu()
#HELP MENU LIST
def helpmenu():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', dest='DOMAIN' ,help='Specify Your URL')
	parser.add_argument('-w', dest='WORDLIST' ,help='Specify Your Wordlists')
	args = parser.parse_args()
	domain = args.DOMAIN
	with open(args.WORDLIST) as file:
		  wd=file.readlines()
	automate(domain,wd)
	
def automate(domain,wordlist):
	for i in wordlist:
	 	newurl=i.rstrip("\n")+"."+domain
	 	#response1 = requests.get("https://"+newurl)#checks for https requests
	 	#response2 = requests.get("http://"+newurl)#checks for http requests

	 	try:
	 		response1 = requests.get("https://"+newurl)
	 		response2 = requests.get("http://"+newurl)
	 		if (response1.status_code == 200 or response2.status_code == 200):
	 			print("[+] 200",newurl)
	 		elif (response1.status_code == 403 or response2.status_code == 403):
	 			print("[+] 403",newurl)
	 		elif (response1.status_code == 301 or response2.status_code == 301):
	 			print("[+] 301",newurl)
	 		
	 	except requests.ConnectionError:
	 			pass
	 			print("[+]URL NOT PRESENT",newurl)



	    



if __name__ == "__main__":
	banner()