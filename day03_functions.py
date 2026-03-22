# DAY 3 — Functions, If/Else, Error Handling
# Rxsyntax AI Portfolio
# Healthcare Use Case: Clinical Decision Support

# ===== BASIC FUNCTION =====
def greet_patient(name):
    print(f"Good morning, {name}. Welcome to the clinic.")

greet_patient("Chidi Okafor")
greet_patient("Amina Bello")
greet_patient("Nick")

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

patient_bmi = calculate_bmi(84.5, 1.75)
print(f"\nPatient BMI: {patient_bmi:.2f}")

def drug_dose(drug_name, dose_mg=500):
    print(f"Prescribing {dose_mg}mg of {drug_name}")

drug_dose("Metformin")          # uses default 500mg
drug_dose("Amoxicillin", 250)   # overrides to 250mg

# ===== IF / ELSE — Clinical Decision =====

def assess_hba1c(hba1c_level):
    print(f"\nHbA1c Level: {hba1c_level}%")

    if hba1c_level < 5.7:
        print("Status: NORMAL — No diabetes risk")
    elif hba1c_level < 6.5:
        print("Status: PRE-DIABETIC — Lifestyle changes advised")
    elif hba1c_level < 8.0:
        print("Status: DIABETIC — Medication required")
    else:
        print("Status: CRITICAL — Immediate intervention needed")

assess_hba1c(5.2)
assess_hba1c(6.1)
assess_hba1c(7.8)
assess_hba1c(9.5)

def assess_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    print(f"\nBMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25.0:
        print("Category: Normal weight")
    elif bmi < 30.0:
        print("Category: Overweight")
    else:
        print("Category: Obese")

assess_bmi(84.5, 1.75)
assess_bmi(55.0, 1.70)
assess_bmi(110.0, 1.68)

# ===== ERROR HANDLING =====

def get_drug_stock(drug_inventory, drug_name):
    try:
        stock = drug_inventory[drug_name]
        print(f"{drug_name} stock: {stock} units")
    except KeyError:
        print(f"ERROR: {drug_name} not found in inventory")

# Our pharmacy inventory
inventory = {
    "Metformin": 150,
    "Lisinopril": 80,
    "Atorvastatin": 200
}

get_drug_stock(inventory, "Metformin")

get_drug_stock(inventory, "Aspirin")

def calculate_dose(weight_kg, dose_per_kg):
    try:
        total_dose = float(weight_kg) * float(dose_per_kg)
        print(f"Total dose: {total_dose}mg")
    except ValueError:
        print("ERROR: Weight and dose must be numbers")

calculate_dose(70, 5)          
calculate_dose("seventy", 5)   

# DAY 3 MINI PROJECT — Clinical Decision Support System
# Rxsyntax AI Portfolio

def assess_patient(name, age, hba1c, systolic_bp, weight_kg, height_m):
    print("\n" + "=" * 50)
    print(f"  PATIENT ASSESSMENT: {name.upper()}")
    print("=" * 50)

    # BMI Calculation
    bmi = weight_kg / (height_m ** 2)
    print(f"\nAge    : {age}")
    print(f"BMI    : {bmi:.2f}")
    print(f"HbA1c  : {hba1c}%")
    print(f"BP     : {systolic_bp} mmHg")

    # Diabetes Assessment
    print("\n--- DIABETES STATUS ---")
    if hba1c < 5.7:
        print("Diabetes Risk: NORMAL")
    elif hba1c < 6.5:
        print("Diabetes Risk: PRE-DIABETIC")
    elif hba1c < 8.0:
        print("Diabetes Risk: DIABETIC")
    else:
        print("Diabetes Risk: CRITICAL")

    # Blood Pressure Assessment
    print("\n--- BLOOD PRESSURE STATUS ---")
    if systolic_bp < 120:
        print("BP Status: NORMAL")
    elif systolic_bp < 130:
        print("BP Status: ELEVATED")
    elif systolic_bp < 140:
        print("BP Status: HIGH — Stage 1")
    else:
        print("BP Status: HIGH — Stage 2. Urgent review needed.")

    # BMI Assessment
    print("\n--- WEIGHT STATUS ---")
    if bmi < 18.5:
        print("Weight: Underweight")
    elif bmi < 25.0:
        print("Weight: Normal")
    elif bmi < 30.0:
        print("Weight: Overweight")
    else:
        print("Weight: Obese")

    print("\n" + "=" * 50)

# Run assessments on 3 patients
assess_patient("Asiegbu solomon",  age=52, hba1c=7.8, systolic_bp=145, weight_kg=94.0, height_m=1.75)
assess_patient("Onyeagba Kelvin",   age=34, hba1c=5.4, systolic_bp=118, weight_kg=62.0, height_m=1.65)
assess_patient("Gabriel Nnamdi", age=61, hba1c=9.2, systolic_bp=160, weight_kg=108.0, height_m=1.72)