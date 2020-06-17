import run
import train

if __name__ == "__main__":
    inp = 1
    while inp:
        inp = int(input("학습은 1번, 배추값 조회는 2번, 종료는 0번 > "))
        if inp == 1:
            train.training_data("data/price_data.csv")
        if inp == 2:
            run.run("data/saved.cpkt")