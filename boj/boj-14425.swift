/**
boj-14425.swift
https://www.acmicpc.net/problem/14425
*/

func main() {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    let n = input[0], m = input[1]
    var strs = Set<String>()
    var result = 0

    for _ in stride(from: 0, to: n, by: 1) { strs.insert(readLine()!) }
    for _ in stride(from: 0, to: m, by: 1) { result += strs.contains(readLine()!) ? 1 : 0 }

    print(result)
}

main()