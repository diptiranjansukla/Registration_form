import streamlit as st
from app import load_template, replace_placeholders, save_customized_docx

# Define the path to the student registration template
template_path = "student_registration_form.docx"

st.title("Student Registration Form Generator")

# Input fields for student registration data
session = st.text_input("Session", value="2023-2024")
institute_roll_no = st.text_input("Institute Roll No.", value="IGIT2023123")
date_of_submission_of_registration_form = st.date_input("Date of Submission of Registration Form")
admission_fees_bank = st.text_input("Admission Fees Deposited in Bank", value="5000")
date_of_deposit = st.date_input("Date of Deposit")
hostel_or_dayscholar = st.radio("Hostel or Dayscholar", ('Hostel', 'Dayscholar'))
sem_admission_required = st.text_input("Semester in which Admission is Required", value="4th")
sem_exam_cleared = st.text_input("Semester Examination Already Cleared", value="3rd")
year_of_first_admission = st.text_input("Year of First Admission in 1st Year at IGIT", value="2020")
state_council_regd_no = st.text_input("State Council Registration No.", value="AB123456")
roll_no = st.text_input("Roll Number", value="123456")
student_name = st.text_input("Student Name", value="John Doe")
signature_of_student = st.text_input("Signature of the Student", value="John Doe")

# Category selection (with tick mark)
category = st.selectbox(
    "Select Category:",
    ["General", "SC", "ST", "Ph.H", "GC", "Ex.Military", "Sp.Man", "NCC", "MCL"]
)

# Generate the customized student registration form
if st.button("Generate Student Registration Form"):
    # Create tick marks based on category choice
    tick = "✓"
    placeholders = {
        "{Session}": session,
        "{Institute_Roll_No}": institute_roll_no,
        "{Date_of_Submission_of_Registration_form}": str(date_of_submission_of_registration_form),
        "{Admission_fees_deposited_in_Bank}": admission_fees_bank,
        "{Date_of_deposit}": str(date_of_deposit),
        "{Hostellor_or_Dayscholar}": hostel_or_dayscholar,
        "{Semester_in_which_admission_is_required}": sem_admission_required,
        "{Semester_Examination_Already_Cleared}": sem_exam_cleared,
        "{Year_Of_First_Admission_In_1_st_year_at_IGIT}": year_of_first_admission,
        "{State_Council_Regd_No}": state_council_regd_no,
        "{Roll_No}": roll_no,
        "{student_name}": student_name,
        "{Signature_of_the_student}": signature_of_student,
        # Place the tick only for the selected category, others will remain empty
        "{General}": tick if category == "General" else "",
        "{SC}": tick if category == "SC" else "",
        "{ST}": tick if category == "ST" else "",
        "{Ph.H}": tick if category == "Ph.H" else "",
        "{GC}": tick if category == "GC" else "",
        "{Ex.Military}": tick if category == "Ex.Military" else "",
        "{Sp.Man}": tick if category == "Sp.Man" else "",
        "{NCC}": tick if category == "NCC" else "",
        "{MCL}": tick if category == "MCL" else ""
    }
    
    # Load the DOCX template
    doc = load_template(template_path)
    
    # Replace placeholders with provided data
    doc = replace_placeholders(doc, placeholders)
    
    # Save the completed registration form
    output_path = "Completed_Student_Registration_Form.docx"
    save_customized_docx(doc, output_path)
    
    st.success("Student Registration Form generated successfully! Download it below.")
    st.download_button("Download Registration Form", data=open(output_path, "rb"), file_name="Student_Registration_Form.docx")
