#!/usr/bin/node

function factorial (num) {
    if (num < 0) {
      return -1;
    } else if (num === 0) {
      return 1;
    } else {
      return (num * factorial(num - 1));
    }
  }
  
  const a = process.argv[2];
  
  if (isNaN(a)) {
    console.log(1);
  } else {
    console.log(factorial(a));
  }
