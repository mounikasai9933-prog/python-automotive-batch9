def physics_result(score):
    if score > 60:
        return True   # Pass
    else:
        return False  # Fail


# Main Program
physics_score = int(input("Enter Physics score: "))

result = physics_result(physics_score)

if result:
    print("Pass")
else:
    print("Fail")