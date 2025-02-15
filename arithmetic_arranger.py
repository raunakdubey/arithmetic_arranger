def arithmetic_arranger(problems, show_answers=False):
    # 1. Check the length of the parameter
    if len(problems) > 5:
        return "Error: Too many problems."

    # 2. Check the operand
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])

    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    # 3. Check for non-digits
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])

    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."

    # 4. Check operand length        
    for number in numbers:
        if len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

    # 5. Evaluation
    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = '' 
    dashes = ''

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        answers.append(result)

        # 6. Formatting problem rows
        space_width = max(len(str(num1)), len(str(num2))) + 2
        top_row += str(num1).rjust(space_width)
        bottom_row += operator + str(num2).rjust(space_width - 1)
        dashes += '-' * space_width

        # 7. Spacing between problems (ensure proper spacing between problems)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4

    # 8. Formatting Answers row
    for i in range(len(answers)):
        space_width = max(len(str(numbers[2 * i])), len(str(numbers[2 * i + 1]))) + 2
        answer_row += str(answers[i]).rjust(space_width)

        # 9. Spacing between answers (ensure spacing between answers)
        if i != len(answers) - 1:
            answer_row += ' ' * 4

    # 10. Final arrangement and return
    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems

# Testing the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
