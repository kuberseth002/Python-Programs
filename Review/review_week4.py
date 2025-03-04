# take fname,lname,age,phone number 
#  decode in +91 900XXXXXx
import pandas as pd

import re

data={
    "fname":["kuber","Ajay","Rakesh"],
    "lname":["Seth","Sharama","Kumar"],
    "age":["23","45","50"],
    "phone":["8524263","741852963","7852134668"]
}

df=pd.DataFrame(data)

name_pattern=r"^[A-Za-z]+$"
age_pattern=r"^\d+$"
phone_pattern=r"^\+91\d{10}$"


def valid_name(name):
    return bool(re.match(name_pattern,name))

def valid_age(age):
    return bool(re.match(age_pattern,age))

def valid_phone(phone):
    return bool(re.match(phone_pattern,phone))

df["fname_name"]=df["fname"].apply(valid_name)
df["lname_name"]=df["lname"].apply(valid_name)
df["valid_age"]=df["age"].apply(valid_age)
df["valid_phone_number"]=df["phone"].apply(valid_phone)

print(df)
    
    
    