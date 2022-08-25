/** 
boj-17478.swift
https://www.acmicpc.net/problem/17478
*/

func recursive(_ n: Int, _ start: inout Int) {
    let prefix = String(repeating: "_", count: 4 * start)
    print(prefix + "\"재귀함수가 뭔가요?\"")
    if start < n {    
        print(prefix + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(prefix + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(prefix + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        start += 1
        recursive(n, &start)
    } else if start == n {
        print(prefix + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    }
    print(prefix + "라고 답변하였지.")
}

func solve(_ n: Int) {
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    var start = 0
    recursive(n, &start)
}

func main() {
    let n = Int(readLine()!)!
    solve(n)
}

main()