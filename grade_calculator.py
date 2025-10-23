def calculate_average(score1, score2, score3):
    return (score1 + score2 +score3) / 3
def drop_lowest(score1, score2, score3):
    minimum = min(score1, score2, score3)
    return (score1 +score2 + score3 - minimum)/2
def calculate_weighted(assignments, midterm, final):
    return (assignments * 0.30) + (midterm  * 0.30) + (final * 0.40)
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def needs_improvement(current_avg, target_grade):
    if   target_grade == "A":
        return current_avg < 90
    elif target_grade == 'B':
        return current_avg < 80
    elif  target_grade == 'C':
        return current_avg < 70
    elif  target_grade == 'D':
        return current_avg < 60
    else:
        return False
score1, score2, score3 = 85, 78, 92
midterm = 88
final = 82

print("STUDENT GRADE CALCULATOR\n")
print("=" * 35 )
regular_avg = calculate_average(score1, score2, score3)
drop_avg = drop_lowest(score1, score2, score3)
better_avg = max(regular_avg,drop_avg)
weighted_avg = calculate_weighted(better_avg, midterm, final)
letter_grade = determine_grade(weighted_avg)
need_improvement = needs_improvement(weighted_avg,"A")

print(f"Assignment Scores: {score1}, {score2}, {score3}")
print("Midterm Score: {midterm}")
print("Final Score: {final}\n ")
print("-" * 35)
print(f"Regular Assignment Average: {regular_avg:.2f} ")
print(f"Average with Lowest Dropped: {drop_avg:.2f}")
print(f"Using Better Average: {better_avg:.2f} ")
print(" " * 35)
print(f"Weighted Course Average: {weighted_avg:.2f}")
print(f"Letter Grade: {letter_grade}")

if need_improvement:
    print(f"Needs improvement for an 'A': Yes")
    points_needed = 90 - weighted_avg
    print(f"Points needed: {points_needed:.2f}")
else:
    print(f"Needs improvement for an 'A': No")
print(f"Already meets or exceeds {letter_grade} grade requirement")

