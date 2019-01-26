import random

def hangman(word):
    #初期処理
    wrong = 0
    stages = ["                 (あと7)",
              "____________     (あと6)",
              "|         |      (あと5)",
              "|         |      (あと4)",
              "|         O      (あと3)",
              "|        /|\     (あと2)",              
              "|        / \     (あと1)",
              "|                   END",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

    #ゲーム進行
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字入力してください=>"
        char = input(msg)

        if char in rletters:
            #正解処理
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            #不正解処理
            wrong += 1

        #途中経過
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        #ゲーム終了判定
        if "_" not in board:
            print("あなたの勝ちです。")
            print(" ".join(board))
            win = True
            break

    #ゲームオーバー判定
    if not win:
        #print("\n".join(stages[0:wrong+1]))
        print("あなたの負けです\n")
        print("正解は{}でした。".format(word))

animals = [
    "dog",
    "cat",
    "fish",
    "lion",
    "bird"
    ]

number = random.randint(0, len(animals)-1)
hangman(animals[number])
