# weather_data_list = []
# with open("weather_data.csv") as weather:
#     for element in weather.readlines():
#         weather_data_list.append(element.strip())
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1])

import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list  = data["temp"].tolist()
# # av_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# # print(av_temp)
# # print(max_temp)
#
# #Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp_in_c = (monday.temp * 1.8) + 32
# print(monday_temp_in_c)

#Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("students.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_list = data["Primary Fur Color"].to_list()
gray_count = fur_list.count("Gray")
red_count = fur_list.count("Cinnamon")
black_count = fur_list.count("Black")

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}
squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")

