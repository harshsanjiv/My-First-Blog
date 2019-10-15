#DOCTOR MANAGEMENT

class PATIENT:
    patient_full_name="default"
    patient_first_name="default"
    patient_last_name="default"
    patient_age=0
    purpose="default"

    date_of_visit="default"
    def new_patient(self):
        self.patient_first_name=str(input("Enter the first name of the patient:"))
        self.patient_last_name=str(input("Enter the last name of the patient:"))
        self.patient_full_name=self.patient_first_name+self.patient_last_name
        self.patient_age=int(input("Enter the age of the patient:"))
        self.purpose=str(input("Enter the purpose of the patient:"))
        input_medicine=str(input("Enter medicines using a space with quantity in brackets:"))
        medicine_list=list(input_medicine.split())
        self.date_of_visit=str(input("Enter the date of visit in DD/MM/YY format:"))

        fo=open(self.patient_full_name.txt,"w")
        fo.write(self.date_of_visit,"\n")
        fo.write(self.patient_age,"\n")
        fo.write(self.purpose,"\n")
        fo.write(medicine_list,"\n\n")

        fo.close()











print("Dr. SEEMA SRIVASTAVA'S CLINIC")

print("1.Enter a new patient into the directory")
print("2.Review a existing patient's record")
option=int(input("Enter the number next to the given operation:"))

while(option!=1 and option!=2):
    print("Invalid input! Please reenter a appropriate option corresponding the given key")
    option=int(input("Enter the number next to the given operation:"))
p=PATIENT()
if option is 1:
    p.new_patient()
elif option is 2:
    p.existing_patient()