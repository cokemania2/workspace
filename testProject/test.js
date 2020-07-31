/**
 * @param {string} text 금액을 담고 있는 문자열
 * @returns {number} 문자열으로부터 뽑아낸 금액 숫자
 */
function getAmount(text) {
	let result = '';
	for (let i=0;i<text.length;i++) {
		const a = text.charAt(i);
		if (a >= '0' && a<= '9') {
			result = result + a;
		}
	}
	return result;
}

console.log(getAmount('$1,250'));
