# Pyrdle

It's just Wordle, but as a Python module that runs on the command line. I wrote this as a quick reference template so I can implement a similar program while learning Golang. 

### Usage
```python
from wordle import Wordle

my_wordle_game = Wordle()
my_wordle_game.play()
```

### Example gameplay
```sh
Enter guess: cough
C  O  U  G  H
⬜ ⬜ 🟨 🟨 ⬜

Q W E R T Y U I   P
 A S D F G   J K L
  Z X   V B N M

Enter guess: tread
C  O  U  G  H
⬜ ⬜ 🟨 🟨 ⬜
T  R  E  A  D
⬜ ⬜ ⬜ ⬜ 🟩

Q W       Y U I   P
   S D F G   J K L
  Z X   V B N M

Enter guess: vinyl
C  O  U  G  H
⬜ ⬜ 🟨 🟨 ⬜
T  R  E  A  D
⬜ ⬜ ⬜ ⬜ 🟩
V  I  N  Y  L
⬜ 🟨 ⬜ ⬜ 🟨

Q W         U I   P
   S D F G   J K L
  Z X     B   M

Enter guess: guild
C  O  U  G  H
⬜ ⬜ 🟨 🟨 ⬜
T  R  E  A  D
⬜ ⬜ ⬜ ⬜ 🟩
V  I  N  Y  L
⬜ 🟨 ⬜ ⬜ 🟨
G  U  I  L  D
🟩 🟩 🟩 🟩 🟩

Winner!
```
