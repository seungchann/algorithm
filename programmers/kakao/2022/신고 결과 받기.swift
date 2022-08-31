import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reportedIDDict: [String: ([String], Int)] = [:]
    var IDIdxDict: [String: Int] = [:]
    var result: [Int] = Array(repeating: 0, count: id_list.count)

    for (idx, id) in id_list.enumerated() { 
        reportedIDDict.updateValue(([], 0), forKey: id) 
        IDIdxDict.updateValue(idx, forKey: id)
    }

    report.forEach {
        let reporterUser = $0.split(separator: " ").map { String($0) }
        let reporter = reporterUser[0], user = reporterUser[1]

        if !reportedIDDict[user]!.0.contains(reporter) { 
            var tempArr = reportedIDDict[user]!.0 + [reporter]
            var tempCnt = reportedIDDict[user]!.1 + 1

            reportedIDDict.updateValue((tempArr, tempCnt), forKey: user)  
        }
    }

    for (reporterArr, cnt) in Array(reportedIDDict.values) {
        if cnt >= k {
            reporterArr.forEach { result[IDIdxDict[$0]!] += 1 }
        }
    }

    return result
}
