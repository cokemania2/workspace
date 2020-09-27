function possible(arr) {
	let possibleArr = new Array(arr[0].length);
	for (let i=0;i<arr.length;i++) {
		for (let j=0;j<arr[i].length;j++) {
			if (arr[i][j] == 'O')
				possibleArr[j] = true;
		}
	}
	for (let i=0;i<arr[0].length;i++) {
		if (possibleArr[i] == undefined) {
			return (false);
		}
	}
	return (true);
}

function getAllCombinations(table,index,arr, i) {
	
	if (i == 0) {
		if (possible(arr)) {
			return (true);
		}
	}
	else {
		for (j = index;j<table.length;j++) {
			arr.push(table[j]);
			if (getAllCombinations(table,j + 1,arr,i - 1))
				return (true);
			arr.pop();
		}
	}
}

function solution(table) {
	var answer = 0;
	for (let i =1;i<=table.length;i++) {
		for (let j=0;j<table.length;j++) {
			if (getAllCombinations(table,j,[],i))
				return (i);
		}
	}
}

console.log(solution(["XOXO", "OXXO", "XXOX", "XOOO"]));
