# programming_dictionary={
#     "Bug":"An error in a program that prevents the program from running as expected.", 
#     "Function":"A piece of code that you can easily call over and over again.",
    
# }

# # print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again" 



# # empty_dictionary = {}

# # programming_dictionary = {}

# # print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#Nesting a dictionary

# travel_log={
#     "Nepal":{"Cities_visited": ["Kathmandu", "Bhaktapur", "Dalitpur"], "total_visits" : 12},
#     "USA": {"Cities_in_usa" :["Texas", "California", "Hawai"], "total_visits" : 3}
    
# }
# print(travel_log)

#Nesting a dictionary in a list


travel_log=[
    {
   "country": "Nepal", 
   "Cities_visited": ["Kathmandu", "Bhaktapur", "Dalitpur"],
   "total_visits" : 12
},
    {
   "country": "USA",
   "Cities_in_usa" :["Texas", "California", "Hawai"], 
   "total_visits" : 3
    }
]
print(travel_log)