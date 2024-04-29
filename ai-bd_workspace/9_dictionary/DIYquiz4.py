# 은행 계좌 프로그램
# 요구사항 분석 : 입금,출금,대출,계좌이체,적금,공과금,계좌생성,계좌해지


# # 인스타 게시물 검색
# 태그 게시물이름 계정
# # "" @
# {계정 : {게시물내용: [태그]}}
# {태그 : {게시물내용:계정}}

userDict = {"admin" : "1234"};
accountDict = {};
tagDict = {};
feedList = [];
isLogin = "";
print("인스타 클론입니다.");

while True:
    mainSelect = input("1. 로그인 2. 비밀번호 찾기 3. 회원가입 >> ");
    if mainSelect.isdigit():
        if 0 < int(mainSelect) < 4:
            if mainSelect == "1":
                print("로그인을 진행합니다.");
                id = input("계정명을 입력 : ");
                pw = input("비밀번호를 입력 : ");
                if id in list(userDict.keys()):
                    if pw == userDict.get(id):
                        print(f"환영합니다, < @{id} >");
                        isLogin = "@" + id;
                    else:
                        print("로그인에 실패하였습니다.");
                else:
                    print("로그인에 실패하였습니다.");
            elif mainSelect == "2":
                print("비밀번호 찾기를 진행합니다.");
                id = input("계정명을 입력 : ");
                if id in list(userDict.keys()):
                    print(f"비밀번호는 {userDict.get(id)}입니다.");
                else:
                    print(f"< {id} > 는 존재하지 않는 계정명입니다.");
            elif mainSelect == "3":
                print("회원가입을 진행합니다.");
                id = input("계정명을 입력 : ");
                pw = input("비밀번호를 입력 : ");
                if id in list(userDict.keys()):
                    print(f"< {id} > 는 이미 존재하는 계정명입니다.");
                else:
                    if len(id) > 3 and not id.isspace():
                        if len(pw) > 3 and not pw.isspace():
                            print("회원가입에 성공하였습니다.");
                            userDict[id] = pw;           
                        else:
                            print("사용 불가능한 비밀번호입니다. (4자이상, 공백 불가)");
                    else:
                        print("가입이 불가능한 계정명입니다. (4자이상, 공백 불가)");
                     
        else:
            print("잘못된 입력입니다.");
    else:
        print("잘못된 입력입니다.");

    while isLogin != "":
        print("="*30);
        print("1. 게시 2. 검색 3. 피드 #. 로그아웃 0. 계정삭제");
        select = input(">> ");
        if select.isdigit():
            if select == "1":
                account = isLogin;

                content = input("게시물 내용을 입력 : ");
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
                if accountDict.get(account) == None:
                    accountDict[account] = {};
                accountDict[account][content] = tags;
                feedList.append([account, len(accountDict.get(account))-1]);
                tagsList = tags.split();
                for tag in tagsList:
                    if tagDict.get(tag) == None:
                        tagDict[tag] = {};
                    tagDict[tag][content] = account;
            elif select == "2":
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
                    accountList = list(accountDict.keys());
                    tmpSearch = search.strip("@");
                    getAccount = [];
                    for account in accountList:
                        if tmpSearch in account:
                            getAccount.append(account);
                    if len(getAccount) == 0:
                        print("검색 결과가 없습니다.");
                    else:
                        print(f"계정 {len(getAccount)}건이 검색되었습니다.");
                        for account in getAccount:
                            print(f"{account} 계정 내 게시물 : ");
                            contentDict = accountDict.get(account);
                            for content, tags in contentDict.items():
                                print(f"{account} < {content} > {tags}");

                elif search.startswith("#"):
                    accountList = [];
                    contentList = [];

                    tagsList = search.split();
                    searched = False;
                    for tag in tagsList:
                        if tagDict.get(tag) != None:
                            tmpContentList = list(tagDict.get(tag).keys());
                            tmpAccountList = list(tagDict.get(tag).values());
                            searched = True;
                            for i in range(len(tmpContentList)):
                                if tmpContentList[i] in contentList:
                                    continue;
                                else:
                                    contentList.append(tmpContentList[i]);
                                    accountList.append(tmpAccountList[i]);

                    if searched:
                        print(f"게시물 {len(contentList)}건이 검색되었습니다.");
                        for i in range(len(contentList)):
                            contentDict = accountDict.get(accountList[i]);
                            tags = contentDict.get(contentList[i]);
                            print(f"{accountList[i]} < {contentList[i]} > {tags}"); 
                    else:
                        print("검색 결과가 없습니다.");
                else:
                    searched = False;
                    searchList = [];
                    for i in range(len(accountDict)):
                        tmpAccountList = list(accountDict.keys());
                        account = tmpAccountList[i];
                        tmpContentList = list(accountDict[account].keys());
                        for content in tmpContentList:
                            if search in content:
                                searchList.append([account, content]);
                                searched = True;
                    if searched:
                        print(f"게시물 {len(searchList)}건이 검색되었습니다.");
                        for i in range(len(searchList)):
                            contentDict = accountDict.get(searchList[i][0]);
                            tags = contentDict.get(searchList[i][1]);
                            print(f"{searchList[i][0]} < {searchList[i][1]} > {tags}");
                    else:
                        print("검색 결과가 없습니다.");
            elif select == "3":
                print("피드 목록");
                for feed in feedList:
                    print("-"*30);
                    contentDict = accountDict.get(feed[0])
                    contentList = list(contentDict.keys());
                    print(f"{feed[0]} < {contentList[feed[1]]} > {contentDict.get(contentList[feed[1]])}");
            
            elif select == "0":
                signDelete = input(f"정말로 < {isLogin} > 계정을 삭제하시겠습니까? (y)");
                if signDelete == "y" or signDelete == "Y":
                    i = 0;
                    while i < len(feedList):
                        if feedList[i][0] == isLogin:
                            feedList.pop(i);
                        else: 
                            i += 1;
                    
                    i = 0;
                    for tag in tagDict:
                        contentDict = tagDict.get(tag);
                        while i < len(list(contentDict.keys())):
                            contentList = list(contentDict.keys());
                            if contentDict.get(contentList[i]) == isLogin:
                                contentDict.pop(contentList[i]);
                            else:
                                i += 1;
                    if isLogin in accountDict:
                        accountDict.pop(isLogin);
                    userDict.pop(isLogin.lstrip("@"));
                    print("계정 삭제가 완료되었습니다.");
                    print("로그인 화면으로 나갑니다");
                    isLogin = "";
                else:
                    print("계정삭제가 취소되었습니다.");
            else:
                print("잘못된 입력입니다.");
        elif select == "#":
            print("로그아웃합니다.");
            isLogin = "";   
        else:
            print("잘못된 입력입니다.");
