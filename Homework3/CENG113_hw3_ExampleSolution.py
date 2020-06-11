import os


def get_database_file_names():
    file_names_in_directory = os.listdir()  # A list of file names including extensions. e.g. ["Main.py", "students.hw3", "countries.hw3"]
    database_file_names = []
    for file_name_in_directory in file_names_in_directory:
        if file_name_in_directory[-4:] == ".hw3":  # If the file name ends with ".hw3" ...
            database_file_names.append(file_name_in_directory[:-4])  # Ignore the last 4 characters.
        # Otherwise, ignore the file.
    return database_file_names  # e.g. ["students", "countries"]


def get_lines(database_file_name): # e.g. "students"
    database_file = open(database_file_name + ".hw3", "r")
    all_lines = database_file.read().split("\n")[:-1]  # Ignore the last line which is empty.
    database_file.close()
    attributes_str = all_lines[0]  # First line defines the attributes (metadata)
    attributes = attributes_str.split(",")
    lines = all_lines[1:]  # Other lines contain the actual lines (data)
    return (attributes, lines)


def write_lines(database_file_name, attributes_str, lines):
    database_file = open(database_file_name + ".hw3", "w")
    database_file.write(attributes_str + "\n")
    for line in lines:
        database_file.write(line + "\n")
    database_file.close()


def is_valid_identifier(identifier):  # e.g. "python" is valid, but "python language" is invalid.
    if len(identifier) == 0:
        return False

    for character in identifier:
        if not character.isalnum() and character not in "_.@":
            return False
    return True


def are_valid_identifiers(identifiers_str):  # e.g. "python,java" is valid but "python, java" is invalid.
    identifiers = identifiers_str.split(",")
    for identifier in identifiers:
        if not is_valid_identifier(identifier):
            return False
    return True


def is_valid_operator(operator):  # e.g. "==" is valid but "<=" is invalid.
    return operator == "==" or operator == "!="


def create(file_name, attributes_str):
    attributes = attributes_str.split(",")
    if "id" in attributes:  # We use attributes, not attributes_str. Otherwise it will reject some valid attributes such as "hidden" which includes "id".
        print("You cannot create a file with attribute 'id'.")
        return

    database_file_names = get_database_file_names()

    # Here, duplicate attributes can be removed if they occur (But the order of the attributes should be preserved).
    # However, such corner case was not explained in the assignment definition.
    # So, we do not include that functionality here.

    out = open(file_name + ".hw3", "w")  # We create a file (if it already exists, the existing file is removed automatically.)
    out.write("id," + attributes_str + "\n")
    out.close()

    if file_name in database_file_names:
        print("There was already such a file. It is removed and then created again.")
    else:
        print("Corresponding file was successfully created.")


def delete(file_name):
    database_file_names = get_database_file_names()
    if file_name in database_file_names:
        os.remove(file_name + ".hw3")
        print("Corresponding file was successfully deleted.")
    else:
        print("There is no such file.")


def display():
    database_file_names = get_database_file_names()
    print("Number of files: " + str(len(database_file_names)))
    counter = 1
    for database_file_name in database_file_names:
        database_file = open(database_file_name + ".hw3")
        first_line = database_file.readline()  # Read a single line.
        attributes_str = first_line[:-1]  # Ignore the last character ("\n").
        database_file.close()
        print(str(counter) + ") " + database_file_name + ": " + attributes_str)
        counter = counter + 1


def add(values_str, file_name):
    database_file_names = get_database_file_names()
    if file_name not in database_file_names:
        print("There is no such file.")
        return

    database_file = open(file_name + ".hw3")
    first_line = database_file.readline()
    attributes_str = first_line[:-1]
    database_file.close()

    if len(values_str.split(",")) != len(attributes_str.split(",")) - 1:
        print("Numbers of attributes do not match.")
        return

    database_file = open(file_name + ".hw3", "r")
    lines = database_file.read().split("\n")[1:-1]  # Attributes and empty line are ignored.
    database_file.close()
    if len(lines) == 0:
        id = 1
    else:
        id = int(lines[-1].split(",")[0]) + 1  # Retrieve id of the last line, then add 1.
    database_file = open(file_name + ".hw3", "a")
    database_file.write(str(id) + "," + values_str + "\n")
    database_file.close()
    print("New line was successfully added to " + file_name + " with id = " + str(id) + ".")


def remove(file_name, condition_attribute, operator, condition_value):
    database_file_names = get_database_file_names()
    if file_name not in database_file_names:
        print("There is no such file.")
        return

    attributes, lines = get_lines(file_name)

    condition_attribute_index = -1
    for i in range(len(attributes)):
        if condition_attribute == attributes[i]:
            condition_attribute_index = i

    if condition_attribute_index == -1:
        print("Your query contains an unknown attribute.")
        return

    new_lines = []
    count = 0
    for line in lines:
        if operator == "==" and line.split(",")[condition_attribute_index] == condition_value:
            count = count + 1
        elif operator == "!=" and line.split(",")[condition_attribute_index] != condition_value:
            count = count + 1
        else:
            new_lines.append(line)

    attributes_str = ",".join(attributes)

    write_lines(file_name, attributes_str, new_lines)
    print(str(count) + " lines were successfully removed.")


def modify(attribute, file_name, value, condition_attribute, operator, condition_value):
    database_file_names = get_database_file_names()
    if file_name not in database_file_names:
        print("There is no such file.")
        return

    if attribute == "id":
        print("Id values cannot be changed.")
        return

    attributes, lines = get_lines(file_name)

    condition_attribute_index = -1
    for i in range(len(attributes)):
        if condition_attribute == attributes[i]:
            condition_attribute_index = i
    if condition_attribute_index == -1:
        print("Your query contains an unknown attribute.")
        return

    attribute_index = -1
    for i in range(len(attributes)):
        if attribute == attributes[i]:
            attribute_index = i
    if attribute_index == -1:
        print("Your query contains an unknown attribute.")
        return

    new_lines = []
    count = 0
    for line in lines:
        if (operator == "==" and line.split(",")[condition_attribute_index] == condition_value) \
                or (operator == "!=" and line.split(",")[condition_attribute_index] != condition_value):
            count = count + 1
            new_values = line.split(",")
            new_values[attribute_index] = value
            new_line = ",".join(new_values)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    attributes_str = ",".join(attributes)

    write_lines(file_name, attributes_str, new_lines)
    print(str(count) + " lines were successfully modified.")


def fetch(attributes_str, file_name, condition_attribute, operator, condition_value):
    file_names = get_database_file_names()
    if file_name not in file_names:
        print("There is no such file.")
        return

    file_attributes, file_lines = get_lines(file_name)

    attributes = attributes_str.split(",")

    condition_attribute_index = -1
    for i in range(len(file_attributes)):
        if condition_attribute == file_attributes[i]:
            condition_attribute_index = i
    if condition_attribute_index == -1:
        print("Your query contains an unknown attribute.")
        return

    indices_of_attributes = []
    for attribute in attributes:
        found = False
        for i in range(len(file_attributes)):
            if file_attributes[i] == attribute:
                indices_of_attributes.append(i)
                found = True
                break
        if not found:
            print("Your query contains an unknown attribute.")
            return

    related_file_lines = []
    for file_line in file_lines:
        if (operator == "==" and file_line.split(",")[condition_attribute_index] == condition_value) \
                or (operator == "!=" and file_line.split(",")[condition_attribute_index] != condition_value):
            related_file_lines.append(file_line)

    number_of_lines = len(file_lines)
    number_of_related_lines = len(related_file_lines)

    print("Number of lines in file " + file_name + ": " + str(number_of_lines))
    print("Number of lines that hold the condition: " + str(number_of_related_lines))

    table = []
    for line in related_file_lines:
        row = []
        cells = line.split(",")
        for index in indices_of_attributes:
            row.append(cells[index])
        table.append(row)

    if len(related_file_lines) == 0: # There is no line to print other than the attribute names.

        max_characters = []  # max_characters[i] is the maximum number of characters in i-th column
        for j in range(len(attributes)):
            max = len(attributes[j])
            max_characters.append(max)

        sum = 0
        for max in max_characters:
            sum = sum + max
        sum = sum + 3 * len(attributes) + 1
        print("-" * sum)

        meta_data_line = ""
        for i in range(len(attributes)):
            attribute = attributes[i]
            meta_data_line = meta_data_line + "| " + attribute + ((max_characters[i] - len(attribute)) * " ") + " "
        meta_data_line = meta_data_line + "|"
        print(meta_data_line)
        print("-" * sum)


    else: # There are at least 1 line to print.

        max_characters = []  # max_characters[i] is the maximum number of characters in i-th column
        number_of_rows = len(table)
        number_of_columns = len(table[0])
        for j in range(number_of_columns):
            max = 0
            for i in range(number_of_rows):
                current = len(table[i][j])
                if current > max:
                    max = current

            if len(attributes[j]) > max:
                max = len(attributes[j])

            max_characters.append(max)

        sum = 0
        for max in max_characters:
            sum = sum + max
        sum = sum + 3 * len(attributes) + 1
        print("-" * sum)

        meta_data_line = ""
        for i in range(len(attributes)):
            attribute = attributes[i]
            meta_data_line = meta_data_line + "| " + attribute + ((max_characters[i] - len(attribute)) * " ") + " "
        meta_data_line = meta_data_line + "|"
        print(meta_data_line)
        print("-" * sum)

        for row in table:
            row_str = ""
            for i in range(len(row)):
                cell = row[i]
                row_str = row_str + "| " + cell + ((max_characters[i] - len(cell)) * " ") + " "
            row_str = row_str + "|"
            print(row_str)

        print("-" * sum)


# ----------          MAIN PROGRAM          ----------#

# Note: We use suffix "_str" to distinguish a string from a list.
# e.g. attributes_str = "name,surname" but attributes = ["name", "surname"]

while True:
    query = input("What is your query?\n")

    if query == "x":
        break

    tokens = query.split(" ")

    if len(tokens) == 5 \
            and tokens[0] == "create" \
            and tokens[1] == "file" \
            and is_valid_identifier(tokens[2]) \
            and tokens[3] == "with" \
            and are_valid_identifiers(tokens[4]):

        file_name = tokens[2]
        attributes_str = tokens[4]
        create(file_name, attributes_str)

    elif len(tokens) == 3 \
            and tokens[0] == "delete" \
            and tokens[1] == "file" \
            and is_valid_identifier(tokens[2]):

        file_name = tokens[2]
        delete(file_name)

    elif len(tokens) == 2 \
            and tokens[0] == "display" \
            and tokens[1] == "files":

        display()

    elif len(tokens) == 4 \
            and tokens[0] == "add" \
            and are_valid_identifiers(tokens[1]) \
            and tokens[2] == "into" \
            and is_valid_identifier(tokens[3]):

        values_str = tokens[1]
        file_name = tokens[3]
        add(values_str, file_name)

    elif len(tokens) == 8 \
            and tokens[0] == "remove" \
            and tokens[1] == "lines" \
            and tokens[2] == "from" \
            and is_valid_identifier(tokens[3]) \
            and tokens[4] == "where" \
            and is_valid_identifier(tokens[5]) \
            and is_valid_operator(tokens[6]) \
            and is_valid_identifier(tokens[7]):

        file_name = tokens[3]
        condition_attribute = tokens[5]
        operator = tokens[6]
        condition_value = tokens[7]
        remove(file_name, condition_attribute, operator, condition_value)

    elif len(tokens) == 10 \
            and tokens[0] == "modify" \
            and is_valid_identifier(tokens[1]) \
            and tokens[2] == "in" \
            and is_valid_identifier(tokens[3]) \
            and tokens[4] == "as" \
            and is_valid_identifier(tokens[5]) \
            and tokens[6] == "where" \
            and is_valid_identifier(tokens[7]) \
            and is_valid_operator(tokens[8]) \
            and is_valid_identifier(tokens[9]):

        attribute = tokens[1]
        file_name = tokens[3]
        value = tokens[5]
        condition_attribute = tokens[7]
        operator = tokens[8]
        condition_value = tokens[9]
        modify(attribute, file_name, value, condition_attribute, operator, condition_value)

    elif len(tokens) == 8 \
            and tokens[0] == "fetch" \
            and are_valid_identifiers(tokens[1]) \
            and tokens[2] == "from" \
            and is_valid_identifier(tokens[3]) \
            and tokens[4] == "where" \
            and is_valid_identifier(tokens[5]) \
            and is_valid_operator(tokens[6]) \
            and is_valid_identifier(tokens[7]):

        attributes_str = tokens[1]
        file_name = tokens[3]
        condition_attribute = tokens[5]
        operator = tokens[6]
        condition_value = tokens[7]
        fetch(attributes_str, file_name, condition_attribute, operator, condition_value)

    else:
        print("Invalid Query.")

    print("")