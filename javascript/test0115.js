let completeTask = function(){
  console.log('함수 시작')
}

startTask(completeTask)

function startTask(A) {
  A();
}