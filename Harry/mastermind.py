from logic import *

color = ["Red", "Blue", "Yellow", "Green"]
position = ["0", "1", "2", "3"]

symbols = []

knowledge = And()

for col in color:
    for pos in position:
        symbols.append(Symbol(f"{col}{pos}"))

# Each person belongs to a house.
for col in color:
    knowledge.add(Or(
        Symbol(f"{col}0"),
        Symbol(f"{col}1"),
        Symbol(f"{col}2"),
        Symbol(f"{col}3")
    ))

# Only one house per person.
for col in color:
    for h1 in position:
        for h2 in position:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{col}{h1}"), Not(Symbol(f"{col}{h2}")))
                )

# Only one person per house.
for pos in position:
    for p1 in color:
        for p2 in color:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{pos}"), Not(Symbol(f"{p2}{pos}")))
                )
#print(knowledge.formula())

knowledge.add(
    Symbol("Red0")
)
knowledge.add(
    Symbol("Blue1")
)

# =============================================================================
for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
# =============================================================================
