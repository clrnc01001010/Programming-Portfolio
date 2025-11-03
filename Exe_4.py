cap = input('What is the Capital Of France: ')
if cap.lower() == 'paris':
    print('Correct')
else:
    print('Incorrect, Capital Of France is Paris')

questions = {
    "Albania":"Tirana",
    "Finland":"Helsinki",
    "Ireland":"Dublin",
    "Italy":"Rome",
    "Greece":"Athens",
    "Germany":"Berlin",
    "Monaco":"Monaco",
    "Poland":"Warsaw",
    "Spain":"Madrid",
    "Sweden":"Stockholm"
}

score = 0
print("Country Quiz")
for country, capital in questions.items():
    answer = input("What is the capital of " + country + "?")
    if answer.strip().lower() == capital.lower():
        score += 1
        print("Correct")
    else:
        print("Incorrect, Capital of " + country + " is " + capital)
print("Total score:", score, "out of", len(questions))
 