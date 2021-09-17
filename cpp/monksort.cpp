#include<iostream>
#include<cstring>
#include<cstdlib>

using namespace std;

void print(int data[]) {
    for (int i = 0; i < 10; i++)
        cout << data[i] << "->";
    cout << "end" << endl;
}

bool check(const int data[]) {
    for (int i = 0; i < 9; i++)
        if (data[i] > data[i + 1])
            return false;
    return true;
}

void monkSort(const int input[], int output[]) {
    int count = 0;
    int flag[10];
    memset(reinterpret_cast<wchar_t *>(flag), 0, sizeof(flag));
    while (count < 10) {
        int index = rand() % 10;   //生成0-9之间的数
        if (!flag[index]) {
            flag[index] = 1;
            output[count++] = input[index];
        }
    }
}

int main() {
    int input[10] = {19, 23, 4, 67, 89, 10, 3, 55, 34, 98};
    int output[10];
    memset(output, 0, sizeof(output));
    //int output[10] = {0,0,0,0,0,0,0,0,0,0};
    bool ok = false;
    long count = 0;
    print(input);
    print(output);
    while (!ok) {
        count++;
        monkSort(input, output);
        ok = check(output);
        if (count % 100000 == 0) {
            cout << "第" << count << "次猴子排序";
            print(output);
        }
    }
    cout << "第" << count << "次猴子排序排序成功";
    cout << endl;
    print(input);
    print(output);
    cout << endl;
    return 0;
}