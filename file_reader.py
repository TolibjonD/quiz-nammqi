import pandas as pd

def file_reader(filePath):
    data = pd.read_excel(filePath)
    columns = list(data.columns)
    question_numbers = list(data[columns[0]])
    questions = list(data[columns[1]])
    questions_answer_1 = list(data[columns[2]])
    questions_answer_2 = list(data[columns[3]])
    questions_answer_3 = list(data[columns[4]])
    questions_answer_4 = list(data[columns[5]])
    context = {}
    options = []

    for i in range(len(questions)):
        context[question_numbers[i]] = { questions[i]: questions_answer_1[i]}
    
    return context