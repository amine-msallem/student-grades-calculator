students = []
N = int(input("Give me the number of students: "))
def get_grade(subject):
    while True:
        try:
            grade = int(input(f"Grade in {subject}: "))
            if 0 <= grade <= 20:
                return grade
            else:
                print("Invalid grade! Please enter a value between 0 and 20.")
        except ValueError:
            print("Please enter a valid number!")
for i in range(1,N+1):
    print(f"\nStudent Number {i}")
    e ={}  
    e["Name"] =input("Student name: ") 
    e["CEM"] =get_grade("CEM")
    e["NF"] =get_grade("Network Foundations")
    e["DT"] =get_grade("Data transmissions")
    e["OS"] =get_grade("Operating system")
    e["AMM"] =get_grade("Architecture of Microprocessors and Microcontrollers")
    e["ASP"] =get_grade("Analog signal processing")
    e["som"]=round((e["CEM"]+e["NF"]+e["DT"]+e["OS"]+e["AMM"]+e["ASP"])/6,2)
    students.append(e)
print("\nAll students' grades:")
maxi=students[0]["som"]
b =students[0]["Name"]
mini =students[0]["som"]
w =students[0]["Name"]
for s in students:
    if s["som"]>maxi:
        maxi =s["som"]
        b =s["Name"]
    if s["som"]<mini:
        mini = s["som"]
        w =s["Name"]
    print(f"{s['Name']}: CEM={s['CEM']}, NF={s['NF']}, DT={s['DT']}, OS={s['OS']}, AMM={s['AMM']}, ASP={s['ASP']} Moy={s['som']}")
print("\nBest student:", b, "with average", maxi)
print("Worst student:", w, "with average", mini)