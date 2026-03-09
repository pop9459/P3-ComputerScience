from challenge import Challenge
from fileExtensionsChallenge import FileExtensionsChallenge
from mathInterpreterChallenge import mathInterpreterChallenge
from nutritionFactsChallenge import NutritionFactsChallenge
from camelCaseDecoderChallenge import CamelCaseDecoderChallenge
from emojizeChallenge import EmojizeChallenge
from guessingGameChallenge import GuessingGameChallenge

class SurvivalSimulator:
    challenges = []
    
    def __init__(self):
        # Initialize the game and add challenges
        self.challenges.append(FileExtensionsChallenge())
        self.challenges.append(mathInterpreterChallenge())
        self.challenges.append(NutritionFactsChallenge())
        self.challenges.append(CamelCaseDecoderChallenge())
        self.challenges.append(EmojizeChallenge())
        self.challenges.append(GuessingGameChallenge())

    def exitGame(self):
        print("Thanks for playing! See you next time.")
        exit()

    def menu(self, show_welcome_message=False):
        if(show_welcome_message):
            print("Welcome to the Survival Simulator!")
            print("You are in an abandoned supermarket and must solve puzzles to escape!")

        num_challenges = len(self.challenges)

        # Display the menu options
        print("\nChoose an option:")        
        for index, challenge in enumerate(self.challenges):
            print(f"{index + 1}. {challenge.menuName}")
        print(num_challenges + 1, ". Exit")

        user_input = input(f"Make a choice (1-{num_challenges + 1}): ")

        match user_input:
            case "1":
                self.challenges[0].playChallenge()
            case str(num_challenges):
                self.exitGame()
            case _:
                print("Invalid choice. Please try again.")