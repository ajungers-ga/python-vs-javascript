# 1. Get Name
# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# def get_name():
#     name = input("what is your name?")
#     return name
# print("hello, " + get_name() + "!")





# 2. Reverse It
# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";
#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

# def reverse_it():
#     string = "a man, a plan, a canal, frenemies!"
#     reverse = ""
    
#     for i in range(len(string)):
#         reverse += string[len(string) - (i + 1)]
        
#     print (reverse)
        
# reverse_it()        
        




# 3. Swap Em
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

# def swap_em():
#     a = 10
#     b = 30
    
#     temp = b
#     b = a
#     a = temp
    
#     print("a is now " + str(a) + ", and b is now " + str(b))
    
# swap_em()    





# 4. Multiply Array/List
# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# def multiply_array(numbers):
#     if len(numbers) == 0:
#         return 1
    
#     total = 1
#     for i in range(len(numbers)):
#         total = total * numbers[i]
        
#     return total
    
# print ("The product is: " + str(multiply_array([2, 3, 4])))    

# 5. Fizz Buzzer
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

# def fizz_buzzer(x):
#     if x % (3 * 5) == 0:
#         return "fizzbuzz"
#     elif x % 3 == 0:
#         return "fizz"
#     elif x % 5 == 0:
#         return "buzz"
#     else:
#         return "archer"
    
# print(fizz_buzzer(3 * 5))
# print(fizz_buzzer(3))
# print(fizz_buzzer(5))
# print(fizz_buzzer(4))





# 6. Nth Fibonacci
# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

# def nth_fibonacci_number():
#     fibs = [1, 1]
#     num = int(input("which Fivonacci number do you want?"))
    
#     while len(fibs) < num:
#         length = len(fibs)
#         next_fib = fibs[length - 2] + fibs[length -1]
#         fibs.append(next_fib)
        
#     print(str(fibs[-1]) + " is the fibonacci number at position " + str(num))

# nth_fibonacci_number()        




 
# 7. Search Array/List
# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };
 
# def search_array(array, value):
#     for i in range(len(array)):
#         if array[i] == value:
#             return True
#     return False

# print(search_array([3, 6, 9, 12, 15], 9))
# print(search_array([3, 6, 9, 12, 15], 99))





# 8. Palindrome
# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

# def is_palindrome(string):
#     for i in range(len(string) // 2):
#         if string [i] != string[len(string) - i - 1]:
#             return False
#     return True

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))





# 9. hasDupes
# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def has_dupes(arr):
    seen = {}
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        else:
            seen[arr[i]] = True
    return False
    
print(has_dupes([1, 2, 3, 4, 5]))
print(has_dupes([1, 2, 3, 4, 2, 5]))                 