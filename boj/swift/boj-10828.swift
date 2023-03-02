import Foundation

let n = Int(readLine()!)!
var stack: [Int] = []

for _ in 0..<n {
    let cn = readLine()!.split(separator: " ")
    let command = cn[0]
    let num = (cn.count == 2) ? Int(cn[1]) : nil
    
    switch command {
    case "push":
        stack.append(num!)
    case "pop":
        print(stack.popLast() ?? -1)
    case "size":
        print(stack.count)
    case "empty":
        _ = (stack.count == 0) ? print(1) : print(0)
    case "top":
        print(stack.last ?? -1)
    default:
        continue
    }
}

