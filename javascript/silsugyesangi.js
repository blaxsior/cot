// Run by Node.js

function gcd(a, b){
	let c;
	while(b) {
		c = a % b;
		a = b;
		b = c;
	}
  return a;
}

function lcm(a, b) {
	return a * b / gcd(a,b);
}

class RealNum {
	constructor(top, bot) {
		this.top = top;
		this.bot = bot;
	}
	
	getnum() {
		const div = this.top / this.bot;
		const trunc = Math.trunc(div);
		if(div === trunc) {
			return trunc;
		}
		
		return [this.top, this.bot];
	}
	
	add(target) {
		const gcdnum = gcd(this.bot, target.bot);
		// 3/4 5/6 => 나눈 값 상대방한테 곱할 예정.
		const mul2 = this.bot / gcdnum;
		const mul1 = target.bot / gcdnum;
		
		const newtop = mul1 * this.top + mul2 * this.bot;
		const newbot = mul1 * mul2 * gcdnum;
		
		return new RealNum(newtop, newbot);
	}
	
	sub(target) {
				const gcdnum = gcd(this.bot, target.bot);
		// 3/4 5/6 => 나눈 값 상대방한테 곱할 예정.
		const mul2 = this.bot / gcdnum;
		const mul1 = target.bot / gcdnum;
		
		const newtop = mul1 * this.top - mul2 * this.bot;
		const newbot = mul1 * mul2 * gcdnum;
		
		return new RealNum(newtop, newbot);
	}
	
	mul(target) {
		const top = this.top * target.top;
		const bot = this.bot * target.bot;
		const gcdnum = gcd(top, bot);
		
		return new RealNum(top / gcdnum, bot / gcdnum);
	}
	
	div(target) {
		const top = this.top * target.bot;
		const bot = this.bot * target.top;
		const gcdnum = gcd(top, bot);
		
		return new RealNum(top / gcdnum, bot / gcdnum);
	}
}

class Parser {
  static parse(str) {
    const tokens = [];
    let i = 0;
    let isNumChance = true;
    while(i < input.length) {
      const ch = input[i];
      switch(ch) {
          // 분수
        case "[":
          let top = "";
          let bot = "";
          i++;
          while(i < input.length && input[i] != ",") {
            top += input[i++];
          }
          i++ // 쉼표
          while(i < input.length && input[i] != "]") {
            bot += input[i++];
          }
          tokens.push(new RealNum(parseInt(top), parseInt(bot)));
          isNumChance = false;
          break;
        case "+":
          tokens.push("+");
          isNumChance = true;
          break;
        case "-":
          // 숫자 앞에 붙는거
          if(isNumChance) {
            const top = "-";
            i++;
            while(i < input.length) {
              let n = input.charCodeAt(i) - 48; 
              if(n < 0 || n > 9) {
                // 문자 아님.
                i--;
                break;
              }
            }
            tokens.push(new RealNum(parseInt(top), 1));
            isNumChance = false;
          } else {
            tokens.push("-");
            isNumChance = true;
          }
          break;
        case "*":
          tokens.push("*");
          isNumChance = true;
          break;
        case "/":
          tokens.push("/");
          isNumChance = true;
          break;
      }
      i++;
    }
  }
}

const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let input = [];
	
	for await (const line of rl) {
		input = line.split('').filter(it => it !== ' ');
		rl.close();
	}
	
	console.log(input);
	
	const num1 = new RealNum(3, 4);
	const num2 = new RealNum(5, 6);
	
	console.log(num1.add(num2).getnum());
	
	process.exit();
})();

// 컴파일러 작성해야 함.
// 연산 정리하고 후위로 처리하고...

// [1, 2] + [2, 3] * [2, 3]
// 