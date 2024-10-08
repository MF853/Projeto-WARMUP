import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="doctor_assistance_db"
    )
    return connection

def create_patient(first_name, last_name, birth_date, gender, email, phone):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = """INSERT INTO patients (first_name, last_name, birth_date, gender, email, phone)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    val = (first_name, last_name, birth_date, gender, email, phone)
    cursor.execute(sql, val)

def get_patient(patient_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "SELECT * FROM patients WHERE patient_id = %s"
    cursor.execute(sql, (patient_id,))

    result = cursor.fetchone()
    cursor.close()
    connection.close()

    return result

def update_patient(patient_id, first_name, last_name, email, phone):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = """UPDATE patients
             SET first_name = %s, last_name = %s, email = %s, phone = %s
             WHERE patient_id = %s"""
    val = (first_name, last_name, email, phone, patient_id)
    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()

def delete_patient(patient_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "DELETE FROM patients WHERE patient_id = %s"
    cursor.execute(sql, (patient_id,))

    connection.commit()
    cursor.close()
    connection.close()

def create_diagnosis(anamnesis_id, doctor_id, diagnosis, treatment):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = """INSERT INTO diagnoses (anamnesis_id, doctor_id, diagnosis, treatment)
             VALUES (%s, %s, %s, %s)"""
    val = (anamnesis_id, doctor_id, diagnosis, treatment)
    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()

def log_consultation(patient_id, doctor_id, ai_prompt, ai_response):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = """INSERT INTO consultations (patient_id, doctor_id, ai_prompt, ai_response)
             VALUES (%s, %s, %s, %s)"""
    val = (patient_id, doctor_id, ai_prompt, ai_response)
    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()