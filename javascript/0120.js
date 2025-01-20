function greet() {
  console.log(`안녕하세요. 저의 이름은 ${this.name} 입니다.`);
}

const boy =  {
  name: '철수',
  greet_boy: greet
};

const girl = {
  name: '영희',
  greet_girl: greet
};
boy.greet_boy()
girl.greet_girl()