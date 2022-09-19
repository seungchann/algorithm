/**
boj-11478.swift
https://www.acmicpc.net/problem/11478
*/

let input = readLine()!
var result = Set<Substring>() 

for i in input.indices {
    for j in input.indices[i...] {
        result.update(with: input[i...j])
    }
}

print(result.count)