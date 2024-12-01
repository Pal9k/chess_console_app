class InputParser:
    @staticmethod
    def parse(user_input: str) -> (str, str):
        try:
            piece_type, position = user_input.split(', ')
            return piece_type, position
        except ValueError:
            raise ValueError("Invalid input format. Expected 'piece_type, position' (e.g., 'King, D5').")
