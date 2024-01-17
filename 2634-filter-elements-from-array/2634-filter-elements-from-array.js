/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const arr1=new Array();
    let p=0;
    for(let i=0;i<arr.length;i++){
        let y=fn(arr[i],i);
        if (y){
            arr1[p]=arr[i];
            p+=1;
        }
    }
    return arr1;
};