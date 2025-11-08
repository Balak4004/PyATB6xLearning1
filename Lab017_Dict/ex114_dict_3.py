

student_info_1 = {
"name":"Aman",
    "age":34,
    "address":{
        "home_address":"ND",
        "office_address":"KA"
    }
}

student_info_2 = {
"name":"Rohan",
    "age":25,
    "address":{
        "home_address":"Goa",
        "office_address":"MH"
    }
}

student_list = [student_info_1,student_info_2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[1]["address"]["home_address"])
