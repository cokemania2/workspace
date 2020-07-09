// ERROR message ( !if ECMA 5 )
'use strict';

// 2. Variable 변수 
// let ( added in ES6 ) 
// let밖에 없음 ! ( var X )

// var hoisting (move declation from bottom to top)
// has no block scope ( 블럭을 신경쓰지 않음 )
{
    let name = 'my';
    console.log(name);
}
console.log(name); //global


// ( W ) 
// Constans ( 정적인 변수 ) , Immutable data type always
// - security , - thread safety , - reduce human mistakes  

const dayInWeek  = 7;
const maxNumber = 5;


// Variable types (RW)
// primitive single item : number, string, boolean, null, undefined, symbol 
// object, box container
// function, first-class function 
// first-class function ( 변수에 활용이 가능하다 ) 


const infinity  = 1/0; 
console.log(infinity);

//const bigInt  =12123123123123123123123n; // bigint 
const char = 'c';
const brendan  =  'brenden'; 
console.log(char+brendan);
console.log(`hello ${char}`);

let undefined = undefined;
 

// Dynamic typing 
// c나 java와는 다르게 선언할때 어떤 타입인지 선언하지않고 할당된 값에따라서 함 
// 이래서 typeScript가 나왔음 

let text = 'hello';
let man = {name : 'my', age  : 18};
console.log(`value : ${text}`);

// primitive type 은 메모리에 저장이됨 
// object는 ref를통해서 담겨있는 메모리를 가리키게 됨
 

