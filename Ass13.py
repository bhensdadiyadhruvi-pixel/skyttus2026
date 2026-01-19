# 1.Bank Management System .
class BankAccount:
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.created = False

    def create_account(self):
        self.name = input("Enter account holder name: ")
        self.balance = int(input("Enter initial balance: "))
        self.created = True
        print("Account created successfully")

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid amount")
        elif amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print("Withdrawal successful")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


acc = BankAccount()

while True:
    print("\n--- Bank Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Balance")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if acc.created:
            print("Account already exists")
        else:
            acc.create_account()

    elif choice == 2:
        if acc.created:
            amt = int(input("Enter amount to deposit: "))
            acc.deposit(amt)
        else:
            print("Create account first")

    elif choice == 3:
        if acc.created:
            amt = int(input("Enter amount to withdraw: "))
            acc.withdraw(amt)
        else:
            print("Create account first")

    elif choice == 4:
        if acc.created:
            acc.show_balance()
        else:
            print("Create account first")

    elif choice == 5:
        print("Thank you for using Bank System")
        break

    else:
        print("Invalid choice")


# 3. Quiz Game
class QuizGame:
    def __init__(self):
        self.score = 0
        self.started = False

    def start_quiz(self):
        self.score = 0
        self.started = True
        print("Quiz Started")

    def ask_questions(self):
        questions = {
            "1. Capital of India? ": "Delhi",
            "2. 2 + 2 = ? ": "4",
            "3. National animal of India? ": "Tiger",
            "4. Python file extension? ": ".py",
            "5. Opposite of hot? ": "Cold",
            "6. 10 * 5 = ? ": "50",
            "7. Founder of Python? ": "Guido van Rossum",
            "8. Which keyword is used to define a function? ": "def",
            "9. 15 + 25 = ? ": "40",
            "10. How many days are there in a week? ": "7"
        }

        for q, ans in questions.items():
            user = input(q)
            if user.strip().lower() == ans.lower():
                print("Correct")
                self.score += 1
            else:
                print("Wrong")

    def show_score(self):
        print("Your Score:", self.score, "/ 10")


quiz = QuizGame()

while True:
    print("\n--- Quiz Menu ---")
    print("1. Start Quiz")
    print("2. Answer Questions")
    print("3. Show Score")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        quiz.start_quiz()

    elif choice == 2:
        if quiz.started:
            quiz.ask_questions()
        else:
            print("Start quiz first")

    elif choice == 3:
        if quiz.started:
            quiz.show_score()
        else:
            print("Start quiz first")

    elif choice == 4:
        print("Thank you for playing")
        break

    else:
        print("Invalid choice")


