include prelude

let data = readFile("input/day1.txt")
let values = data.splitLines().map(parseInt)

echo zip(values, values[3..^1]).countIt it[1]>it[0]



