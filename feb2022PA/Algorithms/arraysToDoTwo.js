// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, 
// with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means 
// that you cannot use a second array – move values within the array that you are given. As always, do not use 
// built-in array functions such as splice().

function reverse(arr) {
    len = arr.length-1;
    for(let i=0; i<=len/2; i++) {
        let temp = arr[i];
        arr[i] = arr[len-i];
        arr[len-i] = temp;
    }
    console.log(arr);
}

console.log("----1----")
reverse([9,7,5,3,1]);


// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 
// 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: 
// given ([1,2,3],1), change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.

function rotateArrPos(arr, shiftBy) {
    var len = arr.length;
    for (let s=0; s<shiftBy; s++) {
        var temp = arr[len-1];
        for (let i=len; i>0; i--) {
            arr[i] = arr[i-1];
        }
        arr[0] = temp;
        arr.length--;
    }
    console.log(arr);
}

function rotateArrNeg(arr, shiftBy) {
    var len = arr.length;
    for (let s=0; s<shiftBy; s++) {
        var temp = arr[0];
        for (let i=0; i<len-1; i++) {
            arr[i] = arr[i+1];
        }
        arr[len-1] = temp;
    }
    console.log(arr);
}

console.log("----2----")
console.log("Positive Rotation:")
rotateArrPos([1,2,3,4,5,6,7,8,9],3);
console.log("Negative Rotation:")
rotateArrNeg([1,2,3,4,5,6,7,8,9],3);


// Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. 
// Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array 
// you are given, with values in original order. No built-in array functions.

function filterMinMax(arr, min, max) {
    var len = arr.length;
    for (let l=min; l>0; l--) {
        for (let i=0; i<len-1; i++) {
            arr[i] = arr[i+1];
        }
        arr.length--;
    }
    var newLen = arr.length;
    for (let h=max-min; h<newLen+1; h++) {
        arr.length--;
    }
    console.log(arr);
}

console.log("----3----")
filterMinMax([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 5, 17);

// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing 
// the first array's elements, followed by the second array's elements. Do not alter the original arrays. 
// Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].

function arrConcat(arr, arr2) {
    var len = arr.length;
    var len2 = arr2.length;
    var newArr = [];
    for (let i=0; i<len; i++) {
        newArr[i] = arr[i];
    }
    for (let i=0; i<len2; i++) {
        newArr[len+i] = arr2[i];
    }
    console.log(newArr);
}

console.log("----4----")
arrConcat( ['a','b','c','d'], [1,2,3,4,5,6,7,8] );