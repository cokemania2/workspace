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

const fetchNumber = new Promise((resolve,reject) =>{
    setTimeout(()=>resolve(1),1000);
})

fetchNumber
    .then(num => num*2)
    .then(num => num*3) 
    .then(num=> {
        return new Promise((resolve,reject)=>{
            setTimeout(()=>resolve(num-1),1000);
        });
    })
    .then(num=>console.log(num));


    // 4. Error Handling 
    const getHen = () => 
        new Promise((resolve,reject) =>{
            setTimeout(()=> resolve('닭'),1000);
        });
    const wldn = hen => 
        new Promise((resolve,reject)=>{
            setTimeout(()=> reject(new Error(`${hen} => 알`)),1000);
        });
    const cook = egg =>
        new Promise((resolve,reject)=>{
            setTimeout(()=> resolve(`${egg} => 후라이팬`),1000);
        });

    getHen()
    .then(wldn) //then에서 가져오는 value를 wldn로 바로 전달 
    .catch(error => {
        return '빵';
    })
    .then(cook)
    .then(meal=>console.log(meal));
    // == .then(meal=>console.log())


