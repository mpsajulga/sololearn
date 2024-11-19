user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression

filtered_answers = list(filter(lambda answer: answer != "", user_answers))

# Display the cleaned list of answers
print(filtered_answers)