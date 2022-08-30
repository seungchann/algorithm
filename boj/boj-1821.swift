/**
boj-1821
https://www.acmicpc.net/problem/1821
*/

func solve(_ arr: [Int]) -> Int {
    var result: [Int] = arr
    var nextResult: [Int] = []

    while true {
        if result.count == 1 {
            break
        }

        for (idx, val) in result.enumerated() {
            if idx == result.count-1 { continue }
            nextResult.append(val + result[idx+1])
        }

        result = nextResult
        nextResult = []
    }

    return result[0]
}

func permutation(_ target: [Int], _ targetNum: Int, _ f: Int) {

    var result: [[Int]] = []
    // 사용된 원소인지 확인하기 위한 함수
    var check = [Bool](repeating: false, count: target.count)

    // 위의 변수들을 이용하기 위해 안에 연산만 하는 함수 구현
    func permute(_ arr: [Int]) {
        if arr.count == targetNum {
            if solve(arr) == f { result.append(arr) }
            return
        }

        for i in 0..<target.count {
            if result.count == 1 { break }
            // 이미 사용된 원소인지 확인
            if check[i] == true {
                continue
            } else {
                check[i] = true
                permute(arr + [target[i]])
                check[i] = false
            }
        }
    }

    permute([])
    result[0].forEach { print($0, terminator: " ") }

    return
}

func main() {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    let n = input[0], f = input[1]
    permutation(Array(1...n), n, f)
}

main()