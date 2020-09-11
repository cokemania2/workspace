const newYears = '1 Jan 2021';

let daysel = document.getElementById('days');
let hoursel = document.getElementById('hours');
let minutesel = document.getElementById('minutes');
let secondsel = document.getElementById('seconds');


function countdown() {
	const currentDate = new Date();
	const newYearsDate = new Date(newYears);

	const totalSeconds = (newYearsDate - currentDate) / 1000;
	const days = Math.floor( totalSeconds / 3600 / 24);
	const hours = Math.floor( totalSeconds / 3600) % 24;
	const minutes  = (Math.floor( totalSeconds / 60) % 24) % 60;
	const second = Math.floor(totalSeconds) % 60; 

	daysel.innerHTML = (days);
	hoursel.innerHTML = formatTime(hours);
	minutesel.innerHTML = formatTime(minutes);
	secondsel.innerHTML = formatTime(second);
	console.log(days,hours,minutes,second);
}

function formatTime (time) {
	return time < 10 ? `0${time}` : time;
}

//Initial call
countdown();
setInterval(countdown,1000);
