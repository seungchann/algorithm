/**
boj-1269.swift
https://www.acmicpc.net/problem/1269
*/

func main() {
    let _ = readLine()
    var a = Set<Int>(readLine()!.split(separator: " ").map { Int(String($0))! })
    let b = Set<Int>(readLine()!.split(separator: " ").map { Int(String($0))! })
    a.formSymmetricDifference(b)
    print(a.count)
}

main()