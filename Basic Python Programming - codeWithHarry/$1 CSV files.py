import csv

# Reading a CSV file
with open("$2competition.csv") as f:
    content_of_f = csv.reader(f)
    potter_competitions = []  # empty list to store read lines
    for each_line in content_of_f:
        print(each_line)

# # Writing a CSV file
# with open("$2competition.csv", "w", newline="") as f:
#     data_handler = csv.writer(f, delimiter=",")
#     data_handler.writerow(["Year", "Event", "Winner"])
#     data_handler.writerow(["1995", "Best-kept Lawn", "None"])
#     data_handler.writerow(["1999", "Gobatones", "Welch National"])
#     data_handler.writerow(["2006", "World Cup", "Burkina Faso"])

# # Appending a CSV file
# with open("$2competition.csv", "a", newline="") as f:
#     data_handler = csv.writer(f, delimiter=",")
#     data_handler.writerow(["2000", "Hello World", "Go one"])

