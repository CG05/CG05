# MP3 플레이어
import os;

musicDict = {1:["바람기억","나얼"], 2:["혜성","윤하"], 3:["Drama","aespa"], 4:["돌덩이","하현우"]};
lastMusicNum = 4;
playLsDict = {"전체":[1,2,3,4],"락":[2,4]};
prtStr = "";
curIndex = 0;
curLs = "전체";
select = 0;
selected = False;
playing = False;
main = True;

while main:
    curPlList = playLsDict.get(curLs);
    curMusic = curPlList[curIndex];
    os.system("cls");    
    print("#"*73);
    prtStr = "MP3 Player";
    print(f"{prtStr:^70}");
    if playing == True:
        prtStr = "▶";
        print(f"{prtStr:^70}");
    else :
        prtStr = "⏸";
        print(f"{prtStr:^70}");
    if len(curPlList) == 0:
        prtStr = f"~[ {curLs} ]재생중~ : -재생 가능한 음악이 없습니다-";
    else:
        
        prtStr = f"~[ {curLs} ]재생중~ : {musicDict.get(curMusic)[0]} - {musicDict.get(curMusic)[1]}";
    print(f"\t\t{prtStr}\t\t");
    print("#"*73);

    if selected == False:
        select = input("1. 음악 목록 2. 시작/정지 3. 다음곡 4. 이전곡 5. 곡 추가 0. 종료\n>> ");
        if select.isdigit() == False:
            print("숫자 키로 입력해주십시오.");
            continue;
        elif int(select) < 0 or int(select) > 5 :
            print("메뉴 중에서 선택해주십시오.");
            continue;
        else:
            selected == True;
    if select == "1":
        for i, k in enumerate(playLsDict):
            print(f"{i + 1}.{k}");
        selectLs = 0;
        while True:
            selectLs = input("목록을 선택해주십시오. #:목록 추가 0:메인나가기 \n>>");
            if selectLs.isdigit():
                selectLs = int(selectLs);
                if 0 <= selectLs <= len(playLsDict):
                    break;
                else:
                    print("없는 번호입니다.");
            elif selectLs == "#":
                break;
            else:
                print("잘못된 입력입니다.");
        if selectLs == "#":
            newLs = input("추가할 목록 이름을 입력해주십시오 : ");
            playLsDict[newLs] = [];
            print(f"새로운 목록 [{newLs}]이 추가되었습니다.");
            continue;
        elif selectLs > 0:
            plNameList = list(playLsDict.keys());
            plName = plNameList[selectLs - 1];
            playLs = playLsDict.get(plName);
            print(f"> [ {plName} ] 플레이리스트 <");
            selectMusic = 0;
            while True:
                for i, k in enumerate(playLs):
                    print(f"{i + 1} : {musicDict.get(k)[0]} - {musicDict.get(k)[1]}");
                print("---------------------------------------------");
                selectMusic = input("선택하려면 해당 음악의 번호를 입력해주십시오. 0:메인나가기]\n>>");
                if selectMusic.isdigit():
                    selectMusic = int(selectMusic);
                    if 0 <= selectMusic <= len(playLs):
                        break;
                    else:
                        print("없는 번호입니다.");
                else:
                    print("잘못된 입력입니다."); 
            if selectMusic > 0:
                music = musicDict.get(playLs[selectMusic-1]);
                s = 0;
                while True:
                    s = input("1:재생 2:삭제 3: 다른 목록에 추가 0:메인나가기\n>>");
                    if s.isdigit():
                        s = int(s);
                        if 0 <= s <= 3:
                            break;
                        else:
                            print("없는 번호입니다.");
                    else:
                        print("잘못된 입력입니다.");
                if s == 1:
                    curIndex = selectMusic-1;
                    curLs = plName;
                    playing = True;
                    continue;
                elif s == 2:
                    if curMusic == playLs[selectMusic - 1]:
                        if curIndex + 1 >= len(curPlList)-1:
                            curIndex = 0;
                        else:
                            curIndex += 1;
                        playing = False;
                    print(f"[ {plName} ] 에서 다음 음악이 삭제되었습니다 : {music[0]} - {music[1]}");
                    delMusic = playLs[selectMusic-1];
                    playLsDict[plName].remove(delMusic);
                    if plName == "전체":
                        musicDict.pop(delMusic);
                        for lsName in playLsDict:
                            if delMusic in playLsDict[lsName]:
                                playLsDict[lsName].remove(delMusic);
                elif s == 3:
                    for i, k in enumerate(playLsDict):
                        if i == 0 or i == selectLs-1:
                            continue;
                        print(f"{i + 1}.{k}");
                    toMoveLs = -1;
                    while True:
                        toMoveLs = input("추가할 곳을 선택해주십시오. 0:메인나가기\n>>");
                        if toMoveLs.isdigit():
                            toMoveLs = int(toMoveLs);
                            if 0 <= toMoveLs <= len(playLsDict) and toMoveLs-1 != selectLs-1:
                                break;
                            else:
                                print("없는 번호입니다.");
                        else:
                            print("잘못된 입력입니다.");
                    if toMoveLs > 0:
                        toMovePlName = plNameList[toMoveLs-1];
                        toMoveMusic = playLs[selectMusic-1];
                        if playLsDict.get(toMovePlName).count(toMoveMusic) > 0:
                            print("이미 존재하는 음악입니다. 실행이 취소됩니다.");
                        else:
                            playLsDict[toMovePlName].append(toMoveMusic);
                            print(f"[ {toMovePlName} ] 에 다음 음악이 추가되었습니다 : {music[0]} - {music[1]}");
                        
                        os.system("pause");
                        selected = False;

                    else:
                        
                        os.system("pause");
                        selected = False;

                else:
                    
                    os.system("pause");
                    selected = False;

            else:
                
                os.system("pause");
                selected = False;
        else:
            
            os.system("pause");
            selected = False;
                
            
        # 
        # os.system("pause");
        
        # selected = False;
        # continue;
    elif select == "2":
        if playing:
            print("음악을 일시정지합니다.");
            playing = False;
        else:
            if len(curPlList) == 0:
                print("현재 플레이리스트에 재생 가능한 음악이 없습니다. 음악을 추가해주십시오.");
            else:
                print("현재 플레이리스트를 재생합니다.");
                playing = True;
        
        selected = False;
        continue;
    elif select == "3":
        if len(curPlList) == 0:
            print("현재 플레이리스트에 재생 가능한 음악이 없습니다. 음악을 추가해주십시오.");
            
        else:
            print("현재 플레이리스트의 다음 곡을 재생합니다.");
            if curIndex + 1 == len(curPlList):
                curIndex = 0;
            else:
                curIndex += 1;
            playing = True;
        
        selected = False;
        continue;
    elif select == "4":
        if len(musicDict) == 0:
            print("현재 플레이리스트에 재생 가능한 음악이 없습니다. 음악을 추가해주십시오.");
            
        else:
            print("현재 플레이리스트의 이전 곡을 재생합니다.");
            if curIndex - 1 < 0:
                curIndex = len(curPlList) - 1;
            else:
                curIndex -= 1;
            playing = True;
        
        selected = False;
        continue;
    elif select == "5":
        addSub = input("추가할 음악의 제목을 입력해주십시오 : ");
        addArtist = input("추가할 음악의 가수을 입력해주십시오 : ");
        add = [addSub, addArtist];
        musicList = list(musicDict.values());
        if musicList.count(add) > 0:
            print("해당 음악은 이미 추가돼있습니다");
        else:
            print(f"다음 음악이 추가되었습니다 : {add[0]} - {add[1]}");
            lastMusicNum += 1;
            musicDict[lastMusicNum] = add;
            playLsDict["전체"].append(lastMusicNum);
        
        os.system("pause");
        selected = False;
        continue;
    elif select == "0":
        print("MP3를 종료합니다.");
        main = False; 
    else:
        print("select예외오류");
