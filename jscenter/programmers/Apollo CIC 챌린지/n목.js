function possibleR(h,w,i,j,n,board) {
	if (j + n <= w) {
		for (let x = j; x<j+n; x++) {
			if (board[i][x] == '0')
				return (false);
		}
		if (j+n < w && board[i][j+n] == '1') {
			return (false);
		}
		if (j - 1 >= 0 && board[i][j-1] =='1') {
			return (false);
		}
		return (true);
	}
}

function possibleD(h,w,i,j,n,board) {
	if (i + n <= h) {
		for (let x = i;x <i +n; x++) {
			if (board[x][j] == '0')
				return (false);
		}
		if (i + n < h && board[i+n][j] == '1') {
			return (false);
		}
		if (i - 1 >= 0 && board[i-1][j] =='1') 
			return (false);
		return (true);
	}
}

function possibleDR(h,w,i,j,n,board) {
	if (i + n <= h && j + n <= w) {
		for (let x=0;x<n;x++) {
			if (board[i+x][j+x] == '0') {
				return (false);
			}
		}
		if (i-1 >= 0 && j-1>=0 && board[i-1][j-1] == '1')
			return (false);
		if (i+n < h && j+n < w && board[i+n][j+n] =='1') {
			return (false);
		}
		return (true);
	}
}

function possibleDL(h,w,i,j,n,board) {
	if (i + n <= h && (j+1) - n >= 0) {
		for (let x=0;x<n;x++) {
			if (board[i+x][j-x] == '0') {
				return (false);
			}
		}
		if (i+n < h && j-n >=0 && board[i+n][j-n] == '1') {
			return (false);
		}
		if (i-1 >= 0 && j+1 < w && board[i-1][j+1] =='1') {
			return (false);
		}
		return (true);
	}
}

function solution(h, w, n, board) {
	var answer = 0;
	for (let i=0;i<h;i++){
		for (let j=0;j<w;j++) {
			if (board[i][j] == '1') {
				if (possibleR(h,w,i,j,n,board)) 
					answer++;
				if (possibleD(h,w,i,j,n,board))
					answer++;
				if (possibleDR(h,w,i,j,n,board))
					answer++;
				if (possibleDL(h,w,i,j,n,board)) 
					answer++;
			}
		}
	}

    return answer;
}