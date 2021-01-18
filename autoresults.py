from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
import csv
import time

filename="sem_2_results.csv"
f=open(filename,'w')
header = "rollno,name,pointer,pps,maths,phy,graphics,pps_lab,workshop,phy_lab\n"

# write into the file 
f.write(header) 


driver=webdriver.Chrome()
start_roll_no = 19733001
end_roll_no = 19733060

for i in range(start_roll_no, end_roll_no + 1):
    
	        # paste the link upboard website 
		driver.get("http://202.63.117.72/result_2020/12/index.php") 
		
		# roll number start with zero then change into string 
		t= '1005'+str(i) 
		
		# find the element where we have to 
		# enter the xpath target rollnumber box 
		# and put rollnumber value who store in t. 
		driver.find_element_by_name("htno").send_keys(t) 
		
		# paste the xpath of submit button 
		driver.find_element_by_name("submit").click()

		rollno=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div').text 

		# name of student's x_path copy and get text of element 
		name=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]').text 
		
		# result of student's x_path copy and get text of element 
		pps=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[2]/td[3]/div').text

		maths=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[3]/td[3]/div').text

		phy=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[4]/td[3]/div').text

		graphics=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[5]/td[3]/div').text

		pps_lab=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[6]/td[3]/div').text

		workshop=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[7]/td[3]/div').text

		phy_lab=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[1]/tbody/tr[8]/td[3]/div').text

		pointer=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td/span/table[2]/tbody/tr/td[2]').text
		
		f.write(rollno + "," + name + "," + pointer + "," + pps + "," + maths +"," +phy +"," +graphics +"," +pps_lab +"," +workshop +"," +phy_lab +"\n" )
		
		
                #to display result
	    
driver.close()
f.close()

		

