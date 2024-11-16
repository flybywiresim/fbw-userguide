# Javascript

Please utilize the following information when developing for the A32NX to keep your JavaScript functions clean. 

## Tips and Tricks

### Don't use eval
    
Just don't.

### Don't reassign function parameters

```js
function foo(bar) {
  bar = 1; // no!
}
```

### Don't add or remove properties from objects

```js
delete obj.x; // no!
```

```js
const obj = { y: 1 };
obj.x = 2; // no!
```

```js
class X {
  constructor() {
    this.y = 1;
  }

  method() {
    this.x = 2; // no!
  }
}
```

### Use specific methods over generic loops where possible

Do not:
```js
// no!
for (const item of array) {
  // ...
}
```
Do:
```js
// yes!
array.forEach((item) => {
});
```

### Don't create arrays with holes

```js
// no!
const array = new Array(5).fill(0);
// yes!
let array = Array.from({ length: 5 }, () => 0);
```

### Use strict equality

```js
// no!
a == b;
// yes!
a === b;
```