import sys
if len(sys.argv) != 5:
    print("Usage: python student.py <name> <marks> <attendance> <rating>")
    sys.exit()

name = sys.argv[1]
marks = int(sys.argv[2])
attendance = int(sys.argv[3])
rating = float(sys.argv[4])

if marks >= 75:
    grade = "Distinction"
elif marks >= 50:
    grade = "Pass"
else:
    grade = "Fail"

att_status = "Good" if attendance >= 75 else "Poor"

if rating >= 4.5:
    remark = "Excellent"
elif rating >= 3:
    remark = "Good"
else:
    remark = "Needs Improvement"


print("\n--- Student Report ---")
print(f"Name       : {name}")
print(f"Marks      : {marks} ({grade})")
print(f"Attendance : {attendance}% ({att_status})")
print(f"Rating     : {rating} ({remark})")