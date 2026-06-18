func productExceptSelf(nums []int) []int {

    ret := make([]int, len(nums))

    pre := 1
    for i := range nums {
        ret[i] = pre
        pre *= nums[i]
    }

    suf := 1
    for i := len(nums) - 1; i >= 0; i-- {
        ret[i] *= suf
        suf *= nums[i]
    }

    return ret

}
