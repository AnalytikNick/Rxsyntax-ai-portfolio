# Day 2 - Lists and Loops
# RxSyntax AI Portfolio
# Healthcare use case: Managing patient data and medication lists


# ======== CREATING A LIST=========

ward_medications = ["Aspirin", "Metformin", "Lisinopril", "Atorvastatin"]
print("Ward Medications:", ward_medications)

#======= ACCESSING MEDICATIONS =======
print("First medication:", ward_medications[0])
print("Second medication:", ward_medications[1])
print("Last medication:", ward_medications[-1])

#======= MODIFYING THE MEDICATION LIST =======
ward_medications.append("Albuterol")
ward_medications.append("Levothyroxine")
print("Updated Ward Medications:", ward_medications)

ward_medications.remove("Metformin")
print("After removing metformin", ward_medications)

# ======= Checking if a medication is in the list =======
print("\nis Aspirin in  ward medications?", "Aspirin" in ward_medications)
print("is Levothyroxine in ward medications?", "Levothyroxine" in ward_medications)

# ======= Counting Total Drugs in the List =======
print("Total medications in the ward:", len(ward_medications))

# ===== FOR LOOP — visit every medication =====
for medication in ward_medications:
    print("Medication:", medication)

print("\nAll medications have been listed.")
for index, medication in enumerate(ward_medications, start=1):
    print(f"{index}. {medication}")

# Flag medications that start with certain letters
print("\n========== MEDICATIONS STARTING WITH 'A' ==========")
for medication in ward_medications:
    if medication.startswith("A"):
        print(medication)

# ===== DICTIONARY — Patient Record =====
Patient = {
    "name": "Solace",
    "age": 45,
    "condition": "Hypertension",
    "medications": ["Lisinopril", "Amlodipine"],
    "diagnosis": "High Blood Pressure",
    "ward": "Cardiology",
    "is_critical": False,
    "blood_pressure": "140/90 mmHg",
    "heart_rate": 80
}

print("\nPatient name:", Patient["name"])
print("Patient age:", Patient["age"])
print("Patient condition:", Patient["condition"])
print("Patient medications:", Patient["medications"])
print("Patient diagnosis:", Patient["diagnosis"])
print("Patient ward:", Patient["ward"])
print("Patient is critical:", Patient["is_critical"])
print("Patient blood pressure:", Patient["blood_pressure"])
print("Patient heart rate:", Patient["heart_rate"])

Patient["heart_rate"] = 85
print("updated patient heart rate:", Patient["heart_rate"])

Patient["allergies"] = ["Penicillin", "Sulfa Drugs"]
print("Patient allergies:", Patient["allergies"])

print("\n======== ALL Patient Information ========")
for key, value in Patient.items():
    print(f'{key}: {value}')


# DAY 2 MINI PROJECT — Drug Inventory Checker
# Rxsyntax AI Portfolio

drug_inventory = [
    {"name": "Lercanidipine", "stock": 200,"Low_stock_threshold": 50},
    {"name": "Amlodipine", "stock": 300,"Low_stock_threshold": 100},
    {"name": "Lisinopril", "stock": 250,"Low_stock_threshold": 75},
    {"name": "Atorvastatin", "stock": 150,"Low_stock_threshold": 30},
    {"name": "Metformin", "stock": 400,"Low_stock_threshold": 100},
    {"name": "Albuterol", "stock": 100,"Low_stock_threshold": 20},
    {"name": "Levothyroxine", "stock": 350,"Low_stock_threshold": 80}
]

print("=" * 40)
print("DRUG INVENTORY CHECKER")
print("=" * 40)

for drug in drug_inventory:
    print(f"\nDrug name: {drug['name']}")
    print(f"Stock: {drug['stock']} units")
    
print("\n" + "=" * 45)
print("     ⚠️  LOW STOCK ALERTS")
print("=" * 45)

for drug in drug_inventory:
    if drug["stock"] < drug["Low_stock_threshold"]:
        print(f"REORDER: {drug['name']} — only {drug['stock']} units left!")

total = sum(drug["stock"] for drug in drug_inventory)
print(f"\nTotal units in pharmacy: {total}")