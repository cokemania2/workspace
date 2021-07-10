'use strict';
// Promise is a Javascript object for asynchronous operation.

// 상태에대해서 이해가 중요.
// producer와 consumer를 이해하는것이 중요 

// state : pending -> fulfilled or rejected 
// Producer vs Consumer 

// 1. Producer 

// when new Promise is created, the executor runs automatically !!
const promise = new Promise((resolve,reject)=>{
    // doing some heavy work (network , read files) 
    console.log('doing something...');
    setTimeout(()=>{
        resolve('ellie');
        reject(new Error('no network'));
    },2000);
})

// 2. Consumers  :then, catch, finally 
promise
    .then((value)=>{
       console.log(value);
    })
    .catch(error=>{
        console.log(error);
    })
    .finally(()=>{
        console.log('finally');
    })

// 3. Promise chaining 

const fetchNumer = new Promise((resolve,reject) =>{
	setTimeout(()=> resolve(1), 1000);
});

fetchNumer
.then(num => num *2)
.then(num => num *3)
.then(num =>{
	return new Promise((resolve,reject) =>{
		setTimeout(()=> resolve(num-1),1000);
	});
})
.then(num => console.log(num));


// 4. Error Handling
const getone = () => 
	new Promise((resolve,reject)=>{
		setTimeout(()=> resolve('1'),1000);
	});

const getTwo = one =>
	new Promise((resolve,reject)=>{
		setTimeout(()=> resolve(`${one} => 2`,1000));
	});

const getThree = two =>
	new Promise((resolve,reject)=>{
		setTimeout(()=> resolve(`${two} => 3`,1000));
	});

getone()
	.then(one => getTwo(one)) // .then(getTwo) 로도 간략화 가능 
	.then(two => getThree(two))
	.catch(error => {
		return '-1'; // 에러가 나면 -1로 대체
	})
	.then(final => console.log(final));