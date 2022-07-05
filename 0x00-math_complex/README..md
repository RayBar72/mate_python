0x00. Math - Complex

Tasks
0. Structure Complex
Build the structure “complex” where a complex number a + ib is represented by two doubles.
Write a function that displays the complex numbers, followed by a new line.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 0-main.c 0-display.c -o 0-complex
julien@ubuntu:~/0x00-math_complex$ ./0-complex
1 + 2i
1


1. Conjugate
Write a function that returns the conjugate of a given complex number.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 1-main.c 1-conjugate.c 0-display.c -o 1-conjugate
julien@ubuntu:~/0x00-math_complex$ ./1-conjugate
1 - 2i
1 + 2i


2. Modulus
Write a function that returns the modulus of a given complex number.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 -lm 2-main.c 2-modulus.c -o 2-modulus
julien@ubuntu:~/0x00-math_complex$ ./2-modulus
2.236068


3. Argument
Write a function that returns the argument of a given complex number.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 3-main.c 3-argument.c -lm -o 3-argument
julien@ubuntu:~/0x00-math_complex$ ./3-argument
1.107149


4. Addition
Write a function that performs the addition operation to complex numbers.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 4-main.c 4-addition.c 0-display.c -o 4-addition
julien@ubuntu:~/0x00-math_complex$ ./4-addition
1 + i
1 + 2i
2 + 3i


5. Substraction
Write a function that performs the substraction operation to complex numbers.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 5-main.c 5-substraction.c 0-display.c -o 5-substraction
julien@ubuntu:~/0x00-math_complex$ ./5-substraction
1 + i
1 + 2i
0 - i


6. Multiplication
Write a function that performs the multiplication operation to complex numbers.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 6-main.c 6-multiplication.c 0-display.c -o 6-multiplication
julien@ubuntu:~/0x00-math_complex$ ./6-multiplication
1 + 2i
2 + 2i
-2 + 6i


7. Division
Write a function that performs the division operation to complex numbers.

julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 7-main.c 7-division.c 0-display.c -o 7-division
julien@ubuntu:~/0x00-math_complex$ ./7-division
4 + 3i
2 + i
2.2 + 0.4i


8. Real and imaginary
Write a function that update the real and the imaginary parts of a complex number given its modulus and arguments.


julien@ubuntu:~/0x00-math_complex$ gcc -Wall -Werror -pedantic -Wextra -std=c89 -lm 8-main.c 8-complex.c 0-display.c 2-modulus.c 3-argument.c -o 8-complex
julien@ubuntu:~/0x00-math_complex$ ./8-complex
2 + 2i
2 + 2i
