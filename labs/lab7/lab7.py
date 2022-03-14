
def weighted_average(in_file_name, out_file_name):
    input_file = open(in_file_name, 'r')
    grade_list = input_file.readlines()
    output_text = ""
    overall_average = 0
    class_size = 0
    for student in grade_list:
        current_line = student.split(': ')
        student_name = current_line[0]
        output_text = output_text + student_name + "'s average: "
        student_numbers = current_line[1]
        number_list = student_numbers.split(' ')
        sum_weight = 0
        sum_grade = 0

        for j in range(len(number_list)):
            if j % 2 == 0:
                weight = eval(number_list[j])
                sum_weight = sum_weight + weight
            else:
                grade = eval(number_list[j])
                weighted_grade = grade * (weight/100)
                sum_grade = sum_grade + weighted_grade

        if sum_weight > 100:
            output_text = output_text + "Error: The weights are more than 100.\n"
        if sum_weight < 100:
            output_text = output_text + "Error: The weights are less than 100.\n"
        if sum_weight == 100:
            average_text_store = "{:.1f}"
            average_text = average_text_store.format(sum_grade)
            output_text = output_text + average_text + "\n"
            overall_average = overall_average + sum_grade
            class_size = class_size + 1

    final_class_average = overall_average/class_size
    average_text_store = "Class average: {:.1f}"
    class_average_text = average_text_store.format(final_class_average)
    output_text = output_text + class_average_text
    final_output = open(out_file_name, 'w')
    print(output_text, file=final_output)

if __name__ == "__main__":
    weighted_average('grades.txt', 'avg.txt')
