#include <pthread.h>
// linux环境下使用 man pthread_mutex_init 查看帮助文档

typedef struct {
    int n;
    pthread_mutex_t foo_mutex;
    pthread_mutex_t bar_mutex;
} FooBar;

extern void printFoo();
extern void printBar();

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    pthread_mutex_init(&obj->foo_mutex, NULL);
    pthread_mutex_init(&obj->bar_mutex, NULL);
    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        // printFoo() outputs "foo". Do not change or remove this line.
        pthread_mutex_lock(&obj->foo_mutex);
        printFoo();
        pthread_mutex_unlock(&obj->bar_mutex);
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&obj->bar_mutex);
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        pthread_mutex_unlock(&obj->foo_mutex);
    }
}

void fooBarFree(FooBar* obj) {
    pthread_mutex_destroy(&obj->foo_mutex);
    pthread_mutex_destroy(&obj->bar_mutex);
}