# 고등학생 성적 기록부
# 열람, 입력
# 열람
# 1학년 -> 1학년 반 목록
# 1학년 3반 -> 1학년 3반 학생 목록
# 학생이름(A) -> A 국영수 성적, 평균 출력
# 입력
# 1학년 3반 A 입력
# 국영수 성적 순차 입력


# MP3 딕셔너리로

# 인스타 게시물 검색
# 태그 게시물이름 계정
# # "" @
# {계정 : {게시물이름: [태그]}}
# {태그 : {게시물이름:계정}}

accountDict = {};
tagDict = {};
main = True;
print("인스타 클론입니다.");

while main:
    print("1. 게시 2. 검색 0. 종료");
    select = input(">> ");
    if select.isdigit():
        if select == "1":
            while True:
                account = input("게시하는 계정명을 입력 (예시_@abc): ");
                if account.count(" ") > 0 or account.count("#") > 0 or account.count("@") > 1:
                    print("계정명에는 첫 @ 외의 구분자를 사용할 수 없습니다.");
                elif account.startswith("@"):
                    break;
                else:
                    print("계정명은 @로 시작해야 합니다.");
            while True:
                subject = input("게시물 제목을 입력 : ");
                if subject.count(" ") > 0 or subject.count("#") > 0 or subject.count("@") > 0:
                    print("제목에는 구분자를 사용할 수 없습니다.");
                else:
                    break;
            while True:
                tags = input("태그들을 띄어쓰기로 구분하여 입력 (예시_#a #b) : ");
                if tags.count("#") != tags.count(" ") + 1:
                    print("태그의 개수와 #의 개수는 일치해야 합니다.");
                elif tags.count("@") > 0:
                    print("태그에는 @를 사용할 수 없습니다.");
                else:
                    tagsList = tags.split();
                    for tag in tagsList:
                        if tag[0] != "#":
                            print("각 태그는 무조건 #으로 시작해야 합니다.");
                            break;
                    else:
                        break;
            tagsList = tags.split();
            if accountDict.get(account) == None:
                accountDict[account] = {};
            accountDict[account][subject] = [];
            
            for tag in tagsList:
                accountDict[account][subject].append(tag);
                if tagDict.get(tag) == None:
                    tagDict[tag] = {};
                tagDict[tag][subject] = account;
        if select == "2":
            search = None;
            while True:
                search = input("검색어의 앞에 계정명은 @, 태그는 #을 달아 검색어를 입력 : ");
                if search.startswith("@"):
                    if search.count(" ") > 0 or search.count("#") > 0 or search.count("@") > 1:
                        print("검색어 오류 : 구분자");
                    else:
                        break;
                elif search.startswith("#"):
                    if search.count("#") != search.count(" ") + 1:
                        print("태그의 개수와 #의 개수는 일치해야 합니다.");
                    else:
                        tagsList = search.split();
                        for tag in tagsList:
                            if tag[0] != "#":
                                print("각 태그는 무조건 #으로 시작해야 합니다.");
                                break;
                        else:
                            break;
                elif search.count(" ") > 0 or search.count("#") > 0 or search.count("@") > 0:
                    print("검색어 오류 : 구분자");
                else:
                    break;
                

            if search.startswith("@"):
                print(f"계정명 검색 - [{search}]");
                if accountDict.get(search) == None:
                    print("검색 결과가 없습니다.");
                else:
                    subjectDict = accountDict.get(search);
                    subjectList = list(subjectDict.keys());
                    print(f"게시물 {len(subjectDict)}건이 검색되었습니다.");
                    for subject in subjectList:
                        print(f"{search} < {subject} >", end=" ");
                        for tag in subjectDict[subject]:
                            print(tag, end = " ");
                        print();
            elif search.startswith("#"):
                accountList = [];
                subjectList = [];

                tagsList = search.split();
                searched = False;
                for tag in tagsList:
                    if tagDict.get(tag) != None:
                        tmpSubjectList = list(tagDict.get(tag).keys());
                        tmpAccountList = list(tagDict.get(tag).values());
                        searched = True;
                        for i in range(len(tmpSubjectList)):
                            if tmpSubjectList[i] in subjectList:
                                continue;
                            else:
                                subjectList.append(tmpSubjectList[i]);
                                accountList.append(tmpAccountList[i]);

                if searched:
                    print(f"게시물 {len(subjectList)}건이 검색되었습니다.");
                    for i in range(len(subjectList)):
                        subjectDict = accountDict.get(accountList[i]);
                        tags = subjectDict.get(subjectList[i]);
                        print(f"{accountList[i]} < {subjectList[i]} >", end=" ");
                        for tag in tags:
                            print(tag, end = " ");
                        print();           
                else:
                    print("검색 결과가 없습니다.");
            else:
                searched = False;
                for i in range(len(accountDict)):
                    tmpAccountList = list(accountDict.keys());
                    account = tmpAccountList[i]
                    tmpSubjectList = list(accountDict[account].keys());
                    searchList = [];
                    for subject in tmpSubjectList:
                        if subject == search:
                            searchList.append([account, subject]);
                            searched = True;
                if searched:
                    print(f"게시물 {len(searchList)}건이 검색되었습니다.");
                    for i in range(len(searchList)):
                        subjectDict = accountDict.get(searchList[i][0]);
                        tags = subjectDict.get(searchList[i][1]);
                        print(f"{searchList[i][0]} < {searchList[i][1]} >", end=" ");
                        for tag in tags:
                            print(tag, end = " ");
                        print();  
                else:
                    print("검색 결과가 없습니다.");
        if select == "0":
            print("프로그램을 종료합니다.");
            main = False;   
    else:
        print("잘못된 입력입니다.");
