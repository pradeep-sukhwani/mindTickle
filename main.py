import os
import csv
import json


def main():
    """
    # Reads the data file, loads the json
    # get the max manager's length to compare the user's manager if less than max then filled it with the 'N/A'
    # half_formated_data is used for the writing the data in the csv file
    # manager_data is to verify that the user is manager or not if manager then get the level of that user
    # returns the half_formated_data, manager_data, max_manager_length
    """
    with open(os.getcwd() + '/data') as file_obj:
        read_file = file_obj.read()
        json_data = json.loads(read_file)
        # Getting max length of Managers
        # For the better readability I have used sorted() function
        max_manager_length = len(sorted(list(json_data.values()), key=len, reverse=True)[0])
        half_formated_data = [] # used for writing the data in generate() function
        manager_data = {} # used for checking the user is manager or not in generate() function

        for user_email, manager_details in json_data.items():
            current_detail = [user_email] # first column will be user's email

            for detail in manager_details:
                manager_data.update({detail.get('email') : detail.get('title')})
                current_detail.append(detail.get('email'))

            # append N/A if the current user's manager list length is not equal to the max manager
            numb_of_na  = max_manager_length - len(current_detail)
            for count in range(numb_of_na + 1):
                current_detail.append("N/A")
        	# half_formated_data has all the rows except level which I will get in below function
            half_formated_data.append(current_detail)
        return half_formated_data, manager_data, max_manager_length


def get_level(title):
    """
    level_dict:
    # key is the title which will get from the user's data
    # value is the number which will show the level of that user
    as 1 being the highest and 10 being the lowest
    # Here level 10 suggest the other category such as 'abc'
    """
    level_dict = {
        'president': 1,
        'svp': 2,
        'senior vice president': 2,
        'vice president': 3,
        'vp': 3,
        'senior director': 4,
        'sr. director': 4,
        'sr director': 4,
        'sr dir': 4,
        'director': 5,
        'chief': 5,
        'dir': 5,
        'head': 6,
        'sr mgr': 7,
        'sr manager': 7, "sr. manager": 7, "senior manager": 7, "senior sales manager": 7,
        'mgr': 8,
        'manager': 8,
        'supervisor': 9,
    }
    level = 10 # Others
    for key, value in level_dict.items():
        if title.lower().find(key) != -1:
            level = value
    return level

def generate_csv():
    """
    # Get the data from main() function
    # open the output file which creates/edit if exist
    # first writerow: writes the Headers such as user, manager_1, manager_2, ..., level
    # in for loop: it checks the data[0] - user_email is in manager's list or not
    # if it is in manager's list than it get's level as number
    # else it append '11'
    # in the for loop it adds the word 'L' if the integer is not 11 or else replaces 11 with 'N/A'
    # Here I have used 11 because of sorting as I have sorted the level from highest to lowest
    # so here 11 for the user's manager is not available which is why I replace with 'N/A'
    # Sorts the formated_data by level which is last element [-1]
    # second writerow: writes the data
    """
    half_formated_data, manager_data, max_manager_length = main()
    formated_data = []
    for data in half_formated_data:
        if data[0] in manager_data.keys(): # Here data[0] is the user_email from the main() function
        	# appending level if user is manager
            data.append(get_level(manager_data[data[0]]))
        else:
        	# appending 11 if user is not manager which will be replaced to N/A right after sorting
            data.append(11)
        formated_data.append(data)
    # sorting from highest to lowest level since I have x[-1] as level number which needs to be sorted
    formated_data = sorted(formated_data, key=lambda x: x[-1])
    with open('output.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        # writes the Header row to csv file - creates the list for the header
        # user, manager_1, manager_2, ... ,level
        writer.writerow(['user'] + ["manager_" + str(i+1) for i in range(max_manager_length)] + ['level'])
        for data in formated_data:
        	# replacing number 11 from N/A
            if data[-1] == 11:
                data[-1] = 'N/A'
            else:
            	# appending word 'L' in front of number to make it level
                data[-1] = 'L' + str(data[-1])
            # writes the data
            writer.writerow(data)


if __name__ == '__main__':
    generate_csv()
