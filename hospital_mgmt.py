
# List to store all patient records
patients = []

# Function to register a new patient
def register_patient():

    # Taking patient details from the user
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")

    # Creating a dictionary to store patient information
    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Doctor": "",
        "Bill": 0
    }

    # Adding the patient record to the list
    patients.append(patient)

    print("Patient Registered Successfully!")


# Function to assign a doctor to a patient
def assign_doctor():

    # Asking for the patient ID
    patient_id = input("Enter Patient ID: ")

    # Searching the patient in the list
    for patient in patients:
        if patient["ID"] == patient_id:

            # Assigning a doctor
            doctor = input("Enter Doctor Name: ")
            patient["Doctor"] = doctor

            print("Doctor Assigned Successfully!")
            return

    print("Patient Not Found!")



# Function to generate the patient's bill
def generate_bill():

    # Asking for the patient ID
    patient_id = input("Enter Patient ID: ")

    # Searching the patient
    for patient in patients:
        if patient["ID"] == patient_id:

            # Taking bill amount
            bill = float(input("Enter Bill Amount: "))
            patient["Bill"] = bill

            print("Bill Generated Successfully!")
            return

    print("Patient Not Found!")




# Function to display all patient records
def display_records():

    # Check if there are no records
    if len(patients) == 0:
        print("No Patient Records Found.")
        return

    # Display all patient details
    for patient in patients:
        print("\n---------------------------")
        print("Patient ID :", patient["ID"])
        print("Name       :", patient["Name"])
        print("Age        :", patient["Age"])
        print("Gender     :", patient["Gender"])
        print("Disease    :", patient["Disease"])
        print("Doctor     :", patient["Doctor"])
        print("Bill       :", patient["Bill"])


# Main menu of the Hospital Patient Management System
while True:

    # Displaying menu options
    print("\n===== Hospital Patient Management System =====")
    print("1. Register Patient")
    print("2. Assign Doctor")
    print("3. Generate Bill")
    print("4. Display Patient Records")
    print("5. Exit")

    # Taking user's choice
    choice = input("Enter Your Choice: ")

    # Calling functions based on user choice
    if choice == "1":
        register_patient()

    elif choice == "2":
        assign_doctor()

    elif choice == "3":
        generate_bill()

    elif choice == "4":
        display_records()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")                    