/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let g=init;
    for (let i=0;i<nums.length;i++){
        g=fn(g,nums[i]);
    }
    return g;
};