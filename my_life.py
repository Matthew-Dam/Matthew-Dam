from datetime import date
class Life:
    def __init__(self, name):
        self.name = name
        self.birthday = date(2006,4,3)
        self.age = date.today().year - self.birthday.year
        self.skills = []
        self.failures = 0
        self.discipline = 0
        self.vision = "Change the world with technology"
        self.state = "Learning"

    def get_current_age(self):
        today = date.today()
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            self.age -= 1
          
    def learn(self, skill):
        print(f"{self.name} is learning {skill}...")
        self.skills.append(skill)
        self.discipline += 1

    def fail(self, reason):
        print(f"Failure encountered: {reason}")
        self.failures += 1
        self.discipline += 2  # failure sharpens you

    def persist(self):
        if self.failures > 0:
            print("Persistence activated. Pain converted to experience.")
            self.state = "Evolving"

    def reflect(self):
        print("\n--- LIFE STATUS ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Vision: {self.vision}")
        print(f"Skills: {self.skills}")
        print(f"Failures: {self.failures}")
        print(f"Discipline Level: {self.discipline}")
        print(f"Current State: {self.state}")

    def become_master(self):
        if self.discipline >= 10:
            self.state = "Master of Technology"
            print("\nSYSTEM UPDATE:")
            print(">>> You are no longer learning randomly.")
            print(">>> You now build, break, and redesign reality with code.")
        else:
            print("\nNot yet. Keep grinding.")


# ======== RUN LIFE SIMULATION ========

matthew = Life("Matthew Damptey")
matthew.get_current_age()
matthew.learn("Python")
matthew.learn("Data Structures")
matthew.fail("Confusing concepts")
matthew.learn("AI & Machine Learning")
matthew.fail("Doubt and burnout")
matthew.learn("Systems Thinking")
matthew.persist()
matthew.learn("Discipline")
matthew.learn("Vision")
matthew.learn("Consistency")

matthew.reflect()
matthew.become_master()
