class GameOfLife:

    def game(self, filename_input: str, filename_output: str) -> None:
        with open(filename_input, 'r') as fr, open(filename_output, 'w') as fw:
            fw.write(fr.read())
