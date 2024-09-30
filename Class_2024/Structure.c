# include<stdio.h>
struct Structure{
    int myNum;
    char myLetter;
};
int main(){
    struct Structure s1;

    s1.myNum=12;
    s1.myLetter='A';

    printf("My Number is :%d  \n",s1.myNum);
    printf("My Letter is : %c ",s1.myLetter);

}