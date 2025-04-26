import time

print("""
███████╗███╗   ███╗ █████╗ ██████╗ ████████╗    ███████╗██████╗  ██████╗ 
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██╔═══██╗
█████╗  ██╔████╔██║███████║██████╔╝   ██║       █████╗  ██████╔╝██║   ██║
██╔══╝  ██║╚██╔╝██║██╔══██║██╔═══╝    ██║       ██╔══╝  ██╔═══╝ ██║   ██║
███████╗██║ ╚═╝ ██║██║  ██║██║        ██║       ███████╗██║     ╚██████╔╝
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝       ╚══════╝╚═╝      ╚═════╝ 
                    Welcome to SmartQuiz Pro! 🎉
""")

# Sections ke naam
sections = [
    "Computer Basics",
    "General Knowledge",
    "Science",
    "History",
    "Geography",
    "Sports",
    "Mathematics",
    "Literature",
    "Current Affairs",
    "Inventions & Discoveries"
]

# Har section ke 10 questions, options, answers (1-based index of correct option)
quiz_data = {
    "Computer Basics": [
        ("What does CPU stand for?", ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"], 2),
        ("Which device is used to input data?", ["Monitor", "Keyboard", "Printer", "Speaker"], 2),
        ("What is RAM?", ["Read Access Memory", "Random Access Memory", "Run Access Memory", "Readily Available Memory"], 2),
        ("Which of these is an output device?", ["Keyboard", "Mouse", "Printer", "Scanner"], 3),
        ("What does URL stand for?", ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Real Link", "Universal Real Link"], 1),
        ("Which language do computers understand?", ["English", "Binary", "French", "Java"], 2),
        ("Which of these is an operating system?", ["Google", "Windows", "Firefox", "YouTube"], 2),
        ("What is the brain of the computer?", ["CPU", "GPU", "RAM", "Hard Disk"], 1),
        ("Which of the following is a storage device?", ["Monitor", "Keyboard", "Hard Disk", "Printer"], 3),
        ("What does GUI stand for?", ["Graphical User Interface", "General Utility Interface", "Graphical Unique Interface", "General User Internet"], 1)
    ],
    "General Knowledge": [
        ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1),
        ("Who wrote 'Harry Potter'?", ["J.K. Rowling", "Dan Brown", "Tolkien", "Agatha Christie"], 1),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], 2),
        ("Which ocean is the largest?", ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
        ("Who invented the light bulb?", ["Thomas Edison", "Albert Einstein", "Isaac Newton", "Nikola Tesla"], 1),
        ("Which language is used to create Android Apps?", ["Python", "Kotlin", "Java", "HTML"], 3),
        ("What gas do plants absorb?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 2),
        ("Which country gifted the Statue of Liberty to the USA?", ["Germany", "France", "Italy", "Spain"], 2),
        ("What is H2O commonly known as?", ["Water", "Hydrogen", "Oxygen", "Salt"], 1)
    ],
    "Science": [
        ("What is the chemical symbol for water?", ["HO", "H2O", "O2", "OH"], 2),
        ("What force keeps us on the ground?", ["Magnetism", "Gravity", "Friction", "Electricity"], 2),
        ("What planet is closest to the sun?", ["Venus", "Mercury", "Earth", "Mars"], 2),
        ("Which part of the plant conducts photosynthesis?", ["Root", "Stem", "Leaf", "Flower"], 3),
        ("What gas do humans breathe in?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 1),
        ("What is the speed of light?", ["300,000 km/s", "150,000 km/s", "1,000 km/s", "30,000 km/s"], 1),
        ("Which organ pumps blood?", ["Lungs", "Brain", "Heart", "Liver"], 3),
        ("Which metal is liquid at room temperature?", ["Mercury", "Gold", "Iron", "Copper"], 1),
        ("What is the center of an atom called?", ["Electron", "Proton", "Nucleus", "Neutron"], 3),
        ("Which vitamin is produced when sunlight falls on skin?", ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"], 3)
    ],
    "History": [
        ("Who was the first President of the USA?", ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], 1),
        ("In which year did World War II end?", ["1940", "1945", "1939", "1950"], 2),
        ("Who discovered America?", ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "James Cook"], 1),
        ("The Great Wall of China was built to protect against?", ["Mongols", "Japanese", "Russians", "Indians"], 1),
        ("Who was known as the Iron Lady?", ["Indira Gandhi", "Margaret Thatcher", "Angela Merkel", "Golda Meir"], 2),
        ("The Renaissance began in which country?", ["France", "Italy", "Germany", "England"], 2),
        ("Who invented the printing press?", ["Gutenberg", "Newton", "Edison", "Tesla"], 1),
        ("Which empire was ruled by Julius Caesar?", ["Greek", "Roman", "Egyptian", "Persian"], 2),
        ("The French Revolution started in which year?", ["1789", "1776", "1800", "1812"], 1),
        ("Who was the first man to step on the moon?", ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], 3)
    ],
    "Geography": [
        ("Which is the largest continent?", ["Africa", "Asia", "Europe", "Antarctica"], 2),
        ("Which is the longest river?", ["Nile", "Amazon", "Yangtze", "Mississippi"], 1),
        ("Mount Everest is located in which country?", ["India", "Nepal", "China", "Bhutan"], 2),
        ("Which desert is the largest hot desert?", ["Gobi", "Sahara", "Kalahari", "Thar"], 2),
        ("Which country has the largest population?", ["USA", "India", "China", "Russia"], 3),
        ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], 3),
        ("Which ocean lies on the east coast of the USA?", ["Pacific", "Atlantic", "Indian", "Arctic"], 2),
        ("Which country is known as the Land of Rising Sun?", ["China", "Japan", "South Korea", "Thailand"], 2),
        ("Which is the smallest country in the world?", ["Vatican City", "Monaco", "Nauru", "San Marino"], 1),
        ("Which mountain range separates Europe and Asia?", ["Andes", "Alps", "Himalayas", "Ural"], 4)
    ],
    "Sports": [
        ("How many players are there in a football team?", ["9", "10", "11", "12"], 3),
        ("In which sport is the term ‘love’ used?", ["Cricket", "Tennis", "Football", "Basketball"], 2),
        ("Which country won the FIFA World Cup in 2018?", ["Germany", "Brazil", "France", "Argentina"], 3),
        ("How long is an Olympic swimming pool?", ["25 meters", "50 meters", "100 meters", "75 meters"], 2),
        ("Who holds the record for most Olympic gold medals?", ["Usain Bolt", "Michael Phelps", "Carl Lewis", "Mark Spitz"], 2),
        ("Which sport uses a shuttlecock?", ["Badminton", "Tennis", "Squash", "Table Tennis"], 1),
        ("How many rings are there on the Olympic flag?", ["3", "4", "5", "6"], 3),
        ("Which country hosts the Wimbledon tennis tournament?", ["USA", "France", "England", "Australia"], 3),
        ("What is the term for scoring three goals in one game in football?", ["Hat-trick", "Triple Score", "Goal Rush", "Triple Play"], 1),
        ("In which sport is the Ryder Cup played?", ["Golf", "Cricket", "Rugby", "Hockey"], 1)
    ],
    "Mathematics": [
        ("What is 7 × 8?", ["54", "56", "58", "60"], 2),
        ("What is the square root of 64?", ["6", "7", "8", "9"], 3),
        ("What is 15% of 200?", ["25", "30", "35", "40"], 2),
        ("What is the value of π (Pi) approximately?", ["3.14", "3.15", "3.13", "3.16"], 1),
        ("What is 12 + 15?", ["25", "26", "27", "28"], 3),
        ("What is 100 divided by 4?", ["20", "25", "30", "35"], 2),
        ("What is 9 squared?", ["81", "72", "90", "99"], 1),
        ("What is 0 divided by any number?", ["0", "1", "Undefined", "Infinity"], 1),
        ("Which shape has 4 equal sides and angles?", ["Rectangle", "Square", "Rhombus", "Trapezium"], 2),
        ("What is the next prime number after 7?", ["9", "11", "13", "17"], 2)
    ],
    "Literature": [
        ("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], 1),
        ("Who is the author of '1984'?", ["George Orwell", "J.K. Rowling", "Ernest Hemingway", "F. Scott Fitzgerald"], 1),
        ("Which book is about a boy wizard?", ["The Hobbit", "Harry Potter", "Percy Jackson", "Narnia"], 2),
        ("Who wrote 'The Odyssey'?", ["Homer", "Virgil", "Plato", "Socrates"], 1),
        ("What genre is 'To Kill a Mockingbird'?", ["Romance", "Historical Fiction", "Thriller", "Classic"], 4),
        ("Who is the poet of 'The Raven'?", ["Edgar Allan Poe", "Robert Frost", "Emily Dickinson", "Walt Whitman"], 1),
        ("Which novel begins with 'Call me Ishmael'?", ["Moby Dick", "Great Expectations", "The Catcher in the Rye", "Dracula"], 1),
        ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Charlotte Bronte", "Emily Bronte", "George Eliot"], 1),
        ("What is a Haiku?", ["A poem", "A story", "A play", "A song"], 1),
        ("Who wrote 'The Great Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "Mark Twain"], 1)
    ],
    "Current Affairs": [
        ("Who is the current President of the USA?", ["Joe Biden", "Donald Trump", "Barack Obama", "George Bush"], 1),
        ("Which country recently hosted the Olympics?", ["China", "Japan", "Brazil", "UK"], 2),
        ("What is the latest technology in smartphones?", ["5G", "4G", "3G", "2G"], 1),
        ("Who won the recent FIFA World Cup?", ["France", "Germany", "Brazil", "Argentina"], 4),
        ("Which country launched the Artemis moon mission?", ["USA", "Russia", "China", "India"], 1),
        ("What is the global organization for health?", ["WHO", "UNICEF", "NATO", "IMF"], 1),
        ("Which climate agreement is global?", ["Kyoto Protocol", "Paris Agreement", "Geneva Convention", "Montreal Protocol"], 2),
        ("Who is the CEO of Tesla?", ["Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg"], 1),
        ("Which country has the highest GDP?", ["USA", "China", "India", "Japan"], 1),
        ("What is cryptocurrency?", ["Digital currency", "Paper money", "Metal coins", "Plastic money"], 1)
    ],
    "Inventions & Discoveries": [
        ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"], 1),
        ("Who discovered penicillin?", ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton"], 2),
        ("When was the internet invented?", ["1960s", "1970s", "1980s", "1990s"], 2),
        ("Who invented the airplane?", ["Wright Brothers", "Orville Wright", "Wilbur Wright", "Glenn Curtiss"], 1),
        ("Which invention is used to see very small things?", ["Telescope", "Microscope", "Binoculars", "Periscope"], 2),
        ("Who discovered gravity?", ["Newton", "Einstein", "Galileo", "Tesla"], 1),
        ("What does GPS stand for?", ["Global Positioning System", "General Positioning System", "Global Place System", "General Place System"], 1),
        ("Who invented the first computer?", ["Charles Babbage", "Alan Turing", "John von Neumann", "Steve Jobs"], 1),
        ("Which invention revolutionized communication in the 19th century?", ["Telephone", "Telegraph", "Radio", "Internet"], 2),
        ("When was the first smartphone released?", ["1992", "1994", "1996", "1998"], 2)
    ]
}

def start_quiz():
    print("Welcome to the Ultimate Quiz Challenge!")
    print("You have 30 minutes to answer 100 questions from 10 sections.")
    print("Each question has 4 options. Type 1, 2, 3, or 4 to answer.")
    print("Let's begin!\n")

    start_time = time.time()
    total_time_limit = 30 * 60  # 30 minutes in seconds

    section_scores = {section: 0 for section in sections}
    total_questions = 0

    for section in sections:
        print(f"Section: {section}")
        questions = quiz_data[section]
        for i, (question, options, correct_ans) in enumerate(questions, 1):
            # Check timer before each question
            elapsed = time.time() - start_time
            if elapsed > total_time_limit:
                print("\n⏰ Time Over! The quiz has ended.")
                show_results(section_scores)
                return

            print(f"\nQ{i}: {question}")
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            while True:
                try:
                    answer = int(input("Your answer (1-4): ").strip())
                    if answer in [1,2,3,4]:
                        break
                    else:
                        print("Please enter a valid option number (1-4).")
                except:
                    print("Invalid input. Please enter number 1 to 4.")

            if answer == correct_ans:
                print("Correct! ✅")
                section_scores[section] += 1
            else:
                print(f"Wrong! ❌ Correct answer was: {correct_ans}. {options[correct_ans-1]}")

            total_questions += 1

        print(f"\nYou completed the section '{section}' with score: {section_scores[section]}/10\n")
        print("-"*40)

    print("\n🎉 You completed the quiz! Let's see your results...\n")
    show_results(section_scores)


def show_results(section_scores):
    total_score = sum(section_scores.values())
    print(f"Your Total Score: {total_score} / 100\n")

    # Find strongest and weakest section
    strongest_section = max(section_scores, key=section_scores.get)
    weakest_section = min(section_scores, key=section_scores.get)

    print(f"Strongest Section: {strongest_section} ({section_scores[strongest_section]}/10)")
    print(f"Weakest Section: {weakest_section} ({section_scores[weakest_section]}/10)")

    # Cute message
    print("\n🌟 Keep learning and growing! You're doing amazing! 🌟\n")


if __name__ == "__main__":
    start_quiz()
