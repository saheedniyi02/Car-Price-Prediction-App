from bs4 import BeautifulSoup
import requests
import csv

csv_file=open("CarMart.csv","w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Name","Price","Model","Year","Condition","Transmission","Fuel Type","Location","Mileage"])
index=1
for page in range(1,182):
	link="https://carmart.ng/cars-for-sale?page={page}"
	req_page=requests.get(link).text
	soup_page=BeautifulSoup(req_page,"html.parser")
	car_links=[car_link.a.get("href") for car_link in soup_page.find_all("div",class_="items-details") ]
	for each_link in car_links:
		index+=1
		try:
			req_each=requests.get(each_link).text
			soup=BeautifulSoup(req_each,"html.parser")
			page_body=soup.body
			title=page_body.find("div",class_="inner").h2.strong.a.text
			price=page_body.find("div",class_="posts-image").h1.text
			location=page_body.find("span",class_="item-location").text
			features=page_body.find("div",class_="row",id="cfContainer").find_all("div",class_="detail-line")
			important_features=features[0:len(features)-1]
			for feature_val in important_features:
				feature_and_val=[feature.text for feature in feature_val.find("div",class_="rounded-small").find_all("span")]
				if feature_and_val[0]=="Model":
					Model=feature_and_val[1]
				elif feature_and_val[0]=="Year":
					Year=feature_and_val[1]
				elif feature_and_val[0]=="Fuel Type":
					FuelType=feature_and_val[1]
				elif feature_and_val[0]=="Condition":
					Condition=feature_and_val[1]
				elif feature_and_val[0]=="Transmission":
					Transmission=feature_and_val[1]
				elif feature_and_val[0]=="Mileage":
					Mileage=feature_and_val[1]
			row=[title,price,Model,Year,Condition,Transmission,FuelType,location,Mileage]
			csv_writer.writerow(row)
			print(index)
		except:
			pass
	print(page)
csv_file.close()