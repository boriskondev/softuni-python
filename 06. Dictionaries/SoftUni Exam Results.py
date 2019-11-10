exams_and_results = {}
language_submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    name = command[0]
    if command[1] == "banned":
        del exams_and_results[name]
    else:
        language = command[1]
        result = int(command[2])
        if name not in exams_and_results:
            exams_and_results[name] = result
        else:
            if exams_and_results[name] < result:
                exams_and_results[name] = result

        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1

print("Results:")
for user, value in sorted(exams_and_results.items(), key=lambda x: (-x[1], x[0])):
    print(f"{user} | {value}")

print("Submissions:")
for language, value in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {value}")