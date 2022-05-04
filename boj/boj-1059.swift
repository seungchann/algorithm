import Foundation

let l = Int(readLine()!)!
var array: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
array.sort()
let n = Int(readLine()!)!

if array.contains(n) {
    print(0)
} else {
    var left = 0, right = 0
    for (idx, num) in array.enumerated() {
        if n < num {
            right = array[idx]
            break
        }
        else {
            left = array[idx]
        }
    }
    right -= 1
    left += 1

    print((right - left) + ((n-left) * (right-n)))
}