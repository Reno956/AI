import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # Si el recuento de minas es igual al número de celdas, todas las celdas son minas
        if len(self.cells) == self.count and self.count != 0:
            print('Mine Identified! - ', self.cells)
            return self.cells
        else:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # Si el recuento de minas es cero, todas las celdas de la sentencia son seguras
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # Si la celda está en la sentencia, se elimínela y se disminuye la cuenta en uno
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Si la celda está en la sentencia, se elimínela, pero no se disminuye la cuenta
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.movesMade = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Se marca la celda como un movimiento que se ha realizado y se marca como seguro
        self.movesMade.add(cell)
        self.mark_safe(cell)

        # Se crea conjunto para almacenar celdas indecisas para Knowledge 
        newSentenceCells = set()

        # Se recorre todas las celdas dentro de una fila y columna
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                if (i, j) == cell:
                    continue

                if (i, j) in self.safes:
                    continue

                if (i, j) in self.mines:
                    count = count - 1
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    newSentenceCells.add((i, j))

        # Se agrega la nueva sentencia a la base de conocimiento
        print(f'Move on cell: {cell} has added sentence to knowledge {newSentenceCells} = {count}' )
        self.knowledge.append(Sentence(newSentenceCells, count))

        # Se marca iterativamente las minas y las cajas fuertes garantizadas, y se infiere nuevos conocimientos
        knowledgeChanged = True

        while knowledgeChanged:
            knowledgeChanged = False

            safes = set()
            mines = set()

            # Se obtiene un conjunto de espacios seguros y minas de Knowledge
            for sentence in self.knowledge:
                safes = safes.union(sentence.known_safes())
                mines = mines.union(sentence.known_mines())

            # Se marca cualquier espacio seguro o minas
            if safes:
                knowledgeChanged = True
                for safe in safes:
                    self.mark_safe(safe)
            if mines:
                knowledgeChanged = True
                for mine in mines:
                    self.mark_mine(mine)

            # Se remueve cualquier sentencia vacia
            empty = Sentence(set(), 0)

            self.knowledge[:] = [x for x in self.knowledge if x != empty]

            # Se trata de inferir sentencias nuevas a partir de las actuales
            for sentence1 in self.knowledge:
                for sentence2 in self.knowledge:

                    if sentence1.cells == sentence2.cells:
                        continue

                    if sentence1.cells == set() and sentence1.count > 0:
                        print('Error - sentence with no cells and count created')
                        raise ValueError

                    if sentence1.cells.issubset(sentence2.cells):
                        newSentenceCells = sentence2.cells - sentence1.cells
                        newSentenceCount = sentence2.count - sentence1.count
                        newSentence = Sentence(newSentenceCells, newSentenceCount)

                        if newSentence not in self.knowledge:
                            knowledgeChanged = True
                            print('New Inferred Knowledge: ', newSentence, 'from', sentence1, ' and ', sentence2)
                            self.knowledge.append(newSentence)

        # Se imprime el conocimiento actual de AI en la terminal
        print('Current AI KB length: ', len(self.knowledge))
        print('Known Mines: ', self.mines)
        print('Safe Moves Remaining: ', self.safes - self.movesMade)
        print('====================================================')

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Se obtiene un conjunto de celdas seguras que no sean movimientos ya realizados
        safeMoves = self.safes - self.movesMade
        if safeMoves:
            print('Making a Safe Move! Safe moves available: ', len(safeMoves))
            return random.choice(list(safeMoves))

        # De lo contrario, no se pueden realizar movimientos seguros garantizados
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # Se instancia un diccionario para contener posibles movimientos y su probabilidad de mina
        moves = {}
        MINES = 8

        # Se calcula la probabilidad básica de que cualquier celda sea una mina sin Knowledge
        numMinesLeft = MINES - len(self.mines)
        spacesLeft = (self.height * self.width) - (len(self.movesMade) + len(self.mines))

        # Si no quedan espacios que sean movimientos aceptables, devuelve None
        if spacesLeft == 0:
            return None

        basicProb = numMinesLeft / spacesLeft

        # Se obtiene una lista de todos los movimientos posibles que no sean minas
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (i, j) not in self.movesMade and (i, j) not in self.mines:
                    moves[(i, j)] = basicProb

        if moves and not self.knowledge:
            move = random.choice(list(moves.keys()))
            print('AI Selecting Random Move With Basic Probability: ', move)
            return move

        elif moves:
            for sentence in self.knowledge:
                numCells = len(sentence.cells)
                count = sentence.count
                mineProb = count / numCells
                for cell in sentence.cells:
                    if moves[cell] < mineProb:
                        moves[cell] = mineProb

            moveList = [[x, moves[x]] for x in moves]
            moveList.sort(key=lambda x: x[1])
            bestProb = moveList[0][1]

            bestMoves = [x for x in moveList if x[1] == bestProb]
            move = random.choice(bestMoves)[0]
            print('AI Selecting Random Move with lowest mine probability using KB: ', move)

            return move
