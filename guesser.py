class Guesser:
    
    def __init__(self):
        self.guesses = []
        
    def get_input(self, msg, input_func=input):
        user_input = input_func(msg)
        return user_input
    
    def validate_input(self, user_input):
        return int(user_input)

    def is_game_over(self):
        if len(self.guesses) >= 3:
            return True
        return False
    
    def add_to_guesses(self, validated_input):
        self.guesses.append(validated_input)
        return self.guesses
    
    def display_msg(self, msg, display_func=print):
        return display_func(msg)
            
    def run(self):
        inp = self.get_input("Enter a number: ")
        validated = self.validate_input(inp)
        if validated:
            self.add_to_guesses(validated)
        if self.is_game_over():
            self.display_msg("Game is over")
        else:
            self.run()
            
            
if __name__ == "__main__":
    g = Guesser()
    g.run()