/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const c = {};
    return function(...args) {
        let key = String(args);

        if(key in c){
            return c[key];
        }
        
        return c[key] = fn(...args);
}
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */