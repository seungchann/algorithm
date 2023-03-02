import Foundation

let t = Int(readLine()!)!

for _ in 0..<t {
    var stack: [String] = []
    var input = Array(readLine()!.map { String($0) })
    var valid = true
    
    while (!input.isEmpty) {
        let cur = input.popLast()
        if cur == ")" { stack.append(cur!) }
        else {
			if stack.isEmpty {
				valid = false
				break
			}
            _ = stack.popLast()
        }
    }
    valid = valid && ((stack.isEmpty) ? true : false)
    print((valid) ? "YES" : "NO")
}

