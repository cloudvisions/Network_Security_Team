Network_Security_Team

Team Project 980404 이현정
***
1.1 (2022-09-12) C언어 Advanced
***
포인터(Pointer)

포인터도 변수이며 C 프로그래밍 언어에서 매우 중요한 역할을 한다. 다음과 같은 여러 가지 이유로 사용된다.
- 문자열
- 동적 메모리 할당
- 참조로 함수 인수 보내기
- 복잡한 데이터 구조 구축
- 함수를 가리킴
- 특수 데이터 구조 구축(예: 트리, 트라이즈 등..)

그리고 그 이상 등등..

포인터란 무엇인가?

포인터는 본질적으로 실제 값 자체를 보유하는 대신 값을 가리키는 메모리 주소를 보유하는 단순한 정수 변수이다.
컴퓨터의 메모리는 데이터를 순차적으로 저장하며 포인터는 메모리의 특정 부분을 가리킨다.
우리 프로그램은 포인터가 많은 양의 메모리를 가리키는 방식으로 포인터를 사용할 수 있다.해당 지점에서 읽기로 결정한 양에 따라 다르다.

포인터로서의 문자열
우리는 이미 문자열에 대해 논의했지만 이제 좀 더 깊이 파고들어 C의 문자열이 실제로 무엇인지 이해할 수 있다.(C++과 혼합할 때 다른 문자열과 구별하기 위해 C-String이라고 한다.)

다음 문장에서 
char * name = "John";
은 세 가지를 수행한다.

1. name이라고 불리는 단일 문자에 대한 포인터는 로컬(스택)변수를 할당한다.
2. 이것은 문자열 "John"이 프로그램 메모리 어딘가에 나타나게 한다.(물론 컴파일되고 실행된 후)
3. name이라는 문자가 있는 위치를 가리키도록 인수를 초기화 한다. J가 포함된 문자는 메모리의 나머지 문자열이 온다.

name 변수에 배열로 액세스하려고 하면 변수가 실제로 문자열의 시작 부분을 정확히 가리키므로 J가 포함된 문자는 문자의 서수 값을 반환한다.

메모리가 순차적이라는 것을 알고 있기 때문에 메모리에서 다음 문자로 이동하면 문자열의 끝에 도달할 때까지 문자열의 다음 문자를 수신할 것이라고 가정할 수 있다. 이 문자는 null 종결자로 표시된다. (서수 값-ordinal value-이 0인 문자로 표시된다.)

역참조

역참조는 메모리 주소 대신 포인터가 가리키는 위치를 참조하는 행위이다. 우리는 이미 배열에서 역참조를 사용하고 있다. 그러나 우리는 아직 그것을 몰랐을 뿐이다. 대괄호 연산자 - 예를 들어 배열의 첫 번째 항목에 액세스한다. 그리고 배열은 실제로 포인터이기 때문에 배열의 첫 번째 항목에 액세스하는 것은 포인터를 역참조하는 것과 같다. 포인터 역참조는 별표 연산자를 사용하여 수행된다.

스택의 다른 변수를 가리키는 배열을 만들고 싶다면 다음 코드를 작성할 수 있다.

/* define a local variable a */
int a = 1;

/* define a pointer variable, and point it to a using the & operator */
int * pointer_to_a = &a;

printf("The value a is %d\n", a);
printf("The value of a is also %d\n", *pointer_to_a);

방금 만든 &변수를 가리키기 위해 연산자를 사용했다.

그런 다음 역참조 연산자를 사용하여 참조했다. 역참조된 변수의 내용을 변경할 수도 있다.

int a = 1;
int * pointer_to_a = &a;

/* let's change the variable a */
a += 1;

/* we just changed the variable again! */
*pointer_to_a += 1;

/* will print out 3 */
printf("The value of a is now %d\n", a);

연습

지역 변수 n이라고 불리는 pointer_to_n이라는 포인터 변수를 만들고 이 값을 n에서 1만큼 늘린다.

#include <stdio.h>

int main() {
	int n = 10;

	int * pointer_to_n = &n;

	*pointer_to_n += 1;

	/* testing code */
	if (pointer_to_n != &n) return 1;
	if (*pointer_to_n ! = 11) return 1;

	printf("Done!\n");
	return 0;
}
***
1.2 (2022-09-12) C언어 Advanced
***
구조체

C 구조체는 몇몇의 이름있는 변수들을 안에 포함하는 특수하고도 큰 변수이다. 구조체들은 C에서 객체와 클래스들의 기본 토대이다. 구조체들은 다음에서 사용된다.
- 데이터의 직렬화
- 단일 인수를 통해 함수 안과 밖으로 여러 인수 전달
- 연결 목록, 이진 트리 등과 같은 데이터 구조

구조의 가장 기본적인 예는 두 개의 변수(x와 y)를 포함하는 단일 엔티티인 포인터이다. 포인터를 정의해보자.

struct point {
	int x;
	int y;
};

지금, 새로운 포인터를 정의하고 사용해보자. 함수 draw가 포인터를 받아 화면에 그린다고 가정해보자. 구조체가 없으면 모든 좌표에 대해 각각 두 개의 인수가 필요하다.

/* draws a point at 10, 5 */
int x = 10;
int y = 5;
draw(x, y);

구조체를 사용하여 포인터 인수를 전달할 수 있다.

/* draws a point at 10, 5 */
struct point p;
p.x = 10;
p.y = 5;
draw(p);

포인터 변수에 액세스하려면 점(dot) 연산자를 사용한다.

형식정의

형식정의를 사용하면 다른 이름으로 유형을 정의할 수 있다. 이는 구조체와 포인터를 다룰 때 유용할 수 있다.
이 경우 우리는 포인터 구조체의 긴 정의를 제외하고 싶을 것이다. 다음 구문을 구조체를 사용하여 새 포인터를 정의할 때마다 키워드를 제거할 수 있다. 

typedef struct {
	int x;
	int y;
} point;

이렇게 하면 다음과 같이 새 포인터를 정의할 수 있다.

point p;

구조체는 또한 포인터를 보유할 수 있다.(문자열을 보유할 수 있도록 하거나 다른 구조체에 대한 포인터도 보유할 수 있음). 이것이 진정한 파워이다. 예를 들어, 다음과 같은 방식으로 탈것의 구조를 정의할 수 있다.

typeof struct {
	char * brand;
	int model;
} vehicle;

brand는 char 포인터이므로 탈것 유형에는 문자열(이 경우 차량의 브랜드를 나타냄)이 포함될 수 있다.

vehicle mycar;
mycar.brand = "Ford";
mycar.model = 2007;

연습

name이라는 문자열(char에 대한 포인터)과 age라는 정수를 포함하는 "person"이라는 새 데이터 구조를 정의한다.

#include <stdio.h>

typedef struct {
	char * name;
	int age;
} person;

int main () {
	person john;

	/* testing code */
	john.name = "John";	
	john.age = 27;
	printf("%s is %d years old.", john.name, john.age);
}
***
1.3 (2022-09-12) C언어 Advanced
***
참조에 의한 함수 인수

이제 포인터와 함수를 이해한다고 가정하면 함수 인수가 값으로 전달된다는 점을 알고 있을 것이다. 즉, 함수 안과 밖으로 복사된다. 그러나 값 자체 대신 값에 대한 포인터를 전달하면 어떻게 될까? 이것은 우리가 부모 함수의 변수와 구조에 대한 제어권을 함수에 부여할 수 있게 하며, 따라서 원본 객체를 직접 읽고 쓸 수 있다.

숫자를 1씩 증가시키는 addone이라는 함수를 작성한다고 가정해보자. 이것은 실행되지 않는다.

void addone(int n) {
	// n is local variable which only exists within the function scope
	n++; // therefore incrementing it has no effect
}

int n;
printf("Before: %d\n", n);
addone(n);
printf("After: %d\n", n);

그러나 다음과 같이 실행된다.
void addone(int *n) {
	// n is a pointer here which point to a memory-address outside the function scope (*n)++; 
	// this will effecctively increment the value of n
}

int n;
printf("Before: %d\n", n);
addone(&n);
printf("After: %d\n", n);

addone의 두번째 버전의 차이점은 변수에 대한 포인터를 n인수로 받은 다음 메모리의 위치를 알고 있기 때문에 이를 조작할 수 있다는 것이다. 
addone 함수를 호출할 때 변수 자체가 아니라 변수 n에 대한 참조를 전달해야 한다. 이는 함수가 변수의 주소를 알고 변수 자의 복사본을 받지 않도록 하기 위한 것이다.

구조체에 대한 포인터
x와 y 방향으로 점을 전진시키는 함수를 만든다고 하자. 두 개의 포인터를 보내는 대신, 이제 포인터 구조의 함수로 하나의 포인터만 보낼 수 있다. 

void move(point * p) {
	(*p).x++;
	(*p).y++;
}

그러나 구조를 역참조하고 내부 구성요소 중 하나에 액세스하려는 경우, 데이터 구조에서 이 연산이 널리 사용되기 떄문에 그에 대한 간략한 구문이 있다. 다음 구문을 사용하여 이 함수를 다시 작성할 수 있다. 

void move(point * p) {
	p->x++;
	p->y++;
}

***
1.4 (2022-09-12) C언어 Advanced
***
동적 할당

메모리의 동적 할당은 C에서 매우 중요한 주제이다. 연결 리스트와 같은 복잡한 데이터 구조를 구축할 수 있다. 메모리를 동적으로 할당하면 프로그램을 작성할 당시 데이터의 크기를 처음에 알지 않고도 데이터를 저장할 수 있다. 

메모리 청크를 동적으로 할당하려면 새로 할당된 메모리의 위치를 저장할 포인터가 필요하다. 우리는 동일한 포인터를 사용하여 우리에게 할당된 메모리에 액세스할 수 있으며, 사용을 마치면 해당 포인터를 사용하여 메모리를 다시 해제할 수 있다. 

person 구조를 동적으로 할당한다고 가정해 보자. person은 다음과 같이 정의된다.

typedef struct {
	char * name;
	int age;
} person;

myperson 인수에 새 사용자를 할당하려면 다음 구문을 사용한다. 

person * myperson = (person *) malloc(sizeof(person));

이것은 컴파일러에게 우리가 사람 구조를 메모리에 보유할 수 있을 만큼만 동적으로 할당하고 나서 새로 할당된 데이터 유형으로 person 포인터를 반환하기를 원한다는 것을 알려준다. 메모리 할당 함수 malloc()는 지정된 메모리 공간을 예약한다. 이 경우 이 크기는 사용자 크기(바이트)이다. 

우리가 malloc()에 호출하기 전에 (person *)을 쓰는 이유는 malloc()이 유형이 없는 포인터인 "void pointer"를 반환하기 때문이다. 앞에 (person *)를 쓰는 것을 typecast라고 하며, malloc()에서 반환되는 포인터의 유형을 person이 되도록 변경한다. 그러나 C는 당신이 캐스트를 입력하지 않으면 반환된 포인터의 유형을 암시적으로(이경우, myperson) 포인터의 유형으로 변환하기 때문에 반드시 이렇게 쓸 필요는 없다. 

"sizeof"는 실제 함수가 아니다. 그 이유는 컴파일러가 이를 해석하고 사용자 구조의 실제 메모리 크기로 변환하기 때문이다. 
사용자 구성원에 접근하기 위해 -> 표기법을 사용할 수 있다. 

myperson->name = "John";
myperson->age = 27;

동적으로 할당된 구조를 사용한 후, 다음과 같이 free로 해제할 수 있다.

free(myperson);

free는 myperson 변수 자체를 삭제하지 않으며, 단순히 가리키는 데이터를 릴리즈한다. myperson 변수는 여전히 메모리의 어딘가를 가리킬 것이지만, myperson에게 호출한 후 더 이상 그 지역에 접근할 수 없다. 포인터를 사용하여 새 데이터를 할당할 때까지 해당 포인터를 다시 사용하면 안된다.

연습하기


#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int x;
  int y;
} point;

int main() {
  point * mypoint;

  mypoint = (point *)malloc(sizeof(point));

  mypoint->x = 10;
  mypoint->y =5 ;
  printf("mypoint coordinates: %d, %d\n", mypoint->x, mypoint->y);

  free(mypoint);
  return 0;
}
