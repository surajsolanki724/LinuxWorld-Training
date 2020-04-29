#!/usr/bin/python36
import os
import subprocess
import cv2
import getpass

os.system('tput setaf 5')
print("\t\t\t Welcome to Tool Menu")
print("\t\t\t =====================")
os.system('tput setaf 0')

ps="redhat"
passwd=getpass.getpass("enter the password")
if passwd != ps:
	print("not auth")
else:

	print("\nWhere do you wish to execute th tool local or remote : ")
	system = input()
	print("\nSystem is : {}".format(system))


	if system == "local":
		os.system("tput setaf 3")

					######--------MENU LIST--------#######
		while True:
			

	
			print ("""
			press 0 to exit
			press 1 to create user
			press 2 to check time
			press 3 to open calander
			press 4 to display list of files and directory
			press 5 to make a new directory
			press 6 to remove directory
			press 7 to take photo
			press 8 to live streaming
			press 9 to take mobile photo
			press 10 to mobile live streaming
			press 11 to mobile camera merge
			press 12 to count face
			press 13 to face detect
			press 14 to face sample collect
			press 15 to train model
			press 16 to recognize face
			""")
					####---choice code----#####
			

			print("\nEnter your choice : ",end='')
			ch=input()
			print("\nThe entered choice is {}".format(ch))


					   ####----user created code----#####
	
			if int(ch) == 1:
				print("\nenter username")
				user_name=input()
				x = subprocess.getstatusoutput("useradd {}".format(user_name))
				print(x)

				if x[0]==0:
					print("user created")
				else:
					print("error created user {}".format(x[1]))

				            ###----cal,time,show file code----####


			elif int(ch) == 2:
				print("time is :")
				x = subprocess.getoutput("clock")
				print(x)

			elif int(ch) == 3:
				print("calender")
				x = subprocess.getoutput("cal")
				print(x)

			elif int(ch) == 4:
				print("show file")
				x = subprocess.getoutput("ls")
				print(x)

				                ####---- directory code----####


			elif int(ch) == 5:
				print("\nenter directory name")
				d_name=input()
				x = subprocess.getstatusoutput("mkdir /root/Desktop/{}".format(d_name))
				print(x)

				if x[0]==0:
					print("dir created")
				else:
					print("error created dir {}".format(x[1]))
	
			elif int(ch) == 6:
				print("\nenter directory name")
				d_name=input()
				x = subprocess.getstatusoutput("rmdir /root/Desktop/{}".format(d_name))
				print(x)

				if x[0]==0:
					print("removed dir")
				else:
					print("error removed dir {}".format(x[1]))

						#####----webcam code ----####

			elif int(ch) == 7:
				print("\ntake a photo : enter program file cam.py : ",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {} : ".format(pg_file))
				print("photo capture")
	
			elif int(ch) == 8:
				print("\nstart live streaming : enter program file live_streaming.py:",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {} :".format(pg_file))
				print("you r live")
	
	

						#####-----mobile cam code-----#####
	

			elif int(ch) == 9:
				print("\n take a photo using mobile : enter the program code mobile_photo.py :",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {} : ".format(pg_file))
				print("photo captured")

			elif int(ch) == 10:
				print("\n mobile live streaming : enter the code phone_live.py :",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {} :".format(pg_file))
				print("live streaming on mobile")
				 
				             ###-----merge mobile cam code----#####

			elif int(ch) ==11:
				print("\n enter url1,2,3",end='')
				x=subprocess.getoutput("python36 camera_merge.py")
				print("camera live")



			elif int(ch) == 12:
				print("\ enter the code to face count : face_count.py",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {}".format(pg_file))
				print(x)


			elif int(ch) == 13:
				print("\ enter the code to face detect : face_detect.py",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {}".format(pg_file))
				print(x)

			elif int(ch) == 14:
				print("\ enter the code to send mail : mail.py",end='')
				pg_file=input()
				x=subprocess.getoutput("python36 {}".format(pg_file))
				print(x)
				
					#####-------face recognization code-----######


					
			elif int(ch) == 15:
				print("\ collect face sample)
				x=subprocess.getoutput("python36 collectface.py)
				print(x)
				
			elif int(ch) == 16:
				print("\ train model)
				x=subprocess.getoutput("python36 trainmodel.py)
				print("train successfull")
				
			elif int(ch) == 17:
				print("\ face recognization")
				x=subprocess.getoutput("python36 recognition.py)
				print("recognize successfull")
					####-----exit code---#####	
	
			elif int(ch) == 0:
				print("\nThank You")
				x = subprocess.getoutput("exit")
				



############################--------- Remote host code -------#################################################



	elif system == "remote":


			print("Enter IP Address to remote access the device : ",end='')
			ip=input()
	

			os.system("tput setaf 1")
							#####--------MENU LIST------######
			print ("""
			press 0 to exit
			press 1 to create user
			press 2 to check time
			press 3 to open calander
			press 4 to display list of files and directory
			press 5 to make a new directory
			press 6 to remove directory
			press 7 to ping
			press 8 to passwordless authentication
			press 9 to passwordless authentication removed
			press 10 to capture photo
			press 11 to live streaming
			""")
						####--------enter choice-----######
			os.system("tput setaf 5")

			print("\nEnter your choice : ",end='')
			ch=input()
			print("\nThe entered choice is {}".format(ch))

						  ####----user created code----#####

			if int(ch) == 1:
				print("\nenter username")
				user_name=input()
				x = subprocess.getstatusoutput("ssh {} useradd {}".format(ip,user_name))
				print(x)

				if x[0]==0:
					print("user created")
				else:
					print("error created user {}".format(x[1]))

					
						####---- directory code----####

			elif int(ch) == 5:
				print("\nenter directory name")
				d_name=input()
				x = subprocess.getstatusoutput("ssh {} mkdir /root/Desktop/{}".format(ip,d_name))
				print(x)

				if x[0]==0:
					print("dir created")
				else:
					print("error dir created {}".format(x[1]))
	

			elif int(ch) == 6:
				print("\nenter directory name")
				d_name=input()
				x = subprocess.getstatusoutput("ssh {} rmdir /root/Desktop/{}".format(ip,d_name))
				print(x)
				if x[0]==0:
					print("directory removed")
				else:
					print("error removed directory {}".format(x[1]))

	

						####-----passwordless authentication code----###

			elif int(ch) == 8:
				print("\ passwrdless authenticaton ")
				x=subprocess.getoutput("ssh-keygen")
				y=subprocess.getstatusoutput("ssh-copy-id {}".format(ip))
				if y[0]==0:
					print("successfull authentication")
				else:
					print("copy-id error {}".format([1]))
	

			elif int(ch) == 9:
				print("\ passwrdless authenticaton removed ")
		
				y=subprocess.getstatusoutput("ssh {} rm  /root/.ssh/authorized_keys".format(ip))
				if y[0]==0:
					print("successfull removed authentication")
				else:
					print("removed error {}".format([1]))

		
						#####----webcam code ----####


	
			elif int(ch) == 10:
				print("remote host photo click",end='')
		
				cmd1 = "scp /root/Desktop/pycode/cam.py {}:/root/Desktop/cam.py".format(ip)
				cmd2 = "ssh {} python36 /root/Desktop/cam.py".format(ip)
				cmd3 = "scp {}:/root/Desktop/suraj.png /root/Desktop/suraj.png".format(ip)
				subprocess.getoutput(cmd1)
				subprocess.getoutput(cmd2)
				subprocess.getoutput(cmd3)
				print("photo capture")
	


			elif int(ch) == 11:
				print("\to live remote host ")
				cmd1="scp /root/Desktop/pycode/access_vid.py {}:/root/Desktop/access_vid.py".format(ip)
				cmd2="ssh -X {} python36 /root/Desktop/access_vid.py".format(ip)
		
				subprocess.getoutput(cmd1)
				subprocess.getoutput(cmd2)
	
				print("live streaming")

							####----exit code---####


			elif int(ch) == 0:
				print("\nThank You")
				x = subprocess.getoutput("exit")
				print(x)
			input("to continue:")
			
