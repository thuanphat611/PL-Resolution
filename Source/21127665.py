#Hàm phụ----------------------------------------------------------------
#hàm loại bỏ phần tử trùng lặp
def removeDuplicates(source):
    result = []
    for i in source:
        if i not in result:
            result.append(i)
    return result

#hàm lấy dữ liệu từ file
def readFile(name):
    global size, start, end
    f = open(name, 'r')

    alphaSize = int(f.readline())
    alpha = []
    for i in range(alphaSize):
        alpha.append(f.readline().strip())
    
    KBSize = int(f.readline())
    KB = []
    for j in range(KBSize):
        KB.append(f.readline().strip())

    return removeDuplicates(alpha), removeDuplicates(KB)#xoá phần tử lặp khi trả về 

#hàm trả về dạng phủ định của alpha
def negation(alpha):
    if not alpha: return []

    result = []

    if alpha[0][0] == '-':
        result.append(alpha[0][-1])
    else:
        result.append('-' + alpha[0])
        
    return result

#hàm loại bỏ tất cả phần tử của mảng nếu có 1 literal và phủ định của nó trong mảng 
#VD: ['-A', 'A', 'B', 'C'] => []
def removeAlwaysTrue(arr):
    for i in range(len(arr) - 1):
        if arr[i][0] == '-':
            nega = arr[i][1]
        else:
            nega = '-' + arr[i]
        for j in range(i + 1, len(arr)):
            if nega == arr[j]:
                return []
    return arr
    
#hàm kiểm tra xem list a có nằm trong list b khác hay không    
def isChildOf(sc, sp):
    size = len(sc)
    count = 0

    for c in sc:
        if c in sp:
            count += 1

    if count == size:
        return True
    else:
        return False
    
#hàm kiểm tra xem mệnh đề có chưa nằm trong tập mệnh đề hay không
def notIn(clause, clausesList):
    clauseLiterals = clause.split(' OR ')
    #lấy mỗi mệnh đề trong tập ra để so sánh
    for i in clausesList:
        iLiterals = i.split(' OR ')
        numDuplicates = 0

        for c in clauseLiterals:
            if c in iLiterals:
                numDuplicates += 1

        # nếu số literal 2 bên bằng nhau và 
        # số literal trùng nhau của 2 bên bằng số literal mỗi bên có thì tức là
        # 2 mệnh đề đang so sánh trùng nhau 
        if len(iLiterals) == len(clauseLiterals) and numDuplicates == len(clauseLiterals):
            return False

    return True

#hàm thuật toán----------------------------------------------------------------
def PL_resolve(a, b):
    a_literals = a.split(' OR ')
    b_literals = b.split(' OR ')
    result = []

    for al in a_literals:
        if al[0] == '-':
            nega_al = al[1]
        else:
            nega_al = '-' + al
        if nega_al in b_literals:
            newClause = []
            for a in a_literals:
                if a != al:
                    newClause.append(a)
            for b in b_literals:
                if b != nega_al:
                    newClause.append(b)
            
            if len(newClause) == 0:
                return ['{}']

            newClause = removeDuplicates(newClause)
            newClause = removeAlwaysTrue(newClause)
            newClause = sorted(list(set(newClause)), key=lambda sub:sub[-1])

            if len(newClause) == 1:
                result = result + newClause
            elif len(newClause) > 1:        
                result.append(' OR '.join(newClause))

    return removeDuplicates(result)

def PL_resolution(a, kb, name):
    nega_a = negation(a)
    clauses = []
    new = []
    
    splitPos = name.rfind('.')
    fname = './Output/' + name[:splitPos] + '_result.txt'
    fw = open(fname, 'w')

    for c in kb:
        clauses.append(c)
    for n in nega_a:
        clauses.append(n)
    clauses = removeDuplicates(clauses) #xoá phần tử trùng lặp nếu có

    while True:
        resolvents = []
        for i in range(len(clauses) - 1):
            for j in range(i + 1, len(clauses)):
                resolvent = PL_resolve(clauses[i],clauses[j])
                if len(resolvent ) != 0:
                    resolvents = resolvents + resolvent
                    
        resolvents = removeDuplicates(resolvents)

        newNum = 0
        for re in resolvents:
            if notIn(re, clauses):
                newNum += 1
        
        fw.write(str(newNum) + '\n')
        for re in resolvents:
            if notIn(re, clauses):
                new.append(re)
                fw.write(str(re) + '\n')

        if '{}' in resolvents:
            fw.write('YES')
            return 
                
        if isChildOf(new, clauses):
            fw.write('NO')
            return 
                
        for n in new:
            if notIn(n, clauses):
                clauses.append(n)
                
#Hàm main----------------------------------------------------------------
def main():
    fileName = input('input file name: ')
    path = './Input/' + fileName#file input phải nằm trong thư mục Input

    alpha, kb = readFile(path)
    PL_resolution(alpha, kb, fileName)
    print("execution finished")

main()