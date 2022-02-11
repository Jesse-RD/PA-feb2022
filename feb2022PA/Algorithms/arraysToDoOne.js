// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

function addToArray(arr, val) {
    var i = arr.length;
    while (i-- > 0) {
        arr[i + 1] = arr[i];
    }
    arr[0] = val;
    console.log(arr);
}

addToArray([1,3,5], 7)



// Pop Front
// Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function firstIndex(arr) {
    var i0 = arr[0];
    const len = arr.length;
    for (let i=0; i<len-1; i++){
        let temp = arr[i+1];
        arr[i+1] = arr[i];
        arr[i] = temp;
    }
    arr.pop();
    console.log(arr);
    console.log(i0);
    }

firstIndex([7,1,3,5])



// Insert At
// Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).

function insertValue(arr, ind, val) {
    var i = arr.length;
    arr[i] = val;
    while (i-- > ind) {
        let temp = arr[i + 1];
        arr[i + 1] = arr[i];
        arr[i] = temp;
    }
    console.log(arr);
}

insertValue([1,3,5,9,11], 3, 7)