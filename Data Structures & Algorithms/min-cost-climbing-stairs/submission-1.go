func minCostClimbingStairs(cost []int) int {
    if len(cost) == 2{
        return min(cost[0], cost[1])
    }

    c := make([]int, len(cost))

    c[len(cost)-1] = cost[len(cost)-1]
    c[len(cost)-2] = cost[len(cost)-2]

    for i := len(cost) - 3; i >= 0; i -= 1{
        c[i] = cost[i] + min(c[i+1], c[i+2])
    }

    return min(c[0],c[1])
}