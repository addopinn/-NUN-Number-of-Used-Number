import json
with open("imsi.json","r") as f:
    data = json.load(f)
print("0~99 사이에서의 수 갯수 찾기입니다 \n =======================================")
S1,S2 = input("[범위설정]\n시작 수:").split()
Num1 = int(S1+S2)
if Num1>=0 and Num1<=99:
    E1,E2 = input("[범위설정]\n끝 수:").split()
    Num2 = int(E1+E2)
    if Num2>=Num1 and Num2<=99:
        YN = input(f"설정하신 수 범위는 {Num1}부터 {Num2}까지입니다. 설정하신 수 범위가 맞습니까? (Y or N) \n Y or N :")
        if YN == "Y":
            print(f"수 범위가 {Num1}부터 {Num2}까지로 설정되었습니다.")
            Tar = (input("찾을 수를 설정해주세요"))
            Target = int(Tar)
            if Target>=1 and Target <= 9:
                print(f"찾을 수가 {Target}으로 설정되었습니다")
                if  int(S1) > Target:
                    if int(S2) <= Target:
                        print(f"범위 내의 수 갯수는 {10 - int(S1)}개 입니다")
                        ##
                        if  int(E1) > Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {10 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(10-int(S1))}-{int(10 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {9 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(10-int(S1))}-{int(9 - int(E1))}개 입니다")
                        elif int(E1) <= Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {20 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(10-int(S1))}-{int(20 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {19 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(10-int(S1))}-{int(19 - int(E1))}개 입니다")
                        ##
                    elif int(S2) > Target:
                        print(f"범위 내의 수 갯수는 {9 - int(S1)}개 입니다")
                        ##
                        if int(E1) > Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {10 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(9-int(S1))}-{int(10 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {9 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(9-int(S1))}-{int(9 - int(E1))}개 입니다")
                        elif int(E1) <= Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {20 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(9-int(S1))}-{int(20 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {19 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(9-int(S1))}-{int(19 - int(E1))}개 입니다")
                        ##
                elif int(S1) <= Target:
                    if int(S2) <= Target:
                        print(f"범위 내의 수 갯수는 {20 - int(S1)}개 입니다")
                        ##
                        if int(E1) > Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {10 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(20-int(S1))}-{int(10 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {9 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(20-int(S1))}-{int(9 - int(E1))}개 입니다")
                        elif int(E1) <= Target:
                            if int(E2) <= Target:
                                print(f"두번째 범위 내의 수 갯수는 {20 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(20-int(S1))}-{int(20 - int(E1))}개 입니다")
                            elif int(E2) > Target:
                                print(f"두번째 범위 내의 수 갯수는 {19 - int(E1)}개 입니다")
                                print(f"총 갯수는 {int(20-int(S1))}-{int(19 - int(E1))}개 입니다")
                        ##
                    elif int(S2) > Target:
                            print(f"범위 내의 수 갯수는 {19 - int(S1)}개 입니다")
                            ##
                            if int(E1) > Target:
                                if int(E2) <= Target:
                                    print(f"두번째 범위 내의 수 갯수는 {10 - int(E1)}개 입니다")
                                    print(f"총 갯수는 {int(19-int(S1))}-{int(10 - int(E1))}개 입니다")
                                elif int(E2) > Target:
                                    print(f"두번째 범위 내의 수 갯수는 {9 - int(E1)}개 입니다")
                                    print(f"총 갯수는 {int(19-int(S1))}-{int(9 - int(E1))}개 입니다")
                            elif int(E1) <= Target:
                                if int(E2) <= Target:
                                    print(f"두번째 범위 내의 수 갯수는 {20 - int(E1)}개 입니다")
                                    print(f"총 갯수는 {int(19-int(S1))}-{int(20 - int(E1))}개 입니다")
                                elif int(E2) > Target:
                                    print(f"두번째 범위 내의 수 갯수는 {19 - int(E1)}개 입니다")
                                    print(f"총 갯수는 {int(19-int(S1))}-{int(19 - int(E1))}개 입니다")
                            ##
                    
#====================================== 아래로는 실패했을 경우  
            else:
                print("찾을 수가 잘못되었습니다. 찾을 수는 한자리 자연수여야 합니다.")          
        elif YN == "N":
            print("처음부터 다시 진행해주세요")
        else:
            print("잘못된 응답입니다.")
    else:
        print("잘못된 수를 입력하셨습니다. 처음부터 다시 입력해주세요")
else:
    print("잘못된 수를 입력하셨습니다. 처음부터 다시 입력해주세요")
####################################
